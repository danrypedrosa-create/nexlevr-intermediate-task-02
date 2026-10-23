# Alert 06 — New Windows Scheduled Task

**Alert ID:** NEX-INT-006  
**Time:** 2026-10-23 12:05 UTC  
**Host:** WIN-OPS-03  
**Initial detector severity:** Medium  
**Context:** CORP\it.admin; task \CorpOps\NightlyInventory; powershell.exe -File C:\CorpIT\inventory.ps1

## Detection summary

Windows Security 4698 shows scheduled task created. A separate approved change record CHG-2042 lists this host, administrator, task name and maintenance time.

## Supporting synthetic log excerpts

```text
12:05:10 Security EventID=4698 SubjectUserName=it.admin TaskName=\CorpOps\NightlyInventory
TaskContent: powershell.exe -NoProfile -File C:\CorpIT\inventory.ps1
Change record: CHG-2042 status=Approved
Authorized host: WIN-OPS-03; authorized account: CORP\it.admin
Authorized maintenance: 2026-10-23 12:00-12:30 UTC
Authorized task name: \CorpOps\NightlyInventory
```

## Evidence limitations

An approved change in this synthetic case does not automatically make similarly named tasks safe elsewhere.

All IP addresses and domains in this exercise are reserved examples. The dataset and all events are **synthetic**; no real client logs or reputation lookups were used.

**For reference:** AI assessment is separately archived under `analysis/ai-triage-06.md`.
