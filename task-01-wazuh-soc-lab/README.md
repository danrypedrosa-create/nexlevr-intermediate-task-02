# Intermediate Task 01 — Wazuh Home SOC Lab

**Status:** Technical test complete; eight evidence screenshots uploaded to GitHub; credential rotation pending.  
**Date:** October 22, 2026  
**Scope:** Personal training lab, not production.

## Objective

Set up a home SOC lab using Wazuh, generate test activity, and demonstrate the alerts produced.

## Architecture

```text
Mokka Linux host
    |
    | https://127.0.0.1:8443
    | (VirtualBox NAT port forwarding -> VM TCP 443)
    v
VirtualBox: NEXLEVR-Wazuh
    Ubuntu Server 24.04 LTS
    Wazuh Manager + Indexer + Dashboard + Filebeat
    sshd + journald log collection
    SSH test: nexlevr-test@127.0.0.1
```

This VM was installed separately from existing Kali, pfSense, and original Wazuh homelabs. No separate endpoint agent was deployed; Wazuh displayed local host/manager events (`agent.id: 000`).

## Installation and verification

1. Created fresh Ubuntu Server 24.04 LTS (Noble Numbat) in VirtualBox.
2. Used default VM NAT configuration.
3. Installed all-in-one Wazuh components.
4. Checked four services:

```bash
sudo systemctl is-active wazuh-manager wazuh-indexer wazuh-dashboard filebeat
```

**Observed:** All four returned `active`.

5. Forwarded host `127.0.0.1:8443` to guest TCP `443`. Verified dashboard login and access from Mokka.
6. Enabled SSH inside the test VM.

## Controlled test

```bash
sudo systemctl start ssh
sudo systemctl is-active ssh
ssh nexlevr-test@127.0.0.1
```

Entered deliberately incorrect passwords for the nonexistent test user. Verified resulting log entries with:

```bash
sudo journalctl -u ssh --since "10 minutes ago" --no-pager | tail -n 30
```

Logs showed invalid-user, failed-password, and PAM authentication-failure events originating from the loopback IP `127.0.0.1`.

## Wazuh detection results

Wazuh **Threat Hunting → Events** search (`sshd`) returned **six matching events** for the controlled SSH test:

| Rule ID | Level | Observed description | Count |
| --- | ---: | --- | ---: |
| `5710` | 5 | sshd: Attempt to login using a non-existent user | 4 |
| `5503` | 5 | PAM: User login failed. | 1 |
| `2502` | 10 | syslog: User missed the password more than one time | 1 |
| **Total** | | | **6** |

The expanded rule `2502` event showed:

- Host: `nexlevr-wazuh`
- Agent ID: `000`
- Event collection location: `journald`
- Decoder: `sshd`
- Severity: **level 10**
- ATT&CK tactic: **Credential Access**
- ATT&CK technique: **T1110 — Brute Force**
- Event timestamp shown in dashboard: **October 22, 2026, 19:52:13**

## Analyst verdict

**True positive for repeated failed SSH logins, caused by an authorized test.** The security event and corresponding Wazuh alert were observed. This was an intentionally generated localhost test, **not** evidence of an external attack or confirmed system compromise. No unauthorized successful authentication was shown.

## Limitations

A single all-in-one VM was used. Remote agent registration, multi-host monitoring, alert response automation, and production scalability were outside the scope of this task.

## Evidence

Eight approved screenshots were supplied for this task. They exclude the earlier screenshots exposing passwords. See [evidence/README.md](evidence/README.md) for all eight verified files and their exact filenames.

## Security note

The Wazuh admin and other lab service credentials were visible in earlier troubleshooting images. Do **not** publish those images. Rotate exposed credentials before making this lab available beyond its current localhost-only access.

## Skills

Wazuh, Ubuntu Server, VirtualBox, Linux authentication logs, SSH, journald, SOC alert triage, MITRE ATT&CK mapping, evidence-based reporting.
