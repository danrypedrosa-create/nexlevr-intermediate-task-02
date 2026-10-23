# Alert 01 — SSH Brute-Force Activity

**Dataset:** Synthetic training scenario; IP addresses are documentation-only examples.  
**Status:** Human-first assessment recorded; AI comparison pending.

## Alert data
- Alert ID: NEX-INT-001
- Alert name: SSH Authentication Failure Spike
- Time: 2026-10-23 08:15 UTC
- Source IP: 203.0.113.45
- Destination IP: 192.0.2.20
- Host: LAB-LINUX-01
- Service: SSH / TCP 22
- Detection summary: 47 failed logins in 5 minutes
- Sample logs: Failed passwords for admin, root, and test; no successful authentication shown in supplied excerpts

## Original human assessment (preserved verbatim)

> Alert 01 — SSH Brute-Force Activity
>
> Verdict: True Positive
> Severity: Medium
>
> Reasoning:
> The severity of this is Medium given that the 47 login attempts was trying to access different privileges e.g admin, root, and test under the short period of time but no successful SSH Authentication.
>
> The source IP was using a public IP 203.0.113.45; Though public IP alone doesn't prove that this is malicious, but having 47 login attempts under 5 minutes is malicious. The name of this alert would Login Time Anomaly because of many failed login attempts.
>
> Recommended Action:
> My approach would be following the NIST Incident Response Lifecycle. Starting with Preparation, Detection and Analysis, followed by Containtment, Eradication and Recovery and Lastly the Post-Incident Activity

## Coaching notes (not part of original verdict)
- Different account names do not necessarily indicate different privilege levels.
- No successful SSH authentication is shown in the provided excerpts; this does not prove none occurred elsewhere.
- Recommended operational checks: search complete SSH authentication logs for successes, determine whether activity was authorized, assess affected account status, and escalate or block according to approved procedures.
- More specific alert name: SSH Brute-Force Activity / SSH Login Failure Anomaly.

**AI verdict:** Withheld until human-first assessments are complete.
