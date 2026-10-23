# Alert 02 — SSH Login After Multiple Failures

**Alert ID:** NEX-INT-002  
**Case type:** Synthetic training scenario  
**My verdict:** To Be Confirmed  
**My severity:** Medium  
**Assessment:** My revised independent response

## Reasoning

It's possible that the user was trying to login with an forgotten password account, with too many failed login attempts could trigger an alert. Since the deploy account is used for application deployments only and not existing user could be the cause of this alert triggered but it doesn't prove that there's a user compromised

## Recommended Action

Check whether the source IP belongs to an approved deployment system and review post-login activity and report to client to confirm if this activity was expected

## Evidence limitations

The synthetic logs contain 18 failed SSH password attempts against `deploy` followed by a successful login and session opening. I have not confirmed whether the source IP was authorized or what happened after the login. A forgotten password is a possible explanation, not a verified fact.

## Comparison

The [model assessment](ai-triage-02.md) also selected TBC, but suggested High severity. I selected Medium; I would review the account's permissions, activity and authorization before making the final escalation decision.
