def redact_answer(answer: str) -> str:
    """
    Redact restricted terms from a chatbot answer.

    This is a simple prototype redaction layer.

    In a real secure document chatbot, redaction would need to be much stronger.
    It should likely use:
    - document-level access labels,
    - paragraph-level permissions,
    - classification metadata,
    - sensitive entity detection,
    - citation filtering,
    - source-aware answer generation,
    - audit logging for redacted content.
    """

    restricted_terms = [
        "confidential defense archive",
        "restricted project information",
        "supplier contract details",
        "Confidential Defense Project Archive",
        "Finance Procurement Records",
        "Defense Engineering",
    ]

    redacted_answer = answer

    for term in restricted_terms:
        redacted_answer = redacted_answer.replace(term, "[REDACTED]")

    return redacted_answer
