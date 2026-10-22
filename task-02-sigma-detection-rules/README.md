# Intermediate Task 02 — Sigma Detection Rules

**Status:** Not started. No completed Sigma test results are claimed.

## Requirement

Write five Sigma detection rules for techniques of choice, test each rule on sample logs, and explain its possible false-positive risk.

## Proposed topics

| Scenario | MITRE ATT&CK | Suggested evidence |
| --- | --- | --- |
| Failed SSH password guessing | T1110 | Linux SSH logs |
| Suspicious PowerShell use | T1059.001 | Windows process creation logs |
| Local account creation | T1136.001 | Windows Event ID 4720 |
| Scheduled task creation | T1053.005 | Windows Event ID 4698 |
| Defender protection disabled | T1562.001 | Defender Operational logs |

Every rule needs valid YAML, an appropriate log field schema, positive/negative sample events, reproducible test results, and false-positive analysis. Sigma is a rule format, not a standalone engine.

Do not publish production SOC customer data.
