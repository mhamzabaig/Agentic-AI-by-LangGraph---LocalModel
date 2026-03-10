import os 
from typing import  TypedDict, Union, List
from langchain_core.messages import HumanMessage, AIMessage
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START,END

class AgentState(TypedDict):
    messages:List[Union[HumanMessage,AIMessage]]

llm = ChatOllama(model="llama3.1:8b")

def process(state:AgentState) -> AgentState:
    """This node will solve the request you input"""
    response = llm.invoke(state["messages"])
    state["messages"].append(AIMessage(content=response.content))

    print(f"\nAI: {response.content}")
    print(state["messages"])
    return state


graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START,"process")
graph.add_edge("process", END)
agent = graph.compile()

convo_history = []

user_input = input("Enter: ")
while user_input != "exit":
    convo_history.append(HumanMessage(content=user_input))
    result = agent.invoke({"messages": convo_history})
    convo_history = result["messages"]
    user_input = input("Enter:")

