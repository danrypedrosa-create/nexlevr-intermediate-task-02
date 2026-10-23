# Alert 05 — Credential-Harvest Phishing Email

**Alert ID:** NEX-INT-005  
**Time:** 2026-10-23 11:26 UTC  
**Host:** MAIL-GATEWAY-01  
**Initial detector severity:** Medium  
**Context:** Sender helpdesk@corp-security.example; recipient j.santos@corp.example; URL https://signin-review.example/verify

## Detection summary

Email impersonates internal IT, urges password verification within 30 minutes, displays a lookalike sender, and links to an unrelated sign-in domain; delivery confirmed but link-click and credential submission unknown.

## Supporting synthetic log excerpts

```text
11:26:01 MAIL accepted sender=helpdesk@corp-security.example recipient=j.santos@corp.example
11:26:02 SPF=fail DKIM=none DMARC=fail
Subject: ACTION REQUIRED: Verify Microsoft 365 Password
Body excerpt: Verify your account within 30 minutes to avoid suspension.
URL: https://signin-review.example/verify
11:26:03 delivery_status=delivered
Click telemetry: NOT PROVIDED
```

## Evidence limitations

Email delivery does not establish a successful phishing compromise.

All IP addresses and domains in this exercise are reserved examples. The dataset and all events are **synthetic**; no real client logs or reputation lookups were used.

**For reference:** AI assessment is separately archived under `analysis/ai-triage-05.md`.
