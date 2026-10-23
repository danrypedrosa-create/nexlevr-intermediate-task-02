# Alert 01 — SSH Brute-Force Activity

**Source:** Synthetic training scenario NEX-INT-001 (not real client data)
**Phase:** Independent human assessment; AI verdict intentionally withheld
**Analyst verdict:** True Positive (attempted SSH password guessing)
**Analyst severity:** Medium

## Analyst's original reasoning

> The severity of this is Medium given that the 47 login attempts against different user e.g admin, root, and test under the short period of time. Having 47 login attempts under 5 minutes is suspicious. The log evidence shows many SSH BruteForce Authentication logs but none of them were successful.

## Analyst's original recommended action

> My approach would be following the NIST Incident Response Lifecycle. Starting with Preparation, Detection and Analysis, followed by Containtment, Eradication and Recovery and Lastly the Post-Incident Activity. Specifically we investigate the SSH authentication logs, checking other related activity confirm whether any login succeeded and consider blocking the IP if authorized. Document and escalate the findings base on the SOC procedure

## Evidence boundaries

- The alert summary reports 47 failed SSH logins in five minutes; the provided excerpt contains five representative failed-login events targeting admin, root, and test.
- No successful login is shown in the provided excerpts. This does not establish that no successful login occurred elsewhere.
- The true-positive assessment concerns suspicious password-guessing attempts, **not** a confirmed compromise.
- No AI verdict or ground-truth outcome has been entered yet.
