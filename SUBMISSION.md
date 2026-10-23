# NEXLEVR Intermediate — Submission Checklist

## Task 01 — Wazuh SOC Lab
- [x] Fresh Ubuntu Server VM on VirtualBox
- [x] Wazuh Manager, Indexer, Dashboard and Filebeat verified active
- [x] Controlled SSH authentication failures performed
- [x] Six matching Wazuh alerts verified
- [x] Rule 2502 investigation documented
- [x] Eight approved evidence screenshots uploaded under `task-01-wazuh-soc-lab/evidence/`
- [ ] Rotate previously exposed lab credentials
- [ ] Submit to NEXLEVR and await review

## Task 02 — Five Sigma Rules
- [x] Write five Sigma YAML detection rules
- [x] Run limited synthetic matcher against 15 sample events (15/15 expected results)
- [x] Upload three Mokka evidence screenshots to `task-02-sigma-detection-rules/evidence/`
- [x] Document five false-positive risks and matcher limits
- [ ] Official Sigma CLI validation (not confirmed)

## Task 03 — SOC Alert Triage
- [x] Prepare ten synthetic alerts with log excerpts
- [x] Preserve the independent human verdicts for Alerts 01 and 02
- [x] Prepare ten model-generated verdicts, severity ratings and recommended actions
- [x] Document agreements, one severity disagreement, evidence gaps and overconfidence risks
- [x] Write final report and comparison without inventing an accuracy rate
- [ ] Obtain **independent analyst verdicts for Alerts 03–10** if a full human-vs-AI evaluation is required
- [ ] Capture optional evidence screenshots if needed
- [ ] Submit for NEXLEVR review and await approval

**Project documentation is not proof of certification, evaluator approval, live incident handling, or ten independently completed analyst investigations.**
