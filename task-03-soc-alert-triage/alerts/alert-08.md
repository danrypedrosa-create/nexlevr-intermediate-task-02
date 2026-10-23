# Alert 08 — Periodic Suspicious Outbound Connections

**Alert ID:** NEX-INT-008  
**Time:** 2026-10-23 14:09 UTC  
**Host:** WIN-FINANCE-03  
**Initial detector severity:** High  
**Context:** Process rundll32.exe PID 9012; destination 203.0.113.167:443

## Detection summary

Five short TLS connection attempts occur approximately every minute. Parent process, command line, destination ownership, payload, and endpoint owner approval are unavailable.

## Supporting synthetic log excerpts

```text
14:05:02 Sysmon EventID=3 Image=rundll32.exe PID=9012 DestinationIp=203.0.113.167 DestinationPort=443 Initiated=true
14:06:04 Sysmon EventID=3 Image=rundll32.exe PID=9012 DestinationIp=203.0.113.167 DestinationPort=443 Initiated=true
14:07:03 Sysmon EventID=3 Image=rundll32.exe PID=9012 DestinationIp=203.0.113.167 DestinationPort=443 Initiated=true
14:08:02 Sysmon EventID=3 Image=rundll32.exe PID=9012 DestinationIp=203.0.113.167 DestinationPort=443 Initiated=true
14:09:03 Sysmon EventID=3 Image=rundll32.exe PID=9012 DestinationIp=203.0.113.167 DestinationPort=443 Initiated=true
```

## Evidence limitations

A periodic connection pattern is not enough to confirm malware or a C2 channel.

All IP addresses and domains in this exercise are reserved examples. The dataset and all events are **synthetic**; no real client logs or reputation lookups were used.

**For reference:** AI assessment is separately archived under `analysis/ai-triage-08.md`.
