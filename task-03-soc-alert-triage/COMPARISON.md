# SOC Alert Triage — Verdict Comparison

I prepared ten fictional alerts and compared the two verdicts I independently recorded with the model's assessments. For Alerts 03–10, the column contains verdicts from first-person answer drafts prepared by the model, not my own independent judgments.

| Alert | Scenario | My verdict / severity | Model verdict / severity | Observation |
|---|---|---|---|---|
| 01 | SSH failed passwords (47 attempts) | TP / Medium | TP / Medium | We agree; no account compromise is confirmed |
| 02 | SSH login after 18 failed attempts | TBC / Medium | TBC / High | We agree on TBC but differ on severity |
| 03 | Word launches encoded PowerShell | TP / High | TP (suspicious pattern) / High | Prepared draft; suspicious command chain, compromise not proven |
| 04 | Possible internal port scan | TBC / Medium | TBC / Medium | Prepared draft; verify approved scanner |
| 05 | Credential-phishing email | TP / Medium | TP (suspicious pattern) / Medium | Prepared draft; phishing signs, no proven credential theft |
| 06 | New approved scheduled task | FP / Low | FP (authorized activity) / Low | Prepared draft; approved task creation |
| 07 | EICAR test-file detection | FP / Low | FP (not a real malware infection) / Low | Prepared draft; EICAR test, not a malware incident |
| 08 | Repeated rundll32 outbound traffic | TBC / High | TBC / High | Prepared draft; possible beaconing, not confirmed |
| 09 | Off-hours RDP login | FP / Low | FP (authorized activity) / Low | Prepared draft; approved RDP session |
| 10 | Large rclone outbound transfer | TBC / High | TBC / High | Prepared draft; transfer requires verification |

## My findings

For **Alert 01**, I chose True Positive and Medium severity because 47 failed logins in five minutes were suspicious. The model agreed. Neither assessment confirms a successful login.

For **Alert 02**, I chose TBC and Medium severity because the source IP and deployment purpose had not been verified. The model also chose TBC but recommended High severity because the `deploy` account successfully authenticated after multiple failures.

For **Alerts 03–10**, I included the [prepared answer drafts](analysis/) in the verdict column for easy access. Both sets of entries came from the model, so their matching results are not independent comparisons.

The main risk I noticed is **overconfidence**. I should not classify a confirmed account compromise, malware infection, command-and-control connection, or data exfiltration without supporting evidence. Approved tasks, authorized tests and scheduled maintenance can also trigger valid detections.

**Note:** Prepared drafts are awaiting my own review. Only Alerts 01 and 02 have independent verdicts for comparison.

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
