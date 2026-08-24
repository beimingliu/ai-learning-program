# AI Learning Program Glossary

Canonical authoring language for Foundations 101 and the two 201 courses. In this program, the terms below have the specific meanings given here.

## Terms

**Access**:
The information, files, tools, and systems an agent can potentially reach.
_Avoid_: Safety, permission

**Agent**:
A system in which a model can use tools and iterate toward a goal.
_Avoid_: Bot, oracle

**Agentic loop**:
Gather context, act, observe, verify, then repeat or stop.
_Avoid_: Autonomous magic

**Artifact**:
A durable output that a human or future agent can inspect, review, or reuse.
_Avoid_: Answer, response

**Context**:
Information active for the model's current reasoning step.
_Avoid_: Everything the agent knows

**Correctness**:
The degree to which an output is accurate and fit for its intended use.
_Avoid_: Safety

**Evaluation**:
A systematic test of whether a workflow succeeds across representative tasks and repeated trials.
_Avoid_: One spot check

**Evidence**:
Information that independently connects a claim or output to a trusted source, test, or observable result.
_Avoid_: Confidence, polish

**Governance**:
Policy, access control, audit, and human ownership for consequential work.
_Avoid_: Prompt instruction

**Harness**:
The surrounding system that gives a model tools, execution, permissions, context management, and a control loop.
_Avoid_: Model

**Human decision owner**:
The person accountable for a judgment or consequential action, even when AI contributes analysis or a recommendation.
_Avoid_: Reviewer of record

**MCP (Model Context Protocol)**:
A standard way for an external system to expose selected tools or resources to an AI client.
_Avoid_: Universal access

**Memory**:
Information intentionally persisted for future sessions or tasks.
_Avoid_: Current context

**Model**:
The reasoning and generation component inside an AI system.
_Avoid_: Agent, tool

**Permission**:
A control determining which actions can occur without approval.
_Avoid_: Access, correctness

**Recovery**:
The ability to interrupt an action or restore a prior state.
_Avoid_: Universal undo

**State**:
Information or conditions outside the current conversation, such as files, databases, applications, tickets, or deployed services.
_Avoid_: Context

**Tool**:
An ability an agent can call to retrieve, calculate, edit, execute, or interact with an external system.
_Avoid_: Model

**Verification**:
Checking an output against independent evidence before using it.
_Avoid_: The agent says it checked

**Workspace**:
The bounded project, folder, or environment from which an agent can potentially access material.
_Avoid_: Context window
