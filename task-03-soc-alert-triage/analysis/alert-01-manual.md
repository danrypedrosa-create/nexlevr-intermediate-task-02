# Alert 01 — SSH Brute-Force Activity

**Alert ID:** NEX-INT-001  
**Case type:** Synthetic training scenario  
**My verdict:** True Positive  
**My severity:** Medium  
**Assessment:** My original independent response

## Reasoning

The severity of this is Medium given that the 47 login attempts against different user e.g admin, root, and test under the short period of time. Having 47 brute-force login attempts under 5 minutes is suspicious but there is not enough information to confirm whether an account was compromised. The log evidence shows only 5 SSH BruteForce Authentication logs but none of them were successful. But True Positive means the detection correctly identified suspicious activity. It doesn't necessarily mean the attacker successfully accessed the system.

## Recommended Action

My approach would be investigate the SSH authentication logs immediately, checking other related activity confirm whether any login succeeded and consider blocking the IP if authorized. Document and escalate the findings base on the SOC procedures. I can also follow the first NIST Incident Response Lifecycle with Preparation, Detection and Analysis, we should also check if the source IP belongs to the authorized scanner.

## Evidence limitations

I was given five representative failed-login entries, while the detection summary reports 47 failures. No successful login is shown in those excerpts, but that does not rule out other activity. The sample uses documentation-only IP addresses.

## Comparison

The [model assessment](ai-triage-01.md) also classified the alert True Positive / Medium. I do not interpret that as proof of compromise.
