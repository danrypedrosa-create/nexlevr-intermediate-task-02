# Alert 02 — SSH Login After Multiple Failures

**Phase:** Independent human investigation (before AI comparison)
**Alert ID:** NEX-INT-002
**Dataset:** Synthetic training alert
**Human verdict:** To Be Confirmed (TBC)
**Human severity:** Medium

## Analyst's revised original assessment

> Verdict: To Be Confirm
> Severity: Medium
>
> Reasoning:
> It's possible that the user was trying to login with an forgotten password account, with too many failed login attempts could trigger an alert. Since the deploy account is used for application deployments only and not existing user could be the cause of this alert triggered but it doesn't prove that there's a user compromised
>
> Recommended Action:
> Check whether the source IP belongs to an approved deployment system and review post-login activity and report to client to confirm if this activity was expected

## Supplied evidence

- 18 failed SSH password attempts against `deploy`, followed by an accepted password and opened session.
- Same source IP: `198.51.100.77`; destination: `192.0.2.35` (`LAB-WEB-02`).
- Source authorization and post-login activity have not been verified.
- Synthetic training data; documentation-only IPs.

## Review notes (not part of the independent assessment)

- TBC is reasonable while authorization is unknown; confirmed login does not itself prove malicious activity.
- Medium severity is a defensible assessment, but an account with deployment access and a success after repeated failures warrants prompt investigation; High may be justified depending on privileges and environment.
- A forgotten password is only one hypothesis, not established by the logs.
- The revised recommended actions appropriately include checking authorized deployment systems, reviewing post-login activity, and seeking client confirmation.

## AI comparison

**AI verdict:** Pending. No AI comparison has been disclosed.
