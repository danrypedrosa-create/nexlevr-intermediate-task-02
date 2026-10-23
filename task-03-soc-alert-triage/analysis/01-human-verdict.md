# Alert 01 — Human-first SOC investigation

**Alert ID:** NEX-INT-001
**Scenario:** Synthetic SSH Authentication Failure Spike
**Source IP:** 203.0.113.45 (documentation address)
**Destination IP:** 192.0.2.20 (documentation address)
**Destination host:** LAB-LINUX-01
**Event time:** 2026-10-23 08:15 UTC
**Observed summary:** 47 failed SSH logins over five minutes, five excerpted logs for admin/root/test usernames, no successful login event supplied.

## Analyst's original submission (recorded before AI triage)

**Verdict:** True Positive

**Severity:** High

**Reasoning (verbatim):**
> The source IP was using a public IP 203.0.113.45; The name of this alert is Login Time Anomaly with Failed login attempts in a short period of time. The severity of this is High because it's a password spraying given that the 47 login attempts was done in only 5minutes

**Recommended Action (verbatim):**
> Report it to client but will automatically block this IP

## Analyst coaching notes (not a replacement for original verdict)

- Repeated failed SSH logins support suspected password guessing/brute-force behavior; password spraying specifically requires more information about attempts across accounts and password reuse.
- 203.0.113.45 is a reserved documentation IP in a synthetic alert, not a reputation finding.
- Blocking a source IP should depend on authorized response procedures and verification. No successful login or compromise was established by the provided excerpts.

## AI comparison

**Pending.** Preserve the human-first verdict until the later independent AI comparison. Do not treat coaching notes as an AI verdict.
