# Alert 02 — SSH Login After Multiple Failures

**Alert ID:** NEX-INT-002  
**Time:** 2026-10-23 09:42 UTC  
**Host:** LAB-WEB-02  
**Initial detector severity:** High  
**Context:** User deploy; source 198.51.100.77; destination 192.0.2.35; SSH TCP/22

## Detection summary

18 failed passwords for deploy followed by one accepted password and an opened SSH session from the same source IP. Source approval and post-login activity unavailable.

## Supporting synthetic log excerpts

```text
09:37:04 sshd: Failed password for deploy from 198.51.100.77 port 53120 ssh2
09:37:19 sshd: Failed password for deploy from 198.51.100.77 port 53122 ssh2
09:38:11 sshd: Failed password for deploy from 198.51.100.77 port 53141 ssh2
09:40:36 sshd: Failed password for deploy from 198.51.100.77 port 53201 ssh2
09:41:57 sshd: Accepted password for deploy from 198.51.100.77 port 53218 ssh2
09:41:57 sshd: pam_unix(sshd:session): session opened for user deploy
```

## Evidence limitations

Successful authentication is not proof of account compromise; no post-login telemetry is included.

All IP addresses and domains in this exercise are reserved examples. The dataset and all events are **synthetic**; no real client logs or reputation lookups were used.

**For reference:** AI assessment is separately archived under `analysis/ai-triage-02.md`.
