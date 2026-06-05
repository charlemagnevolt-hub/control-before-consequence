from datetime import datetime, timezone

from models import User, ProposedAction, RiskReview, PolicyDecision


def audit_log(
    user: User,
    action: ProposedAction,
    risk_review: RiskReview,
    policy_decision: PolicyDecision,
) -> None:
    """
    Record the security-relevant details of a chatbot interaction.

    In a real system, audit logs should be:
    - timestamped,
    - tamper-resistant,
    - searchable,
    - connected to user identity,
    - connected to document IDs,
    - reviewed by security or compliance teams.

    This prototype prints the audit log to the console.
    """

    timestamp = datetime.now(timezone.utc).isoformat()

    print("\n--- AUDIT LOG ---")
    print(f"Timestamp UTC: {timestamp}")
    print(f"User ID: {user.user_id}")
    print(f"User name: {user.name}")
    print(f"Department: {user.department}")
    print(f"Clearance level: {user.clearance_level}")
    print(f"User roles: {user.roles}")
    print(f"User query: {action.user_query}")
    print(f"Action type: {action.action_type}")
    print(f"Requested documents: {action.requested_documents}")
    print(f"AI risk level: {risk_review.risk_level}")
    print(f"AI concerns: {risk_review.concerns}")
    print(f"AI recommendation: {risk_review.recommendation.value}")
    print(f"Policy decision: {policy_decision.decision.value}")
    print(f"Policy reason: {policy_decision.reason}")
    print(f"Allowed documents: {policy_decision.allowed_documents}")
    print("-----------------")
