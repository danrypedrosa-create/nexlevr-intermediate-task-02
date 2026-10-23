# Alert 10 — Possible Data Exfiltration

**Case:** [NEX-INT-010](../alerts/alert-10.md)  
**Verdict:** To Be Confirmed  
**Severity:** High  
**Document status:** Prepared answer for my review; this is not a separately recorded independent verdict.  
**Data:** Synthetic training alert, not a real client incident.

## Reasoning

I chose TBC because rclone.exe sent about 2.4 GiB to an external IP address after business hours, and the destination is not listed among the approved backup servers. That is a serious concern because rclone can be used to transfer files. However, the logs do not identify the transferred files or prove that confidential data was stolen. I cannot confirm data exfiltration based only on the traffic volume.

## Recommended Action

I would check the rclone command line, transfer logs, file access records, proxy or NetFlow details, and destination ownership. I would ask the account owner and client to confirm whether this transfer was approved, preserve evidence, and escalate urgently. I would recommend containment if the investigation shows an active unauthorized transfer.

## Evidence limitations

File names, data sensitivity, transfer purpose and destination ownership are not available.

## Note

Large traffic volume is a risk indicator, not proof of sensitive-data theft.

For the separate AI assessment, see [AI triage 10](ai-triage-10.md).
