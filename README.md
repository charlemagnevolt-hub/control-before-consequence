# Control Before Consequence: Secure Document Chatbot Prototype

This project is a small Python prototype that demonstrates a **runtime admissibility control layer** for an AI-powered internal document chatbot.

The main idea is simple:

> An AI agent should not be allowed to directly execute or reveal information just because it generated an answer.  
> Every proposed action must be reviewed, checked against rules, logged, and only then executed if it is allowed.

This project uses a defense-industry document chatbot scenario to show how confidential information can be blocked before it appears in a chat response.

---

## Scenario

Imagine a defense-industry manufacturer with many internal departments, such as:

- HR
- Manufacturing
- Finance
- Defense Engineering

Employees can chat with an AI assistant to ask questions about internal documentation and archives.

However, the organization’s documents are classified by:

- department ownership
- clearance level
- access roles

For example, an HR employee may be allowed to access general HR policy documents, but not confidential Defense Engineering archives.

The chatbot must therefore prevent confidential information from being leaked through:

- direct answers
- summaries
- document titles
- archive references
- cross-department content
- restricted project information

Once confidential information appears in the chat, the damage has already happened. This project demonstrates how to block or constrain that response **before execution**.

---

## Core Architecture

The project follows this runtime flow:

```text
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
```

The important principle is:

> AI Agent 1 can propose an answer, but it cannot directly show the answer to the user.  
> The executor only displays the final response after the policy layer has approved or constrained it.

---

## Why This Matters

Many AI systems focus on checking prompts or model outputs. That is useful, but it is not enough for agentic systems.

A chatbot connected to internal documentation can accidentally leak restricted information even when the user asked a normal question.

For example:

```text
User:
Can you summarize the HR leave policy and any related defense project archive notes?
```

The AI may retrieve both:

```text
DOC-001: General HR Policy
DOC-003: Confidential Defense Project Archive
```

If the user is an HR employee with low clearance, the system must block the restricted document before the answer is shown.

This prototype demonstrates that control point.

---

## Project Structure

```text
control-before-consequence/
├── main.py
├── models.py
├── document_store.py
├── agents.py
├── policy_engine.py
├── redaction.py
├── human_approval.py
├── executor.py
├── audit.py
└── README.md
```

---

## Module Overview

### `main.py`

The starting point of the project.

Run it with:

```bash
python main.py
```

It connects the whole runtime pipeline:

1. Agent 1 proposes a chatbot action
2. Agent 2 reviews risk
3. Policy engine enforces access rules
4. Human approval is requested if needed
5. Audit log records the decision
6. Executor displays only the approved or safe response

---

### `models.py`

Defines the shared data structures used across the project.

Important models include:

- `User`
- `Document`
- `ProposedAction`
- `RiskReview`
- `PolicyDecision`
- `DecisionType`

These models make the pipeline structured and predictable.

---

### `document_store.py`

Contains a mock classified document archive.

Each document includes:

- document ID
- title
- department owner
- classification level
- content

Example:

```text
DOC-003
Title: Confidential Defense Project Archive
Owner: Defense Engineering
Classification level: 5
```

This file simulates the organization’s internal document archive.

---

### `agents.py`

Contains two simulated AI-agent functions.

#### AI Agent 1

```python
ai_agent_1_propose_action()
```

This simulates the normal chatbot behavior:

- receives a user question
- selects documents
- drafts an intended answer
- proposes an action

It does **not** execute the action.

#### AI Agent 2

```python
ai_agent_2_review_risk()
```

This simulates a second AI agent that reviews the proposed action for risk.

It checks for issues such as:

- low clearance
- cross-department document access
- sensitive terms in the intended answer
- possible leakage of restricted information

Agent 2 gives a recommendation, but it is **not the final authority**.

---

### `policy_engine.py`

The deterministic rule-based control layer.

This is the most important safety component.

It enforces hard rules such as:

- block documents above the user’s clearance level
- require approval for cross-department access
- block high-risk actions
- constrain medium-risk actions
- allow only safe actions

Unlike an AI agent, the policy engine should be deterministic:

```text
Same input = same output
```

This means the final authorization decision does not depend only on AI judgment.

---

### `redaction.py`

Contains the redaction layer for constrained responses.

If an answer is medium-risk but not fully blocked, restricted terms can be replaced with:

```text
[REDACTED]
```

This is a simple prototype redaction layer. A production system would need a much stronger approach using document-level and paragraph-level access controls.

---

### `human_approval.py`

Simulates a human approval process.

Some cases may not be safe to automatically allow or block. For example:

- cross-department access
- unusual access patterns
- requests involving sensitive archives
- ambiguous user permissions

In this prototype, human approval is denied by default for safety.

---

### `audit.py`

Prints an audit log for each chatbot interaction.

The audit log records:

- timestamp
- user ID
- user department
- clearance level
- roles
- user query
- requested documents
- AI risk review
- policy decision
- policy reason

