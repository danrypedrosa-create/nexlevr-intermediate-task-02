# Alert 04 — Possible Internal Port Scan

**Alert ID:** NEX-INT-004  
**Time:** 2026-10-23 11:02 UTC  
**Host:** LAB-APP-04  
**Initial detector severity:** Medium  
**Context:** Source 192.0.2.90; target 192.0.2.44; TCP ports 21-1024

## Detection summary

Single source sent SYN probes to 164 destination ports in 70 seconds; 11 SYN-ACK replies; no successful application authentication in provided evidence; scanner authorization list unavailable.

## Supporting synthetic log excerpts

```text
11:01:05 Zeek conn.log orig_h=192.0.2.90 resp_h=192.0.2.44 resp_p=21 proto=tcp conn_state=S0
11:01:06 Zeek conn.log orig_h=192.0.2.90 resp_h=192.0.2.44 resp_p=22 proto=tcp conn_state=SF
11:01:07 Zeek conn.log orig_h=192.0.2.90 resp_h=192.0.2.44 resp_p=23 proto=tcp conn_state=S0
11:02:14 IDS scan_summary src=192.0.2.90 dst=192.0.2.44 unique_dst_ports=164 window_seconds=70
11:02:14 IDS scan_summary syn_ack_responses=11
```

## Evidence limitations

SYN-ACK shows a responsive port, not compromise.

All IP addresses and domains in this exercise are reserved examples. The dataset and all events are **synthetic**; no real client logs or reputation lookups were used.

**For reference:** AI assessment is separately archived under `analysis/ai-triage-04.md`.
