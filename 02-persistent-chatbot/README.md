
# 🤖 Persistent Streaming Chatbot using LangGraph

A conversational AI chatbot built using **LangGraph, LangChain, Mistral AI, and Streamlit**.

This project demonstrates how to build a chatbot with conversation memory using LangGraph's checkpointer and stream AI-generated responses progressively through a Streamlit interface.

The project is part of my learning journey in **Generative AI and Agentic AI development**.

## 🚀 Features

- 💬 **Conversational AI:** Interact with a Mistral-powered chatbot.
- 🧠 **Conversation Memory:** Uses LangGraph's `MemorySaver` to maintain conversation state.
- 🧵 **Thread-Based Conversations:** Uses a `thread_id` to associate messages with a conversation.
- ⚡ **Streaming Responses:** Streams AI message chunks and displays the response progressively.
- 🔗 **LangGraph Workflow:** Uses state, nodes, and edges to build the chatbot execution flow.
- 🎨 **Streamlit Interface:** Provides an interactive chat UI.
- 🐍 **Python-Based Implementation:** Uses LangChain's message abstractions and Python.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangGraph | Building the chatbot workflow and managing state |
| LangChain Core | Message types and message handling |
| Mistral AI | Large language model |
| Streamlit | Interactive chatbot frontend |
| python-dotenv | Loading environment variables |

## 📁 Project Structure

```text
02-persistent-chatbot/
│
├── backend.py          # LangGraph workflow and memory
├── frontend.py         # Streamlit chatbot interface
└── README.md           # Project documentation
```

## 🧠 How the Chatbot Works

The chatbot is divided into two main components:

### 1. Backend (`backend.py`)

The backend is responsible for creating and compiling the LangGraph workflow.

It contains:

- **ChatState:** Defines the state of the chatbot.
- **Messages:** Stores conversation messages.
- **Chat Node:** Sends messages to the Mistral AI model.
- **Graph Edges:** Define the execution flow.
- **MemorySaver:** Stores conversation checkpoints in memory.
- **Thread ID:** Identifies a conversation thread.

### 2. Frontend (`frontend.py`)

The frontend is built using Streamlit.

It:

1. Accepts user input through `st.chat_input()`.
2. Sends the user message to the LangGraph chatbot.
3. Receives streamed message chunks.
4. Accumulates the chunks into a complete response.
5. Updates the response progressively using `st.empty()`.
6. Stores the conversation in Streamlit session state.

## 🔄 LangGraph Workflow

```text
START
  │
  ▼
Chat Node
  │
  ▼
Mistral AI Model
  │
  ▼
END
```

The chat node receives the current message state, invokes the language model, and returns the AI response as a state update.

## 🧩 Backend Implementation

The chatbot state is defined using `TypedDict`:

```python
class ChatState(TypedDict):
    messages: Annotated[
        list[BaseMessage],
        add_messages
    ]
```

The `add_messages` reducer manages how messages are added to the state.

The graph is compiled with a checkpointer:

```python
memory = MemorySaver()

chatbot = graph.compile(
    checkpointer=memory
)
```

## 🧠 Conversation Memory

The chatbot uses LangGraph's `MemorySaver` to store conversation checkpoints.

A thread ID is passed through the configuration:

```python
CONFIG = {
    "configurable": {
        "thread_id": "thread_1"
    }
}
```

The thread ID allows LangGraph to associate messages with the same conversation thread.

### Memory Limitation

This project uses `MemorySaver`, which stores checkpoints in application memory.

It is suitable for learning and experimentation but does not provide durable database-backed storage across application restarts.

## ⚡ Streaming Implementation

The frontend uses LangGraph's streaming interface:

```python
for chunk in chatbot.stream(
    {
        "messages": [
            HumanMessage(content=user_input)
        ]
    },
    config=CONFIG,
    stream_mode="messages"
):
    message, metadata = chunk
```

The streamed message content is extracted and accumulated:

```python
full_response += token
```

The Streamlit placeholder is updated progressively:

```python
message_placeholder.markdown(
    full_response + "▌"
)
```

After the stream finishes, the final response is displayed without the cursor:

```python
message_placeholder.markdown(full_response)
```

### Streaming Process

```text
User Input
    │
    ▼
chatbot.stream()
    │
    ▼
LangGraph Workflow
    │
    ▼
Mistral AI Response Chunks
    │
    ▼
Accumulate Chunks
    │
    ▼
Update Streamlit Placeholder
    │
    ▼
Display Complete Response
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Akanksha-1708/Agentic-AI-mini-projects.git
```

Navigate to the project:

```bash
cd Agentic-AI-mini-projects
cd 02-persistent-chatbot
```

### 2. Activate the Virtual Environment

If you already have a virtual environment in the parent directory, activate it from the repository root or use the appropriate path for your environment.

For a virtual environment located in the repository root:

```bash
..\.venv\Scripts\activate
```

### 3. Install Dependencies

Install the required packages:

```bash
pip install streamlit langgraph langchain-core langchain-mistralai python-dotenv
```

### 4. Configure Environment Variables

Create a `.env` file in the appropriate project or repository directory:

```env
MISTRAL_API_KEY=your_mistral_api_key
```

Never expose your API key or commit your `.env` file to GitHub.

Add the following to `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

### 5. Run the Chatbot

From the `02-persistent-chatbot` directory, run:

```bash
python -m streamlit run frontend.py
```

The Streamlit application will open in your browser.

## 🧪 Testing

The chatbot can be tested through the Streamlit interface.

Example prompts:

```text
What is LangGraph?
```

```text
Explain the difference between LangChain and LangGraph.
```

```text
What did I ask you in my previous message?
```

The final prompt can be used to explore conversation context maintained by the configured thread during the application's lifetime.

## 📚 Concepts Learned

Through this project, I practiced:

- [x] Defining state using `TypedDict`.
- [x] Using `Annotated` and the `add_messages` reducer.
- [x] Creating LangGraph nodes and edges.
- [x] Compiling a graph with `MemorySaver`.
- [x] Using `thread_id` for conversation state.
- [x] Integrating Mistral AI with LangChain.
- [x] Using `chatbot.invoke()` for complete graph responses.
- [x] Using `chatbot.stream()` for streamed responses.
- [x] Processing streamed message chunks.
- [x] Accumulating response tokens.
- [x] Building a Streamlit chatbot interface.
- [x] Managing frontend messages with `st.session_state`.


## 👩‍💻 Author

**Akanksha Dwivedi**

Computer Science Engineering Student

Interested in:
- Artificial Intelligence
- Machine Learning
- Generative AI
- Agentic AI
- AI Engineering

---

⭐ This project is part of my journey toward building practical Generative AI and Agentic AI applications.