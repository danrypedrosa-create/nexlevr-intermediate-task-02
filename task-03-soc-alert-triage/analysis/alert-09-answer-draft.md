# Alert 09 — Normal Administrative Activity

**Case:** [NEX-INT-009](../alerts/alert-09.md)  
**Verdict:** False Positive (approved RDP session)  
**Severity:** Low  
**Document status:** Prepared answer for my review; this is not a separately recorded independent verdict.  
**Data:** Synthetic training alert, not a real client incident.

## Reasoning

I classified this as False Positive because the RDP login occurred within the approved service ticket SR-822 window. The account, source IP and destination host match the ticket, and MFA was approved. Although an off-hours RDP login can be suspicious, the supplied evidence supports an authorized maintenance session.

## Recommended Action

I would verify the ticket with the assigned support team and review the session details for any activity outside the approved scope. If nothing else is suspicious, I would document the ticket number and close the alert according to SOC procedures.

## Evidence limitations

The supplied scenario does not include a complete post-login activity history.

## Note

Off-hours authentication is not malicious by itself.

For the separate AI assessment, see [AI triage 09](ai-triage-09.md).
