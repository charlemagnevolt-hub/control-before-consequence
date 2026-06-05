from models import User, ProposedAction, PolicyDecision


def request_human_approval(
    user: User,
    action: ProposedAction,
    decision: PolicyDecision,
) -> bool:
    """
    Simulate a human approval step.

    In a real system, this function could send the request to:
    - a security officer,
    - a department manager,
    - a compliance reviewer,
    - the owner of the requested document,
    - a ticketing or approval workflow system.

    This prototype denies approval by default so restricted information is
    not accidentally shown during the demo.
    """

    print("\nHuman approval required.")
    print(f"User: {user.name}")
    print(f"User ID: {user.user_id}")
    print(f"Department: {user.department}")
    print(f"Clearance level: {user.clearance_level}")
    print(f"Reason: {decision.reason}")
    print(f"Requested documents: {action.requested_documents}")

    return False
