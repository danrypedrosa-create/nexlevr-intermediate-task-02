# Alert 08 — Suspicious Outbound Connection

**Case:** [NEX-INT-008](../alerts/alert-08.md)  
**Verdict:** To Be Confirmed  
**Severity:** High  
**Document status:** Prepared answer for my review; this is not a separately recorded independent verdict.  
**Data:** Synthetic training alert, not a real client incident.

## Reasoning

I marked this TBC because rundll32.exe initiated outbound HTTPS connections to the same IP approximately once every minute. The repeated pattern could indicate beaconing, but it does not confirm malware or command-and-control activity. The parent process, command line and destination ownership are missing, so I cannot determine why the connections occurred.

## Recommended Action

I would investigate the parent process, command line and loaded DLLs, then check DNS, proxy, firewall and EDR events for the same destination. I would verify whether the connection is expected and escalate promptly. I would recommend isolating the endpoint if supporting evidence confirms suspicious or active malicious behavior.

## Evidence limitations

No payload, destination reputation, process parent or authorization evidence is included.

## Note

Repeated periodic traffic can suggest beaconing without proving it.

For the separate AI assessment, see [AI triage 08](ai-triage-08.md).
