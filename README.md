# NEXLEVR Intermediate — Cybersecurity Tasks

Hands-on cybersecurity training projects using personal laboratory systems and sample data, separate from my NEXLEVR Beginner repository.

| Task | Requirement | Status |
| --- | --- | --- |
| [01 — Wazuh SOC Lab](task-01-wazuh-soc-lab/README.md) | Set up a virtual SIEM, generate test activity, show alerts | **Technical testing and eight evidence screenshots uploaded; credential rotation pending** |
| [02 — Sigma Detection Rules](task-02-sigma-detection-rules/README.md) | Write five Sigma rules, test sample logs, explain false-positive risk | Not started |
| [03 — AI-Assisted Alert Triage](task-03-ai-assisted-alert-triage/README.md) | Independently triage ten alerts and compare with AI verdicts | Not started |

## Task 01 — Verified findings

A fresh **Ubuntu Server 24.04 LTS** VM running **Wazuh** detected controlled SSH authentication failures against the local test host. In **Threat Hunting**, six matching events were observed. Wazuh rule **2502** produced a level **10** detection with **MITRE ATT&CK T1110 — Brute Force** mapping.

These events were intentionally generated in an authorized training lab. They do **not** indicate unauthorized access, an external attacker, or a confirmed compromise.

The new VM was separate from the existing Kali, pfSense, and original Wazuh home labs. No real customer data was used.

The eight reviewed screenshots are now uploaded in [Task 01 evidence](task-01-wazuh-soc-lab/evidence/). The older screenshots containing passwords are excluded. Previously exposed Wazuh lab credentials should be rotated.

See [SUBMISSION.md](SUBMISSION.md) for the remaining checklist.
