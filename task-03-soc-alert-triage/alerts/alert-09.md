# Alert 09 — Off-Hours RDP Login

**Alert ID:** NEX-INT-009  
**Time:** 2026-10-23 16:48 UTC  
**Host:** WIN-SUPPORT-05  
**Initial detector severity:** Medium  
**Context:** User CORP\helpdesk2; source 192.0.2.120; destination WIN-SUPPORT-05 RDP/3389

## Detection summary

Successful RDP logon outside normal work hours. Authorized maintenance ticket SR-822 lists the same host, source address, user and time, with MFA success.

## Supporting synthetic log excerpts

```text
16:48:19 Security EventID=4624 LogonType=10 TargetUserName=helpdesk2 IpAddress=192.0.2.120
16:48:19 MFA event=Approved user=CORP\helpdesk2
16:48:20 RDP session established to WIN-SUPPORT-05
Ticket SR-822 status=Approved user=CORP\helpdesk2 host=WIN-SUPPORT-05
Ticket SR-822 approved_source=192.0.2.120 window=16:30-17:30 UTC
```

## Evidence limitations

Off-hours activity alone does not establish an attack.

All IP addresses and domains in this exercise are reserved examples. The dataset and all events are **synthetic**; no real client logs or reputation lookups were used.

**For reference:** AI assessment is separately archived under `analysis/ai-triage-09.md`.
