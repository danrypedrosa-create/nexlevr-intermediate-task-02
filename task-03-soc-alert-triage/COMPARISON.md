# SOC Alert Triage — Verdict Comparison

I compared ten synthetic alert classifications side by side. I independently recorded Alerts 01 and 02. The written answers for Alerts 03–10 were produced by ChatGPT from the same evidence as its model assessments.

| Alert | Scenario | My verdict / severity | Model verdict / severity | Observation |
|---|---|---|---|---|
| 01 | SSH failed passwords (47 attempts) | TP / Medium | TP / Medium | We agree; no account compromise is confirmed |
| 02 | SSH login after 18 failed attempts | TBC / Medium | TBC / High | We agree on TBC but differ on severity |
| 03 | Word launches encoded PowerShell | [TP / High](analysis/alert-03-answer.md) | TP (suspicious pattern) / High | Same verdict and severity; suspicious command chain |
| 04 | Possible internal port scan | [TBC / Medium](analysis/alert-04-answer.md) | TBC / Medium | Same verdict and severity; scan authorization unknown |
| 05 | Credential-phishing email | [TP / Medium](analysis/alert-05-answer.md) | TP (suspicious pattern) / Medium | Same verdict and severity; credential theft unconfirmed |
| 06 | New approved scheduled task | [FP / Low](analysis/alert-06-answer.md) | FP (authorized activity) / Low | Same verdict and severity; approved task creation |
| 07 | EICAR test-file detection | [FP / Low](analysis/alert-07-answer.md) | FP (not a real malware infection) / Low | Same verdict and severity; approved EICAR test |
| 08 | Repeated rundll32 outbound traffic | [TBC / High](analysis/alert-08-answer.md) | TBC / High | Same verdict and severity; beaconing not confirmed |
| 09 | Off-hours RDP login | [FP / Low](analysis/alert-09-answer.md) | FP (authorized activity) / Low | Same verdict and severity; approved RDP session |
| 10 | Large rclone outbound transfer | [TBC / High](analysis/alert-10-answer.md) | TBC / High | Same verdict and severity; data theft unconfirmed |

## My findings

For **Alert 01**, I chose True Positive and Medium severity because 47 failed logins in five minutes were suspicious. The model agreed. Neither assessment confirms a successful login.

For **Alert 02**, I chose TBC and Medium severity because the source IP and deployment purpose had not been verified. The model also chose TBC but recommended High severity because the `deploy` account successfully authenticated after multiple failures.

For **Alerts 03–10**, the verdict column links to the full written answers. Both answers and AI assessments came from the same model, so the matching results do not count as separate human-versus-AI comparisons.

The main risk I noticed is **overconfidence**. I should not classify a confirmed account compromise, malware infection, command-and-control connection, or data exfiltration without supporting evidence. Approved tasks, authorized tests and scheduled maintenance can also trigger valid detections.

**Comparison scope:** Alerts 01 and 02 are my independently submitted verdicts. Alerts 03–10 show generated answers for review. A matching pair prepared by the same model does not prove the AI was right.

**Verdict definitions:** TP = correctly flagged suspicious activity, not necessarily confirmed compromise; FP = no malicious incident indicated by the supplied context; TBC = more verification needed.

## Source assessments

- [My Alert 01 verdict](analysis/alert-01-manual.md)
- [My revised Alert 02 verdict](analysis/alert-02-manual.md)
- [All ten written answers and ten model assessments](analysis/)
- [Original simulated alerts](alerts/)

I do not report an AI accuracy percentage because only two cases have independent verdicts and the dataset does not establish full ground truth.
