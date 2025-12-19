from dotenv import load_dotenv
from typing_extensions import TypedDict
from typing import Annotated, List
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model

load_dotenv()

llm = init_chat_model(
    model="gpt-4.1-mini",
    model_provider="openai"
)

class State(TypedDict):
    messages: Annotated[list, add_messages]
    
def chatbot(state: State):
    response = llm.invoke(state.get("messages"))
    return { "messages": [response] }
    
def sample_node(state: State):
    print("\n\nInside sample_node node", state)
    return { "messages": ["Sample Message Appended"]}
    
graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("sample_node", sample_node)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", "sample_node")
graph_builder.add_edge("sample_node", END)

graph = graph_builder.compile()

updated_state = graph.invoke(State({ "messages": ["Hi, my name is Henry"]}))
print("\n\nupdated_state", updated_state)

# (START) -> chatbot -> sample_node -> (END)

# state = { messages: ["Hey there"] }
# node runs: chatbot(state: ["Hey There"]) -> ["Hi, This is a message from ChatBot Node"])
# state = { messages: ["Hey there", "Hi, This is a message from ChatBot Node"] }
