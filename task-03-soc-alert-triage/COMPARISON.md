# SOC Alert Triage — Verdict Comparison

I prepared ten fictional alerts and compared the two verdicts I independently recorded with the model's assessments. For Alerts 03–10, I have prepared model-written answer drafts, but I have not recorded separate independent personal verdicts.

| Alert | Scenario | My verdict / severity | Model verdict / severity | Observation |
|---|---|---|---|---|
| 01 | SSH failed passwords (47 attempts) | TP / Medium | TP / Medium | We agree; no account compromise is confirmed |
| 02 | SSH login after 18 failed attempts | TBC / Medium | TBC / High | We agree on TBC but differ on severity |
| 03 | Word launches encoded PowerShell | Not independently assessed | TP (suspicious pattern) / High | Needs payload and endpoint review |
| 04 | Possible internal port scan | Not independently assessed | TBC / Medium | Authorized scanning not ruled out |
| 05 | Credential-phishing email | Not independently assessed | TP (suspicious pattern) / Medium | Delivered email; no confirmed credential theft |
| 06 | New approved scheduled task | Not independently assessed | FP (authorized activity) / Low | Change approval matches |
| 07 | EICAR test-file detection | Not independently assessed | FP (not a real malware infection) / Low | Approved test and quarantine |
| 08 | Repeated rundll32 outbound traffic | Not independently assessed | TBC / High | C2 is possible, not verified |
| 09 | Off-hours RDP login | Not independently assessed | FP (authorized activity) / Low | Ticket and MFA match |
| 10 | Large rclone outbound transfer | Not independently assessed | TBC / High | Data theft is not confirmed |

## My findings

For **Alert 01**, I chose True Positive and Medium severity because 47 failed logins in five minutes were suspicious. The model agreed. Neither assessment confirms a successful login.

For **Alert 02**, I chose TBC and Medium severity because the source IP and deployment purpose had not been verified. The model also chose TBC but recommended High severity because the `deploy` account successfully authenticated after multiple failures.

For **Alerts 03–10**, I can review the [prepared answer drafts](analysis/) and the model's reports, but these share their source and are not an independent two-party comparison. I cannot claim a personal verdict or a valid agreement rate for them.

The main risk I noticed is **overconfidence**. I should not classify a confirmed account compromise, malware infection, command-and-control connection, or data exfiltration without supporting evidence. Approved tasks, authorized tests and scheduled maintenance can also trigger valid detections.

**Verdict definitions:** TP = correctly flagged suspicious activity, not necessarily confirmed compromise; FP = no malicious incident indicated by the supplied context; TBC = more verification needed.

## Source assessments

- [My Alert 01 verdict](analysis/alert-01-manual.md)
- [My revised Alert 02 verdict](analysis/alert-02-manual.md)
- [Eight prepared answer drafts and ten model-generated triage reviews](analysis/)
- [Original simulated alerts](alerts/)

I do not report an AI accuracy percentage because only two cases have independent verdicts and the dataset does not establish full ground truth.

## Prepared answer drafts — Alerts 03–10

- [Alert 03 — Suspicious PowerShell (TP (suspicious) / High)](analysis/alert-03-answer-draft.md)
- [Alert 04 — Port scanning (TBC / Medium)](analysis/alert-04-answer-draft.md)
- [Alert 05 — Phishing email (TP (suspicious) / Medium)](analysis/alert-05-answer-draft.md)
- [Alert 06 — Scheduled task (FP (authorized) / Low)](analysis/alert-06-answer-draft.md)
- [Alert 07 — Malware detection (EICAR test) (FP (authorized test) / Low)](analysis/alert-07-answer-draft.md)
- [Alert 08 — Outbound connection (TBC / High)](analysis/alert-08-answer-draft.md)
- [Alert 09 — Administrative RDP activity (FP (authorized) / Low)](analysis/alert-09-answer-draft.md)
- [Alert 10 — Possible data exfiltration (TBC / High)](analysis/alert-10-answer-draft.md)

These drafts require my review before they can be called my own verdicts.
