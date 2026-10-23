# NEXLEVR Intermediate Task 02 — Five Sigma Detection Rules

**Status:** Five experimental YAML rules committed with 15 synthetic test events and a limited sample matcher. The supplied sample tests were run in an isolated development environment (15/15 expected outcomes). Mokka terminal evidence showing **15/15 expected outcomes** is uploaded. Official Sigma validation is **not yet confirmed**.

## Assignment

Write **five Sigma rules** for techniques of choice, test them on sample logs, and explain the possible false-positive risk of each.

## Rules

| # | Rule | ATT&CK | Pattern | False-positive risk |
| --- | --- | --- | --- | --- |
| 1 | [Linux SSH failed password](rules/01_lnx_sshd_failed_password.yml) | T1110.001 | Single failed-password log line | User mistypes password; repeated events over time are needed to support brute-force assessment |
| 2 | [PowerShell encoded command](rules/02_win_powershell_encoded_command.yml) | T1059.001 | PowerShell process with EncodedCommand/-enc switch | Legitimate scripts/IT deployment |
| 3 | [Windows user account creation](rules/03_win_user_account_created.yml) | T1136 | Security Event ID 4720 | Normal onboarding or service accounts |
| 4 | [Windows scheduled task creation](rules/04_win_scheduled_task_created.yml) | T1053.005 | Security Event ID 4698 | Authorized backup, patching and installers |
| 5 | [Defender registry policy value set](rules/05_win_defender_policy_registry_change.yml) | T1562.001 | Sysmon Event ID 13 sets DisableRealtimeMonitoring to 1 | Authorized endpoint policy test; does **not** prove Defender stopped running |

## Reproducible samples

The [synthetic events](samples/synthetic_events.jsonl) provide three fixtures per rule: a suspicious-pattern match, a routine nonmatch, and a **benign match** that illustrates false-positive risk. These are made-up examples with no customer data.

The [test_rules.py](test_rules.py) script parses YAML and checks only the **restricted Sigma expressions present in these five rules**: logsource metadata, equality, string `contains`, string `endswith`, and a simple `selection` condition. This **is not a Sigma engine or official Sigma syntax validator**, and the fixtures are simplified normalized events rather than raw SIEM logs.

## Run the tests yourself on Mokka

You can run these on your Garuda Linux host **without touching any Kali, pfSense, Wazuh, or production SOC configuration**:

```bash
git clone https://github.com/danrypedrosa-create/nexlevr-intermediate-task-02.git
cd nexlevr-intermediate-task-02/task-02-sigma-detection-rules
python3 -m venv .venv
source .venv/bin/activate.fish  # Mokka uses fish shell
python -m pip install -r requirements.txt
python test_rules.py
```

If you already cloned the repository, use `git pull` in its root directory instead of cloning it again.

**Expected from this synthetic matcher:** 5 rules, 15/15 expected outcomes, five suspicious-pattern matches, five benign matches, five nonmatching examples. The uploaded Mokka terminal screenshot confirms the limited synthetic matcher returned 15/15 expected outcomes. Official Sigma validation remains outstanding.

For proper Sigma rule validation later, use the [official Sigma CLI](https://github.com/SigmaHQ/sigma-cli) and a backend/pipeline that maps the exact log fields. Conversion is not deployment. Some event sources require auditing or Sysmon configuration to be enabled.

## Evidence screenshots uploaded

The three PNGs are organized in the dedicated [`evidence/`](evidence/) folder, separate from the [`samples/`](samples/) folder:

- [01-rule-files.png](evidence/01-rule-files.png): five YAML filenames in the Mokka terminal, with GitHub repository view.
- [02-synthetic-tests.png](evidence/02-synthetic-tests.png): 15/15 expected outcomes from the limited Python matcher on Mokka.
- [03-rule-and-false-positives.png](evidence/03-rule-and-false-positives.png): PowerShell YAML rule, detection, falsepositives, and ATT&CK tags.

**Fish shell note:** Use `source .venv/bin/activate.fish` on Mokka. The uploaded terminal screenshot shows a harmless failed attempt to source the Bash activation file, followed by successful execution of `python test_rules.py`.

- `04-official-validation.png`: optional, only if official Sigma validation is actually run and verified.

See [TEST-REPORT.md](TEST-REPORT.md) for the full false-positive review.

## Notes

A **Sigma match is not proof of compromise**. SSH password failures, task creation, account creation, and encoded PowerShell can all be authorized. Validate context, time, affected device and user, and related events before escalating.

References: [Sigma rule specification](https://github.com/SigmaHQ/sigma-specification) · [Sigma CLI](https://github.com/SigmaHQ/sigma-cli) · [MITRE ATT&CK](https://attack.mitre.org/).
