from models import User, DecisionType, PolicyDecision
from document_store import DOCUMENTS
from agents import ai_agent_1_propose_action, ai_agent_2_review_risk
from policy_engine import policy_engine_enforce_rules
from human_approval import request_human_approval
from executor import executor_run
from audit import audit_log


def secure_document_chatbot(user: User, user_query: str) -> None:
    """
    Complete runtime pipeline:

    AI Agent 1 proposes action
        ↓
    AI Agent 2 reviews risk
        ↓
    Rule-based policy engine enforces hard constraints
        ↓
    Human approval if needed
        ↓
    Audit log records decision
        ↓
    Executor runs approved action
    """

    print(f"\nUser question: {user_query}")

    # Step 1: AI Agent 1 proposes an action.
    proposed_action = ai_agent_1_propose_action(user_query)

    # Step 2: AI Agent 2 reviews risk.
    risk_review = ai_agent_2_review_risk(
        user=user,
        action=proposed_action,
        documents=DOCUMENTS,
    )

    # Step 3: deterministic policy engine enforces hard rules.
    policy_decision = policy_engine_enforce_rules(
        user=user,
        action=proposed_action,
        risk_review=risk_review,
        documents=DOCUMENTS,
    )

    # Step 4: human approval if policy requires it.
    if policy_decision.decision == DecisionType.REQUIRE_HUMAN_APPROVAL:
        approved = request_human_approval(
            user=user,
            action=proposed_action,
            decision=policy_decision,
        )

        if approved:
            policy_decision = PolicyDecision(
                decision=DecisionType.ALLOW,
                reason="Human approver allowed the action.",
                allowed_documents=policy_decision.allowed_documents,
            )
        else:
            policy_decision = PolicyDecision(
                decision=DecisionType.BLOCK,
                reason="Human approver rejected the action.",
            )

    print("\nPolicy decision:")
    print(policy_decision.decision.value)
    print(policy_decision.reason)

    # Step 5:
    # Record the interaction before showing the final response.
    audit_log(
        user=user,
        action=proposed_action,
        risk_review=risk_review,
        policy_decision=policy_decision,
    )

    # Step 6:
    # The executor is the only place where the final chatbot response is shown.
    executor_run(
        action=proposed_action,
        decision=policy_decision,
    )


if __name__ == "__main__":
    employee = User(
        user_id="U-1007",
        name="Sara",
        department="HR",
        clearance_level=1,
        roles=["employee"],
    )

    secure_document_chatbot(
        user=employee,
        user_query="Can you summarize the HR leave policy and any related defense project archive notes?",
    )
