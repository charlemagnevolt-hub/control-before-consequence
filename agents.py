from models import ProposedAction


def ai_agent_1_propose_action(user_query: str) -> ProposedAction:
    """
    AI Agent 1 proposes what the chatbot wants to do.
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
