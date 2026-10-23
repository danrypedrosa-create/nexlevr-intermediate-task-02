# Alert 01 — SSH Brute-Force Activity

**Phase:** Independent human investigation (before AI assessment)
**Alert ID:** NEX-INT-001
**Dataset:** Synthetic training alert
**Human verdict:** True Positive
**Human severity:** Medium

## Analyst's original reasoning

> The severity of this is Medium given that the 47 login attempts against different user e.g admin, root, and test under the short period of time. Having 47 brute-force login attempts under 5 minutes is suspicious but there is not enough information to confirm whether an account was compromised. The log evidence shows only 5 SSH BruteForce Authentication logs but none of them were successful. But True Positive means the detection correctly identified suspicious activity. It doesn't necessarily mean the attacker successfully accessed the system.

## Analyst's original recommended action

> My approach would be investigate the SSH authentication logs immediately, checking other related activity confirm whether any login succeeded and consider blocking the IP if authorized. Document and escalate the findings base on the SOC procedures. I can also follow the first NIST Incident Response Lifecycle with Preparation, Detection and Analysis, we should also check if the source IP belongs to the authorized scanner.

## Evidence boundaries

- Detection summary: 47 failed SSH logins within five minutes, targeting admin, root and test.
- Five provided excerpts show failed passwords; these are a sample, not the full event set.
- No successful authentication appears in the provided excerpts; account compromise is **not established**.
- Source IP 203.0.113.45 and destination IP 192.0.2.20 are documentation addresses.
- This is a synthetic case, not a real client incident.

## Comparison status

**AI verdict:** Pending. Do not add or reveal until the independent human assessment phase is complete.
