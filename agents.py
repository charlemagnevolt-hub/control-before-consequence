from typing import Dict

from models import (
    User,
    Document,
    ProposedAction,
    RiskReview,
    DecisionType
)


def ai_agent_1_propose_action(user_query: str) -> ProposedAction:
    """
    AI Agent 1 proposes what the chatbot wants to do.

    In a real system, this agent would:
    - understand the user question,
    - retrieve relevant documents,
    - draft an answer,
    - propose the final action before execution.

    Here we simulate a risky proposal.
    """

    return ProposedAction(
        action_type="answer_document_question",
        user_query=user_query,
        requested_documents=["DOC-001", "DOC-003"],
        intended_answer=(
            "According to the HR policy, employees can request annual leave through the HR portal. "
            "The confidential defense archive also contains restricted project information."
        )
    )


def ai_agent_2_review_risk(
    user: User,
    action: ProposedAction,
    documents: Dict[str, Document]
) -> RiskReview:
    """
    AI Agent 2 reviews the proposed action for risk.

    This function represents the second AI-agent layer in the architecture:

    AI Agent 1 proposes action
        ↓
    AI Agent 2 reviews risk
        ↓
    Rule-based policy engine enforces hard constraints
        ↓
    Human approval if needed
        ↓
    Executor runs approved action

    Important:
    This function does not make the final authorization decision.
    It only identifies possible risk and gives a recommendation.

    The final authority belongs to the deterministic policy engine.
    """

    concerns = []
    highest_risk = "low"

    for doc_id in action.requested_documents:
        document = documents.get(doc_id)

        if document is None:
            concerns.append(
                f"Requested document {doc_id} does not exist."
            )

            if highest_risk == "low":
                highest_risk = "medium"

            continue

        # Risk 1:
        # The requested document requires a higher clearance level
        # than the user has.
        if document.classification_level > user.clearance_level:
            concerns.append(
                f"User clearance level is too low for document {doc_id}."
            )
            highest_risk = "high"

        # Risk 2:
        # The document belongs to another department.
        if document.department_owner != user.department:
            concerns.append(
                f"Document {doc_id} belongs to another department: "
                f"{document.department_owner}."
            )

            if highest_risk != "high":
                highest_risk = "medium"

        # Risk 3:
        # The answer may reveal the existence or title of a document
        # the user should not know about.
        if document.title.lower() in action.intended_answer.lower():
            concerns.append(
                f"Answer may reveal the title or existence of restricted "
                f"document {doc_id}."
            )

            if highest_risk != "high":
                highest_risk = "medium"

        # Risk 4:
        # The answer may include sensitive terms from restricted content.
        sensitive_terms = [
            "confidential",
            "restricted",
            "defense archive",
            "project information",
            "supplier contract",
            "procurement records"
        ]

        intended_answer_lower = action.intended_answer.lower()

        for term in sensitive_terms:
            if term in intended_answer_lower:
                concerns.append(
                    f"Answer may contain sensitive term: '{term}'."
                )

                if highest_risk != "high":
                    highest_risk = "medium"

    if highest_risk == "high":
        recommendation = DecisionType.BLOCK
    elif highest_risk == "medium":
        recommendation = DecisionType.CONSTRAIN
    else:
        recommendation = DecisionType.ALLOW

    return RiskReview(
        risk_level=highest_risk,
        concerns=concerns,
        recommendation=recommendation
    )
