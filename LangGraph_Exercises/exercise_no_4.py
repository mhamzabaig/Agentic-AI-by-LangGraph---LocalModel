from typing import TypedDict,Dict
from langgraph.graph import StateGraph,START,END
from IPython.display import Image,display

class AgentState(TypedDict):
    num1: int
    num2: int
    num3: int
    num4: int
    operation1: str
    operation2:str
    final_number1:int
    final_number2:int


def choose_next_node(state:AgentState)->AgentState:
    """This function will decide which operation to perform on first two numbers"""

    if state['operation1'] == "+":
        return "addition_operation"
    elif state['operation1'] == "-":
        return "subtraction_operation"


def choose_next_node2(state:AgentState)->AgentState:
    """This function will decide which operation to perform on second two numbers"""

    if state['operation2'] == "+":
        return "addition_operation"
    elif state['operation2'] == "-":
        return "subtraction_operation"


def first_adder(state:AgentState)-> AgentState:
    """This function will add first two numbers of the state"""    
    state["final_number1"] = state["num1"] + state["num2"]
    return state 

def second_adder(state:AgentState)-> AgentState:
    """This function will add second two numbers of the state"""
    state["final_number2"] = state["num3"] + state["num4"]
    return state

def first_subtractor(state:AgentState)-> AgentState:
    """This function will add second two numbers of the state"""
    state["final_number1"] = state["num3"] - state["num4"]
    return state

def second_subtractor(state:AgentState)-> AgentState:
    """This function will add second two numbers of the state"""
    state["final_number2"] = state["num3"] - state["num4"]
    return state

graph = StateGraph(AgentState)
graph.add_node("first_adder",first_adder)
graph.add_node("second_adder",second_adder)
graph.add_node("first_subtractor",first_subtractor)
graph.add_node("second_subtractor",second_subtractor)

graph.add_node("router1",lambda state:state)
graph.add_edge(START,"router1")
graph.add_conditional_edges(
    "router1",
    choose_next_node,
    {
        "addition_operation":"first_adder",
        "subtraction_operation":"first_subtractor"
    }
)
graph.add_edge("first_adder","router2")
graph.add_edge("first_subtractor","router2")

graph.add_node("router2",lambda state:state)
graph.add_conditional_edges(
    "router2",
    choose_next_node2,
    {
        "addition_operation":"second_adder",
        "subtraction_operation":"second_subtractor"
    }
)

graph.add_edge("second_adder",END)
graph.add_edge("second_subtractor",END)

app = graph.compile()
result = app.invoke({"num1":2,"num2":4,"num3":6,"num4":7,"operation1":"+","operation2":"-"})

print(result["final_number1"],result["final_number2"])

# Get the image bytes from the Mermaid graph
img_bytes = app.get_graph().draw_mermaid_png()

# Save it as exercise_no_1.png in the current directory
with open("exercise_no_4.png", "wb") as f:
    f.write(img_bytes)

print("✅ Image saved as exercise_no_3.png in the current directory.")