In a real system, this should be written to a secure, tamper-resistant logging system.

---

### `executor.py`

The final execution layer.

The executor is the only module allowed to display the final chatbot response.

It follows the policy decision:

| Decision    | Executor behavior                     |
| ----------- | ------------------------------------- |
| `ALLOW`     | Shows the original answer             |
| `CONSTRAIN` | Shows the constrained/redacted answer |
| `BLOCK`     | Shows a safe refusal message          |

The executor must never trust Agent 1 directly.

---

## How to Run

From the project root:

```bash
python main.py
```

Or, if your system uses `python3`:

```bash
python3 main.py
```

---

## Example Output

A sample run may look like this:

```text
User question: Can you summarize the HR leave policy and any related defense project archive notes?

Policy decision:
block
Blocked because document DOC-003 has classification level 5, but user clearance is only 1.

--- AUDIT LOG ---
Timestamp UTC: 2026-06-05T17:02:18.138402+00:00
User ID: U-1007
User name: Sara
Department: HR
Clearance level: 1
User roles: ['employee']
User query: Can you summarize the HR leave policy and any related defense project archive notes?
Action type: answer_document_question
Requested documents: ['DOC-001', 'DOC-003']
AI risk level: high
AI concerns: [...]
AI recommendation: block
Policy decision: block
Policy reason: Blocked because document DOC-003 has classification level 5, but user clearance is only 1.
Allowed documents: None
-----------------

Chatbot response:
Sorry, I cannot provide that information because it is restricted.
```

This shows that the system blocked confidential information before it was displayed.

---

## Runtime Decision Types

The project uses four decision types:

| Decision                 | Meaning                                                     |
| ------------------------ | ----------------------------------------------------------- |
| `ALLOW`                  | The action is safe and can be executed                      |
| `CONSTRAIN`              | The action may continue only with restrictions or redaction |
| `BLOCK`                  | The action must not be executed                             |
| `REQUIRE_HUMAN_APPROVAL` | The action must be reviewed by a human before execution     |

---

## Example Security Flow

### User

```text
Sara
Department: HR
Clearance level: 1
Roles: employee
```

### Requested documents

```text
DOC-001: General HR Policy
DOC-003: Confidential Defense Project Archive
```

### Policy result

```text
DOC-001 is allowed.
DOC-003 is blocked because it requires clearance level 5.
```

### Final chatbot response

```text
Sorry, I cannot provide that information because it is restricted.
```

---

## Design Principle

The project is based on this principle:

> Control should happen before consequence.

In other words:

```text
Do not wait until after the AI leaks information.
Do not rely only on logs after the fact.
Do not let the model be the final authority.
Check the action before it happens.
```

---

## What This Prototype Demonstrates

This project demonstrates:

- separating proposal from execution
- using one AI agent to propose an action
- using another AI agent to review risk
- enforcing hard rules through deterministic code
- escalating uncertain cases to human approval
- logging security-relevant decisions
- preventing restricted information from appearing in chat

---

## What This Prototype Does Not Do

This is not a production-grade security system.

It does not include:

- real authentication
- real authorization provider integration
- real document database
- encrypted storage
- secure logging backend
- real LLM calls
- real retrieval-augmented generation
- paragraph-level access control
- full data loss prevention
- production-grade redaction
- adversarial prompt-injection defense
- SOC or SIEM integration

It is a conceptual and educational prototype.

---

## Production Considerations

A real implementation would need stronger controls, such as:

- identity and access management integration
- document-level and section-level permissions
- clearance verification
- department ownership checks
- secure retrieval filtering before generation
- prompt-injection detection
- output filtering
- citation-level access control
- tamper-resistant audit logs
- approval workflows
- monitoring and alerting
- strict tool-call permissions
- least-privilege agent identities

The policy engine should be connected to trusted enterprise systems, not hardcoded demo data.

---

## Possible Future Improvements

Potential next steps:

- add tests for the policy engine
- add command-line user selection
- add multiple example users
- simulate approval granted and denied cases
- add structured JSON audit logs
- add document search simulation
- add safer source-aware response generation
- separate document retrieval from answer generation
- add a real policy configuration file
- add a small web interface
- integrate with a real LLM provider

---

## Suggested GitHub Issues

The project can be developed issue by issue:

1. Add shared data models
2. Add mock classified document store
3. Implement AI Agent 1 for proposed chatbot actions
4. Implement AI Agent 2 risk review layer
5. Implement deterministic policy engine
6. Add redaction layer
7. Add human approval simulation
8. Add executor for approved chatbot actions
9. Add audit logging
10. Add `main.py` entry point
11. Add project documentation

---

## Summary

This project shows how a chatbot can be made safer by placing a control layer between AI-generated actions and real execution.

The key message is:

> The AI agent may suggest what to do, but the system must decide whether it is allowed.

That is the essence of **control before consequence**.
