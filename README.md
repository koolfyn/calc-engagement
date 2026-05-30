# Calc Engagement MVP

## Overview

This project was developed as part of **Track 2: Learning Actions** within the Capillary Actions ecosystem.

The long-term research question driving this work is:

> How can we flatten the outcome curve for students with varying learning needs while maintaining the same quality of content and instruction?

To explore this question, I built a proof-of-concept adaptive tutoring system focused on **AP Calculus BC**. The system combines a domain knowledge graph, learner memory, prompt augmentation, model routing, and LLM generation to create personalized learning engagements based on where a student is in the curriculum and how they have interacted with previous lessons.

Rather than acting as a generic chatbot, the goal is to move toward a system that can determine:

* What the learner already knows
* Where the learner is struggling
* What concept should be taught next
* How that concept should be presented to the learner

The current implementation validates these ideas against the Capillary SDK architecture while providing a working end-to-end tutoring workflow.

---

## Educational Motivation

Many AI tutoring systems focus primarily on generating answers.

This project explores a different approach:

* The curriculum itself should be structured.
* Learner progress should be tracked over time.
* Student interactions should leave "breadcrumbs" that influence future instruction.
* Different learners may benefit from different teaching approaches while still covering the same core material.

For the MVP, AP Calculus BC was chosen as a high-demand subject with a well-defined prerequisite structure that naturally lends itself to knowledge graph modeling.

---

## Current Architecture

The current workflow is:

Student Input

↓

Teaching Context Assembly

↓

Prompt Augmentation

↓

Model Routing

↓

OpenRouter Generation

↓

Outcome Recording

↓

Updated Learner State

The system currently combines two major forms of knowledge:

### Domain Knowledge Graph

Represents the curriculum itself.

Examples include:

* Limits
* Derivatives
* Integrals
* Prerequisite relationships between concepts

The graph provides structure for determining what can be taught and what concepts depend on one another.

### Learner Model / Memory

Represents the individual learner.

Examples include:

* Mastery scores
* Completed concepts
* Previous confusion points
* Recommended instructional approach

Together, these components determine the next learning engagement presented to the student.

---

## Capillary SDK Integration

This project validates the **Learner Interaction** track of the Capillary Actions SDK.

Implemented concepts include:

* KnowledgeGraph
* KnowledgeConcept
* LearnerProgress
* TeachingContext

The MVP uses Capillary's domain models and ports to structure educational data while OpenRouter serves as the generation layer.

In practice:

* Capillary provides the educational domain structure.
* OpenRouter provides LLM execution.
* Prompt augmentation connects the two.

This separation allows teaching logic to remain independent from any specific model provider.

---

## What This MVP Demonstrates

The current proof-of-concept successfully demonstrates:

* Knowledge graph driven curriculum structure
* Learner progress tracking
* Teaching context assembly
* Prompt augmentation
* OpenRouter integration
* Model routing based on instructional needs
* Personalized tutoring responses

Example learner context may include:

* Current concept: Integrals
* Mastery of prerequisite concepts
* Previous confusion with the Power Rule
* Recommended teaching style: Conceptual

The generated response is then tailored using that context rather than relying solely on the student's raw message.

---

## Repository Structure

```text
main.py
├── adapters/
│   ├── knowledge_graph_adapter.py
│   ├── learner_progress_adapter.py
│   └── teaching_adapter.py
│
├── prompts/
│   └── prompt_builder.py
│
├── routing/
│   └── model_router.py
│
├── retrieval/
│   └── retriever.py
│
└── llm/
    └── openrouter_client.py
```

---

## Running The Demo

Create a local `.env` file:

```env
OPENROUTER_API_KEY=your_key_here
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

The system will:

1. Build a learner teaching context
2. Assemble an augmented prompt
3. Select a model
4. Generate a tutoring response through OpenRouter

---

## Current Limitations

This repository intentionally prioritizes architecture validation over production readiness.

Currently:

* Learner data is hard-coded
* Retrieval is a placeholder
* RAG is not fully implemented
* Knowledge graphs are manually defined
* Routine definition and execution are tightly coupled
* Validation tools are not yet implemented

These limitations are deliberate and help expose the next architectural steps.

---

## Next Steps

The most important next step is separating the educational routine from the agent that executes it.

Today:

```text
Routine
+
Prompt Logic
+
Routing
+
Execution
```

all live inside a single repository.

The intended direction is:

```text
Routine Definition (YAML)

↓

Agent Runtime

↓

Tools

↓

Execution
```

In this model:

* A routine defines what should happen.
* An agent determines how to execute it.
* Modular tools perform specialized tasks.

This would allow the same tutoring workflow to be executed by different agents while maintaining identical educational behavior.

It also enables more reliable educational tooling, such as:

* Homework validation
* Concept mastery checks
* Rubric-based grading
* Prerequisite verification

without relying on the LLM to guess.

---

## Research Direction

This MVP is not the final product.

It is an architectural experiment exploring how learner memory, knowledge graphs, educational standards, retrieval, and AI generation can work together to create adaptive learning experiences that scale to students with different backgrounds, learning preferences, and instructional needs.
