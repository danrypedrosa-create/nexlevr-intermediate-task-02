# Alert 02 — SSH Login After Multiple Failures

**Phase:** Independent human investigation (before AI comparison)
**Alert ID:** NEX-INT-002
**Dataset:** Synthetic training alert
**Human verdict:** To Be Confirmed (TBC)
**Human severity:** Medium

## Analyst's original submission

> Alert 02 — SSH Login After Multiple Failures
>
> Verdict: To Be Confirmed
> Severity: Medium
>
> Reasoning:
> Alert 02: Successful SSH Login After Multiple Failed Attempts.
>
> Verdict: To Be Confirm
> Severity: Medium
>
> Reasoning:
> It's possible that the user was trying to login with his forgotten password account, with too many failed login attempts could trigger an alert. Since the deploy account is used for application deployments only and not existing user could be the cause of this alert triggered but it doesn't prove that there's a user compromised
>
> Recommended Action:
> Report to client to confirm if this activity was expected

## Provided evidence

- 18 failed SSH password attempts for `deploy`, followed by one accepted password and opened session.
- Same source IP: `198.51.100.77`; destination: `192.0.2.35` (`LAB-WEB-02`).
- The source IP has not been verified against authorized administrators or automation.
- No post-login command or process evidence was provided.
- These are synthetic training events and documentation-only IPs.

## Feedback, kept separate from the original verdict

- TBC is defensible while authorization remains unverified.
- The analyst revised severity from Low to Medium before AI comparison. A successful login after 18 failed attempts still warrants prompt investigation; High may be appropriate depending on asset criticality and authorization.
- Forgotten password is a hypothesis, not an established fact.
- Check authorized source IPs, deployment schedule, account owner, and post-login activity; escalate if unauthorized.

## Revision history

- Original submission: TBC / Low.
- Analyst revised the severity to **Medium** before AI comparison, leaving the reasoning and recommended action unchanged. The revised assessment is the one to use in the later comparison.

## AI comparison

**AI verdict:** Pending. The original human verdict remains unchanged.
