# NEXLEVR Intermediate — Cybersecurity Tasks

I use this repository to document my cybersecurity training labs and sample-data investigations, separate from my NEXLEVR Beginner repository.

| Task | Requirement | Status |
| --- | --- | --- |
| [01 — Wazuh SOC Lab](task-01-wazuh-soc-lab/README.md) | Set up a virtual SIEM, generate test activity, show alerts | Lab tests and eight screenshots documented; credential rotation pending |
| [02 — Sigma Detection Rules](task-02-sigma-detection-rules/README.md) | Write five rules, test sample logs and discuss false positives | Five rules, 15/15 limited synthetic matcher results and screenshots; official Sigma CLI validation pending |
| [03 — SOC Alert Triage](task-03-soc-alert-triage/README.md) | Review ten simulated alerts and compare my verdicts with model responses | Ten alert cases and reviews prepared; I independently assessed two cases |

## Task 01 — Findings

I set up a fresh **Ubuntu Server 24.04 LTS** virtual machine with Wazuh and generated controlled SSH authentication failures. In Threat Hunting, I observed six matching events. Wazuh rule **2502** generated a level **10** alert mapped to **MITRE ATT&CK T1110 — Brute Force**.

The activity was generated in a training lab, not by an unauthorized attacker. This VM was separate from my existing Kali, pfSense and Wazuh labs. No client data was used.

I saved [eight evidence screenshots](task-01-wazuh-soc-lab/evidence/) that do not include the earlier images containing credentials. I still need to rotate the previously exposed lab credentials.

My remaining steps are tracked in [SUBMISSION.md](SUBMISSION.md).
