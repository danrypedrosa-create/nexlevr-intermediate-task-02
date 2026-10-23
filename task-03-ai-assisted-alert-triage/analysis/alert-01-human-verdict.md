# Alert 01 — Human-first SOC investigation

**Alert ID:** NEX-INT-001  
**Scenario:** Synthetic SSH Authentication Failure Spike  
**Human verdict:** True Positive  
**Human severity:** High  
**Analyst-suggested alert name:** Login Time Anomaly

## Original analyst reasoning (preserved)

> The source IP was using a public IP 203.0.113.45; Though public IP alone doesn't prove that this is malicious, but having 47 loging attempts under 5 minutes is malicious. The name of this alert would Login Time Anomaly because of Failed login attempts in a short period of time. The severity of this is High given that the 47 login attempts was trying to access different privileges e.g admin, root, and test for only 5minutes.

## Original recommended action (preserved)

> Will be following the NIST Incident Response Lifecycle. Starting with Preparation Detection and Analysis, following by Containtment, Eradication and Recovery and Lastly the Post-Incident Activity

## Supplied synthetic alert context

- Source: 203.0.113.45 (documentation-only IP)
- Destination: 192.0.2.20 (documentation-only IP), LAB-LINUX-01, TCP/22
- Detection summary: 47 failed SSH authentication attempts over five minutes
- Excerpted usernames: admin, root, test
- No successful SSH authentication event was supplied in the excerpts

## Analyst feedback (not part of original human verdict)

- Repeated failures across usernames support attempted credential guessing; compromise is not confirmed.
- Public IP alone is not proof of maliciousness.
- root is privileged, while admin and test may or may not be privileged.
- Specific follow-up checks: search successful logins, review host and IP activity, consider validated containment.

**AI triage verdict:** Pending. Do not overwrite the independent human verdict.
