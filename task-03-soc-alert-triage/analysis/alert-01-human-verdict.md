# Alert 01 — Human-first SOC investigation

**Alert ID:** NEX-INT-001  
**Scenario:** Synthetic SSH Authentication Failure Spike  
**Human verdict:** True Positive  
**Human severity:** Medium  
**AI verdict:** Pending

## Analyst's latest submitted assessment (verbatim)

**Reasoning:**

> The severity of this is Medium given that the 47 login attempts was trying to access different privileges the logs shows different attempts against different user e.g admin, root, and test under the short period of time. Having 47 login attempts under 5 minutes is malicious. The log evidence shows many SSH BruteForce Authentication logs but none of them were successful.

**Recommended Action:**

> My approach would be following the NIST Incident Response Lifecycle. Starting with Preparation, Detection and Analysis, followed by Containtment, Eradication and Recovery and Lastly the Post-Incident Activity

## Supplied synthetic alert context

- Source: 203.0.113.45 (documentation-only IP)
- Destination: 192.0.2.20 (documentation-only IP), LAB-LINUX-01, TCP/22
- Detection summary: 47 failed SSH authentication attempts over five minutes
- Excerpted usernames: admin, root, test
- No successful SSH authentication event was supplied in the excerpts; the full logs were not provided.

## Reviewer feedback (separate from analyst verdict)

- Repeated failures across usernames support attempted credential guessing; intent and compromise are not conclusively established.
- Different usernames do not necessarily indicate different privilege levels.
- Next steps: search full authentication history for successful logins, confirm authorized testing context, assess source and host activity, and escalate for containment if warranted.

## Version note

An earlier draft in this file recorded **High** severity and different wording. The analyst's newer submitted assessment above supersedes that draft for the Human vs. AI comparison. Git history retains the earlier draft.

**AI triage verdict:** Pending. Preserve the analyst's latest independent response above unchanged.
