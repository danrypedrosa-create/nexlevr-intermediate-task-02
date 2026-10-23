# Task 03 — My Verdict vs AI Verdict

I placed my first two independently submitted verdicts and the written answers for Alerts 03–10 beside the model classifications so I can compare the results quickly. All ten alert cases are **synthetic training data**, not real client investigations.

## At-a-glance verdict comparison

| Alert | Scenario | My verdict | My severity | AI verdict | AI severity | Comparison |
|:---:|---|---|---|---|---|---|
| [01](alerts/alert-01.md) | SSH brute-force activity | **True Positive** | **Medium** | True Positive (suspicious activity) | Medium | **Same verdict and severity** |
| [02](alerts/alert-02.md) | Successful SSH login after failures | **To Be Confirmed** | **Medium** | To Be Confirmed | High | **Same verdict, different severity** |
| [03](alerts/alert-03.md) | Suspicious PowerShell execution | **[True Positive](analysis/alert-03-answer.md)** | **High** | True Positive (suspicious activity) | High | Same verdict and severity; suspicious command chain |
| [04](alerts/alert-04.md) | Possible internal port scan | **[To Be Confirmed](analysis/alert-04-answer.md)** | **Medium** | To Be Confirmed | Medium | Same verdict and severity; scan authorization unknown |
| [05](alerts/alert-05.md) | Credential-phishing email | **[True Positive](analysis/alert-05-answer.md)** | **Medium** | True Positive (suspicious activity) | Medium | Same verdict and severity; credential theft unconfirmed |
| [06](alerts/alert-06.md) | Approved scheduled task | **[False Positive](analysis/alert-06-answer.md)** | **Low** | False Positive (authorized activity) | Low | Same verdict and severity; approved task creation |
| [07](alerts/alert-07.md) | Authorized EICAR antivirus test | **[False Positive](analysis/alert-07-answer.md)** | **Low** | False Positive (not a malware incident) | Low | Same verdict and severity; approved EICAR test |
| [08](alerts/alert-08.md) | Periodic outbound connections | **[To Be Confirmed](analysis/alert-08-answer.md)** | **High** | To Be Confirmed | High | Same verdict and severity; beaconing not confirmed |
| [09](alerts/alert-09.md) | Approved off-hours RDP login | **[False Positive](analysis/alert-09-answer.md)** | **Low** | False Positive (authorized activity) | Low | Same verdict and severity; approved RDP session |
| [10](alerts/alert-10.md) | Large outbound rclone transfer | **[To Be Confirmed](analysis/alert-10-answer.md)** | **High** | To Be Confirmed | High | Same verdict and severity; data theft unconfirmed |

**TP** = True Positive (suspicious behavior detected, not automatically a confirmed compromise). **FP** = False Positive as a malicious-incident classification. **TBC** = To Be Confirmed.

**Comparison scope:** I independently submitted Alerts 01 and 02. The Alert 03–10 answers and the corresponding model assessments were both prepared by ChatGPT from the same synthetic logs. Their matching outcomes are shown for reference, not counted as separate human-versus-AI agreement.


## Alert 01 — SSH Brute-Force Activity

| My assessment | AI assessment |
|---|---|
| **Verdict:** True Positive | **Verdict:** True Positive (suspicious detection) |
| **Severity:** Medium | **Severity:** Medium |
| **My reasoning:** 47 failed SSH attempts against accounts including admin, root and test within five minutes are suspicious. Only five failure entries were shown, and I cannot confirm a successful compromise. | **AI reasoning:** Repeated password failures against changing usernames suggest attempted password guessing. The provided logs do not confirm an accepted login or compromise. |
| **My recommended action:** Investigate the full SSH log history, verify any successful authentication, check whether the IP belongs to an authorized scanner, and consider blocking and escalation if authorized. | **AI recommended action:** Search for accepted logins, validate the source and related hosts, consider rate limiting or blocking with approval, and document/escalate. |

**My comparison:** Our verdicts and severity match. The important limitation is that suspicious login failures do not prove that an account was accessed.

[My original response](analysis/alert-01-manual.md) · [AI response](analysis/ai-triage-01.md)

## Alert 02 — SSH Login After Multiple Failures

| My assessment | AI assessment |
|---|---|
| **Verdict:** To Be Confirmed | **Verdict:** To Be Confirmed |
| **Severity:** Medium | **Severity:** High |
| **My reasoning:** A legitimate user may have entered a forgotten password repeatedly, but I cannot confirm whether the successful login to the `deploy` account was authorized or compromised. | **AI reasoning:** The accepted SSH login confirms access, not authorization. A deployment account may have important permissions and deserves prompt review after repeated failures. |
| **My recommended action:** Check whether the source IP belongs to an approved deployment system, review post-login activity, and ask the client whether the activity was expected. | **AI recommended action:** Verify approved deployment IPs, deployment windows and account ownership; examine post-login activity and escalate unexpected access. |

**My comparison:** We both selected TBC, but I chose Medium while the AI suggested High. I would verify the account's access level and authorization before finalizing the priority. The forgotten-password explanation remains only a possibility.

[My revised response](analysis/alert-02-manual.md) · [AI response](analysis/ai-triage-02.md)

## What I found from the comparison

- **Verdict agreement:** 2 of 2 cases where I gave my own independent verdict.
- **Severity agreement:** 1 of 2 comparable cases.
- **Other cases:** The written answers for Alerts 03–10 are linked directly from the main table. Matching results from the same model are not independent comparisons.
- **Accuracy:** I am not reporting an AI accuracy rate because these synthetic cases do not provide enough independent ground truth.

My main takeaway is to check the available evidence, verify whether the activity was authorized, and avoid claiming compromise or malicious intent when the logs do not prove it.

See the [final report](FINAL-REPORT.md) or [full comparison notes](COMPARISON.md) for more context.
