# Alert 01 — SSH Authentication Failure Spike

**Alert ID:** NEX-INT-001  
**Time:** 2026-10-23 08:15 UTC  
**Host:** LAB-LINUX-01  
**Initial detector severity:** Medium  
**Context:** Source 203.0.113.45; destination 192.0.2.20; SSH TCP/22

## Detection summary

47 failed password attempts in five minutes against admin, root, and test; five representative failures supplied; no successful login event in the supplied excerpts.

## Supporting synthetic log excerpts

```text
08:10:11 sshd: Failed password for invalid user admin from 203.0.113.45 port 50211 ssh2
08:10:24 sshd: Failed password for root from 203.0.113.45 port 50218 ssh2
08:11:03 sshd: Failed password for invalid user test from 203.0.113.45 port 50231 ssh2
08:12:46 sshd: Failed password for root from 203.0.113.45 port 50310 ssh2
08:14:52 sshd: Failed password for invalid user admin from 203.0.113.45 port 50389 ssh2
```

## Evidence limitations

Do not claim a compromised account or complete 47-event log review from five excerpts.

All IP addresses and domains in this exercise are reserved examples. The dataset and all events are **synthetic**; no real client logs or reputation lookups were used.

**For reference:** AI assessment is separately archived under `analysis/ai-triage-01.md`.
