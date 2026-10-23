# Alert 10 — Possible Data Exfiltration via File Transfer Tool

**Alert ID:** NEX-INT-010  
**Time:** 2026-10-23 18:22 UTC  
**Host:** WIN-FINANCE-11  
**Initial detector severity:** High  
**Context:** User CORP\finance.ops; process rclone.exe; destination 198.51.100.222:443

## Detection summary

Endpoint network counters show about 2.4 GB transmitted over 19 minutes after business hours. Tool launched from Downloads; destination and transfer contents are not recognized in the supplied approved-backup list, but no data inspection or user confirmation is provided.

## Supporting synthetic log excerpts

```text
18:03:10 Sysmon EventID=1 Image=C:\Users\finance.ops\Downloads\rclone.exe User=CORP\finance.ops
18:03:12 Sysmon EventID=3 Image=rclone.exe DestinationIp=198.51.100.222 DestinationPort=443 Initiated=true
18:22:11 NetFlow summary src=192.0.2.111 dst=198.51.100.222 bytes_out=2576980378 duration_seconds=1139
Backup register: approved destinations 192.0.2.200 and 192.0.2.201
Destination 198.51.100.222: NOT LISTED
File inventory / transfer content: NOT PROVIDED
```

## Evidence limitations

Do not label confirmed data exfiltration without proof of transferred sensitive data and authorization status.

All IP addresses and domains in this exercise are reserved examples. The dataset and all events are **synthetic**; no real client logs or reputation lookups were used.

**For reference:** AI assessment is separately archived under `analysis/ai-triage-10.md`.
