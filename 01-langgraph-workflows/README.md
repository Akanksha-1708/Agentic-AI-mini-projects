# 01 — LangGraph Workflows

A learning lab for understanding the fundamentals of **LangGraph and agentic workflows**.

The goal of this project is to understand how state, nodes, edges, routing, parallel execution, and iteration work together to create agentic workflows.

## Concepts Covered

* Agentic AI fundamentals
* LangChain vs LangGraph
* State
* Nodes
* Edges
* Graphs
* Sequential workflows
* Parallel workflows
* Conditional workflows
* Iterative workflows

## Project Structure

```text
01-langgraph-workflows/
│
├── README.md
├── requirements.txt
│
├── 01_graph_and_state.py
├── 03_sequential_workflow.py
├── 04_parallel_workflow.py
├── 05_conditional_workflow.py
├── 06_iterative_workflow.py
│
└── .env
```

## Workflow Patterns

### 1. Basic Graph

```text
START → Node → END
```

Introduces the basic LangGraph architecture.

### 2. State

Shows how information is passed from one node to another.

```text
State → Node → Updated State → Node
```

### 3. Sequential Workflow

```text
A → B → C → D
```

Used when each step depends on the previous step.

### 4. Parallel Workflow

```text
        ┌→ B ─┐
A ──────┤     ├→ D
        └→ C ─┘
```

Used when independent tasks can be executed as separate branches.

### 5. Conditional Workflow

```text
        ┌→ B
A ──────┤
        └→ C
```

The next node is selected based on the current state.

### 6. Iterative Workflow

```text
A → B → C
    ↑   │
    └───┘
```

The workflow can repeat until a condition is satisfied.

## Core Mental Model

```text
State
  ↓
Nodes
  ↓
Edges
  ↓
Graph
  ↓
Workflow
```

In LangGraph:

* **State** = information shared throughout the workflow
* **Node** = function that performs work
* **Edge** = connection between nodes
* **Conditional edge** = decides which node runs next
* **Graph** = complete workflow
* **Compile** = converts the graph definition into an executable graph
* **Invoke** = runs the graph with an initial state

## Learning Goal

The purpose of this project is not to build a production application.

It is a **learning lab** designed to develop the mental model required to build more advanced agentic AI systems later.
