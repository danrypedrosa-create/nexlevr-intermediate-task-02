# Alert 07 — Antivirus Signature Detection

**Alert ID:** NEX-INT-007  
**Time:** 2026-10-23 13:14 UTC  
**Host:** WIN-QA-02  
**Initial detector severity:** High  
**Context:** User CORP\qa.operator; test file C:\QA\Samples\eicar-test.txt

## Detection summary

Endpoint AV reports an EICAR test signature and quarantine success. QA change ticket QA-118 authorizes the test on WIN-QA-02 at this time.

## Supporting synthetic log excerpts

```text
13:14:02 AV detection=EICAR-Test-File file=C:\QA\Samples\eicar-test.txt
13:14:03 AV action=Quarantine status=Success
13:14:04 ticket=QA-118 purpose=Antivirus detection check
QA-118 approved_host=WIN-QA-02 approved_operator=CORP\qa.operator
QA-118 test_window=2026-10-23 13:00-13:30 UTC
No additional malicious telemetry supplied
```

## Evidence limitations

The signature detection is genuine; the false positive concerns a malicious-infection interpretation.

All IP addresses and domains in this exercise are reserved examples. The dataset and all events are **synthetic**; no real client logs or reputation lookups were used.

**For reference:** AI assessment is separately archived under `analysis/ai-triage-07.md`.
