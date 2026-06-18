from typing import Dict

from models import (
    User,
    Document,
    ProposedAction,
    RiskReview,
    PolicyDecision,
    DecisionType,
)

from redaction import redact_answer


def policy_engine_enforce_rules(
    user: User,
    action: ProposedAction,
    risk_review: RiskReview,
    documents: Dict[str, Document],
) -> PolicyDecision:
    """
    Deterministic rule-based policy engine.

    This module is the hard safety layer of the chatbot system.

    It enforces fixed access-control rules before the chatbot is allowed
    to show any answer to the user.

    Important:
    - AI Agent 1 can propose an answer.
    - AI Agent 2 can review the risk.
    - But this policy engine is the final authority before execution.

    Same input = same output.
    """

    allowed_documents = []

    for doc_id in action.requested_documents:
        document = documents.get(doc_id)

        # Rule 1:
        # Block if the requested document does not exist.
        if document is None:
            return PolicyDecision(
                decision=DecisionType.BLOCK,
                reason=f"Blocked because document {doc_id} does not exist.",
            )

        # Rule 2:
        # A user cannot access documents above their clearance level.
        if document.classification_level > user.clearance_level:
            return PolicyDecision(
                decision=DecisionType.BLOCK,
                reason=(
                    f"Blocked because document {doc_id} has classification level "
                    f"{document.classification_level}, but user clearance is only "
                    f"{user.clearance_level}."
                ),
            )

        # Rule 3:
        # Cross-department access requires a special role.
        if document.department_owner != user.department:
            if "cross_department_reader" not in user.roles:
                return PolicyDecision(
                    decision=DecisionType.REQUIRE_HUMAN_APPROVAL,
                    reason=(
                        f"Document {doc_id} belongs to {document.department_owner}, "
                        f"but user belongs to {user.department}."
                    ),
                    allowed_documents=allowed_documents,
                )

        allowed_documents.append(doc_id)

    # Rule 4:
    # If the AI risk reviewer detected high risk, block the action.
    if risk_review.risk_level == "high":
        return PolicyDecision(
            decision=DecisionType.BLOCK,
            reason="Blocked because the AI risk reviewer detected high leakage risk.",
        )

    # Rule 5:
    # If the AI risk reviewer detected medium risk, allow only a redacted answer.
    if risk_review.risk_level == "medium":
        return PolicyDecision(
            decision=DecisionType.CONSTRAIN,
            reason="Allowed only with constrained answer because medium risk was detected.",
            allowed_documents=allowed_documents,
            constrained_answer=redact_answer(action.intended_answer),
        )

    # Rule 6:
    # If all hard rules pass and the risk is low, allow the action.
    return PolicyDecision(
        decision=DecisionType.ALLOW,
        reason="All hard policy checks passed.",
        allowed_documents=allowed_documents,
    )
