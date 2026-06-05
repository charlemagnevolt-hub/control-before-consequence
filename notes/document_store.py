from models import Document


DOCUMENTS = {
    "DOC-001": Document(
        document_id="DOC-001",
        title="General HR Policy",
        department_owner="HR",
        classification_level=1,
        content="Employees may request annual leave through the HR portal."
    ),
    "DOC-002": Document(
        document_id="DOC-002",
        title="Manufacturing Safety Manual",
        department_owner="Manufacturing",
        classification_level=2,
        content="Factory floor safety rules include protective equipment and incident reporting."
    ),
    "DOC-003": Document(
        document_id="DOC-003",
        title="Confidential Defense Project Archive",
        department_owner="Defense Engineering",
        classification_level=5,
        content="Restricted project information. This content must not be shared outside authorized teams."
    ),
    "DOC-004": Document(
        document_id="DOC-004",
        title="Finance Procurement Records",
        department_owner="Finance",
        classification_level=4,
        content="Confidential procurement records and supplier contract details."
    )
}
