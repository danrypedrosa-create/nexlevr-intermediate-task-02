# Intermediate Task 03 — SOC Alert Triage

**Status:** Training dataset, model triage notes, comparison and final report prepared. Two independent analyst reviews were recorded; the remaining eight were not independently assessed. Submission approval is pending.

## Objective

Investigate ten simulated SOC alerts, compare independent analyst judgments with AI classifications where possible, and identify unsupported assumptions or overconfidence.

## Files

- [Ten synthetic security alerts](alerts/) — detailed event context and log excerpts
- [Triage notes](analysis/) — independent original analyst assessments for Alerts 01 and 02, plus ten model-generated triage reports
- [Comparison table](COMPARISON.md) — human and AI verdicts with clearly marked unavailable comparisons
- [Final report](FINAL-REPORT.md) — findings, limitations, and recommendations
- [Evidence checklist](evidence/README.md) — how to capture report and case screenshots

## Quick results

| Item | Count |
|---|---|
| Simulated alerts | 10 |
| AI classifications | 10 |
| Independent analyst classifications | 2 |
| Broad verdict agreement among comparable cases | 2 |
| Comparable cases with differing severity | 1 |
| Independent verdicts for Alerts 03–10 | 0 |

This is a **documentation and learning exercise**, not production SOC triage. No measured AI accuracy is claimed. The AI did not independently verify any live IPs, hosts, files, or service activity. The sample alert events are fictional and use documentation-only addresses.

**NEXLEVR requirement note:** A complete ten-case independently written human-vs-AI assessment still needs analyst review if the evaluator requires independent human verdicts for all ten alerts. Do not claim that the AI-generated entries are those human assessments.
