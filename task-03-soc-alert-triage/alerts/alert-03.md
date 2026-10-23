# Alert 03 — Suspicious PowerShell Encoded Command

**Alert ID:** NEX-INT-003  
**Time:** 2026-10-23 10:18:42 UTC  
**Host:** WIN-FINANCE-07  
**Initial detector severity:** High  
**Context:** CORP\j.santos; WINWORD.EXE -> powershell.exe PID 4820; 203.0.113.88:443

## Detection summary

A macro-enabled document from Downloads was opened about one minute before WINWORD.EXE launched hidden PowerShell with -EncodedCommand; PowerShell initiated a TCP connection.

## Supporting synthetic log excerpts

```text
Sysmon EventID 1 | User=CORP\j.santos | Image=powershell.exe | PID=4820
ParentImage=WINWORD.EXE | CommandLine=powershell.exe -NoProfile -WindowStyle Hidden -EncodedCommand <redacted>
Sysmon EventID 3 | Image=powershell.exe | PID=4820 | SourceIp=192.0.2.57 | DestinationIp=203.0.113.88 | DestinationPort=443 | Initiated=true
Security EventID 4688 | CreatorProcessName=WINWORD.EXE | NewProcessName=powershell.exe
File opened: Q4_Financial_Review.docm | payload and URL response not provided
```

## Evidence limitations

An initiated TCP session is not proof of downloaded malware, exfiltration, or a completed C2 connection.

All IP addresses and domains in this exercise are reserved examples. The dataset and all events are **synthetic**; no real client logs or reputation lookups were used.

**For reference:** AI assessment is separately archived under `analysis/ai-triage-03.md`.
