# Task 02 — Synthetic Log Test Findings

**Inputs:** 5 experimental Sigma YAML rules and 15 synthetic JSONL events. **Testing method:** restricted Python teaching matcher. A full Sigma parser and a live SIEM/OpenSearch backend were not tested.

| Rule | Suspicious matching event | Expected nonmatch | Benign event also matching (false-positive example) | Important limitation |
| --- | --- | --- | --- | --- |
| Failed SSH password | Failed password for nonexistent user | Successful public-key SSH login | Ordinary password typo | A single failure does not establish brute force |
| Encoded PowerShell | PowerShell -EncodedCommand | Normal PowerShell Get-Date | Approved encoded administrative script | Encoding is not inherently malicious |
| Account created | Windows 4720 new account | Windows 4726 deletion | Approved HR onboarding | Confirm whether local/domain and authorized |
| Scheduled task created | Windows 4698 scheduled task | Windows 4699 deletion | Approved backup task | Requires task action and creator context |
| Defender registry change | Sysmon 13 value 1 | Sysmon 13 value 0 | Approved policy test | Registry change does not prove Defender was disabled |

### Isolated test-run observations

The sample harness returned **15/15 expected results**: five suspicious-pattern matches, five benign-context matches, and five nonmatches. This proves only that the narrow matcher behaved as expected on its synthetic fixtures; it is **not proof of Sigma CLI validation or real-world performance**.

### Remaining checks before submission

- [ ] Run the script yourself on Mokka and capture the resulting terminal screenshot
- [ ] Verify the five rules parse with a standard Sigma implementation, if possible
- [ ] Capture rule, sample events, and false-positive discussion screenshots
- [ ] Clearly state that the sample logs are synthetic and there is no production deployment
