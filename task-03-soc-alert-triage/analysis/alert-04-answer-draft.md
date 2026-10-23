# Alert 04 — Port Scanning Activity

**Case:** [NEX-INT-004](../alerts/alert-04.md)  
**Verdict:** To Be Confirmed  
**Severity:** Medium  
**Document status:** Prepared answer for my review; this is not a separately recorded independent verdict.  
**Data:** Synthetic training alert, not a real client incident.

## Reasoning

I chose TBC because one source IP sent connection attempts to 164 TCP ports within 70 seconds, which is consistent with port scanning. But an authorized vulnerability scanner may produce the same activity. The 11 SYN-ACK responses only show that some ports answered, not that an attacker accessed or exploited the system.

## Recommended Action

I would check whether the source IP belongs to an approved scanner and review scheduled vulnerability assessments or change requests. I would search for similar connections to other hosts and escalate or recommend blocking only if the activity was not authorized.

## Evidence limitations

The source IP has not been checked against the authorized scanner list; no application compromise evidence was supplied.

## Note

A scan pattern can be confirmed without assuming malicious intent.

For the separate AI assessment, see [AI triage 04](ai-triage-04.md).
