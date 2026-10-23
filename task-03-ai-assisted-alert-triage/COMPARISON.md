# SOC Alert Triage — Human and AI Comparison

**Dataset:** Ten fictional security alerts. **Independent analyst verdicts:** Alerts 01 and 02. **AI verdicts:** all ten. **Alerts 03–10 were not independently assessed by the analyst.**

| Alert | Scenario | Analyst verdict / severity | AI verdict / severity | Comparison |
|---|---|---|---|---|
| 01 | 47 SSH password failures across usernames | TP / Medium | TP / Medium | Verdict and severity agree; no confirmed compromise |
| 02 | 18 SSH failures followed by successful deploy login | TBC / Medium | TBC / High | Verdict agrees; severity differs; source authorization remains unknown |
| 03 | Word launches hidden encoded PowerShell and connection | Not independently assessed | TP (suspicious activity) / High | AI-only example; cannot count as agreement |
| 04 | Internal port scan | Not independently assessed | TBC / Medium | Authorization unknown |
| 05 | Credential-phishing message | Not independently assessed | TP (suspicious activity) / Medium | Delivery shown; credential theft unconfirmed |
| 06 | Approved scheduled task | Not independently assessed | FP (authorized change) / Low | Approval supplied in simulated case |
| 07 | Authorized EICAR antivirus test | Not independently assessed | FP (not a malware incident) / Low | Genuine test alert, not a confirmed infection |
| 08 | Periodic outbound rundll32 connections | Not independently assessed | TBC / High | Suspected beaconing not proven |
| 09 | Approved off-hours RDP login | Not independently assessed | FP (authorized support) / Low | Ticket and MFA match |
| 10 | High-volume rclone transfer | Not independently assessed | TBC / High | Traffic volume shown; sensitive-data theft unproven |

**TP** means the suspicious pattern was correctly detected, not that compromise was established. **FP** here means no malicious incident is indicated by the available scenario context; the underlying telemetry can still be accurate. **TBC** means verification is needed.

## Comparison findings

- **Alert 01:** Both assessments identify likely password guessing and give Medium severity. The five log excerpts are not a full incident history.
- **Alert 02:** Both leave the login as TBC. The analyst chose Medium; the AI recommended High. The deployment account's permissions and the source's authorization would determine escalation.
- **Alerts 03–10:** There is no separate analyst verdict, so agreement, disagreement, or accuracy for these eight cannot be calculated. Their responses are model-generated demonstrations.
- **Overconfidence risks:** It would exceed the evidence to say there was a proven account takeover (01–02), confirmed document-based malware (03), proven C2 beaconing (08), or confirmed sensitive-data exfiltration (10).
- **True ground truth is limited:** Authorized test/change information is explicitly supplied for synthetic Alerts 06, 07, and 09. The remaining cases lack conclusive investigation evidence.

**No human-vs-AI accuracy rate is reported.** Agreement on two hand-selected synthetic scenarios is not a meaningful accuracy benchmark.

## Original independent assessments

- [Alert 01](analysis/alert-01-manual.md)
- [Alert 02 — revised](analysis/alert-02-manual.md)

Full [alert dataset](alerts/) and [AI assessments](analysis/).
