# Alert 07 — Malware Detection

**Case:** [NEX-INT-007](../alerts/alert-07.md)  
**Verdict:** False Positive (no real malware incident)  
**Severity:** Low  
**Data:** Synthetic training alert, not a real client incident.

## Reasoning

I chose False Positive for a malware incident because the detected file is an EICAR antivirus test file, and approved QA ticket QA-118 confirms this test was scheduled on the affected endpoint. The antivirus successfully detected and quarantined the file. This means the security control worked, but the test file is not proof that real malware infected the system.

## Recommended Action

I would verify the approved QA ticket, confirm quarantine status, and save the antivirus alert as test evidence. I would report this as authorized security testing and close the malicious-infection alert based on the approved procedure.

## Evidence limitations

The antivirus signature match is genuine; the false-positive label refers only to interpreting the event as a real infection.


For comparison, see [AI triage 07](ai-triage-07.md).
