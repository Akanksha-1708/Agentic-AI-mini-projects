from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated

from langchain_core.messages import BaseMessage, HumanMessage
from langchain_mistralai import ChatMistralAI

from dotenv import load_dotenv
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver

load_dotenv()

# LLM
llm = ChatMistralAI(model="ministral-3b-latest", streaming=True)


# State
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


# Create graph
graph = StateGraph(ChatState)


# Chatbot node
def chat_node(state: ChatState):

    # Take messages from state
    messages = state["messages"]

    # Send messages to LLM
    response = llm.invoke(messages)

    # Return response
    return {
        "messages": [response]
    }


# Add node
graph.add_node("chat_node", chat_node)

# Add edges
graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)


# Memory
memory = MemorySaver()

# Compile graph with memory
chatbot = graph.compile(checkpointer=memory)

