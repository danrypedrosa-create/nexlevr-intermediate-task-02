# Alert 03 — Suspicious PowerShell Execution

**Case:** [NEX-INT-003](../alerts/alert-03.md)  
**Verdict:** True Positive (suspicious behavior)  
**Severity:** High  
**Document status:** Prepared answer for my review; this is not a separately recorded independent verdict.  
**Data:** Synthetic training alert, not a real client incident.

## Reasoning

I classified this as True Positive because Microsoft Word launched PowerShell with an encoded command and a hidden window. A macro-enabled document was opened shortly before that, and PowerShell initiated an outbound connection on port 443. This is a suspicious sequence that needs urgent investigation. However, I cannot confirm that malware executed or that data was stolen because the encoded command and network response were not provided.

## Recommended Action

I would check the document's source and hash, safely review the encoded PowerShell command, and search Sysmon, EDR and proxy logs for related processes and connections. I would escalate the alert and recommend endpoint isolation if the incident response team confirms active malicious behavior.

## Evidence limitations

The contents of the encoded command, the network response, and any later endpoint activity are unknown.

## Note

PowerShell launched by Word is suspicious but not automatic proof of compromise.

For the separate AI assessment, see [AI triage 03](ai-triage-03.md).
