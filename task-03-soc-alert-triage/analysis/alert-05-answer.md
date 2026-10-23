# Alert 05 — Phishing Email

**Case:** [NEX-INT-005](../alerts/alert-05.md)  
**Verdict:** True Positive (phishing indicators)  
**Severity:** Medium  
**Data:** Synthetic training alert, not a real client incident.

## Reasoning

I classified this as True Positive because the email pretends to be from IT and pressures the employee to verify a Microsoft 365 password within 30 minutes. SPF and DMARC failed, DKIM is missing, and the link uses an unrelated sign-in domain. These are strong signs of a credential-phishing attempt. However, delivery does not mean the recipient clicked the link or gave away credentials.

## Recommended Action

I would preserve the message and headers, search for other recipients, and request removal or quarantine according to email security procedures. I would verify whether the user clicked the link or entered credentials, and recommend a password reset and account review if exposure is confirmed. I would document the findings and report them to the client.

## Evidence limitations

User clicks, credential entry and account compromise are not confirmed.


For comparison, see [AI triage 05](ai-triage-05.md).
