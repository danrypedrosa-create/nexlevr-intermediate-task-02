# Task 03 — SOC Alert Triage: Final Report

## Objective

My goal was to practice reviewing security alerts, identifying suspicious behavior, recording a clear verdict and recommending the next investigation steps. I also compared my own decisions with model-generated triage examples.

## Method

I used **ten synthetic alerts**, not production SOC or client data. I independently recorded my decisions for **Alerts 01 and 02** before reviewing the corresponding model assessments. For Alerts 03–10, I prepared the investigation write-ups using model-generated examples, so I do not count them as my independent decisions.

I only worked with the details supplied in the simulated cases. I did not perform live log searches, endpoint scans, IP reputation checks, user confirmation or containment.

## Results

| Metric | Result |
|---|---|
| Simulated alerts documented | 10 |
| Model-generated reviews | 10 |
| My independent verdicts | 2 |
| Broad verdict agreements for those 2 | 2 of 2 |
| Severity agreement for those 2 | 1 of 2 |
| Confirmed real security incidents | 0 |
| Live production investigations | 0 |

These results describe a small training comparison, **not an AI accuracy score**.

## Investigation findings

**Alert 01 — SSH brute-force attempts:** I marked this True Positive with Medium severity because 47 failed SSH logins occurred within five minutes. The model reached the same conclusion. I would review the full authentication history and check whether any successful login occurred before escalating. The provided excerpts do not confirm account compromise.

**Alert 02 — Successful SSH login after failures:** I marked this To Be Confirmed with Medium severity. I would check whether the source IP belongs to an approved deployment system, review post-login activity, and ask the client to verify the session. The model also selected TBC but gave High severity because the deployment account successfully authenticated after repeated failures.

**Alert 03 — Encoded PowerShell:** The sample shows Word launching hidden encoded PowerShell before an outbound TCP connection. This is a suspicious pattern worth investigating, but I cannot confirm a malicious macro, completed data transfer or endpoint compromise from the supplied logs.

**Alerts 04–10:** The remaining simulated cases cover port scanning, phishing, scheduled task creation, antivirus testing, periodic outbound traffic, RDP access and possible data exfiltration. I documented each scenario and its model-generated triage assessment in the [comparison](COMPARISON.md).

## What I learned

I found that model responses can help me organize alert details, suggest useful log checks and identify missing evidence. But I still need to verify the source, affected account, change requests, process activity and complete event timeline.

I also learned to separate **suspicious detection** from **confirmed compromise**. For example, a true-positive alert does not automatically mean that an attacker accessed the system. A successful login, outbound connection or large transfer also needs context before I conclude that malicious activity occurred.

For my SOC workflow, I would use AI as a supporting tool and follow our approved investigation, escalation and reporting procedures before making a final operational decision.

## Limitations

The data is fictional and some log records are only excerpts. No IPs, hashes, files or affected hosts were independently verified. Since I submitted only two personal verdicts, I cannot claim ten independent human investigations or a meaningful accuracy percentage. I will also avoid uploading confidential client data into external tools without authorization.

## Project files

- [Ten synthetic alert cases](alerts/)
- [Investigation notes and model assessments](analysis/)
- [Comparison table](COMPARISON.md)
- [Evidence checklist](evidence/README.md)

The written project is organized for review. A full independent ten-alert comparison and NEXLEVR evaluator approval are still outstanding.
