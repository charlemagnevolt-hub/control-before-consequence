from models import ProposedAction, PolicyDecision, DecisionType


def executor_run(
    action: ProposedAction,
    decision: PolicyDecision,
) -> None:
    """
    Execute only approved or constrained chatbot actions.

    The executor is the final stage of the runtime pipeline.

    Important:
    - It must never trust Agent 1 directly.
    - It must only use the decision returned by the policy layer.
    - It must not display blocked content.
    """

    if decision.decision == DecisionType.ALLOW:
        print("\nChatbot response:")
        print(action.intended_answer)
        return

    if decision.decision == DecisionType.CONSTRAIN:
        print("\nChatbot response:")
        print(decision.constrained_answer)
        return

    print("\nChatbot response:")
    print("Sorry, I cannot provide that information because it is restricted.")
