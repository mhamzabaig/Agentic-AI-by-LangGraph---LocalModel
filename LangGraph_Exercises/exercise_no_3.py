from typing import TypedDict,Dict
from langgraph.graph import StateGraph
from IPython.display import Image,display

class AgentState(TypedDict):
    name:str
    age: int
    skills: list
    result: str
def first_node(state:AgentState)->AgentState:
    """This is the first node that will be used to update the name of the user interacting with the agent"""
    state["result"] = "Hi " + state["name"] + " "
    return state

def second_node(state:AgentState)-> AgentState:
    """This is second node that will  be used to update the user age """
    state["result"] = state["result"] + "I am " + str(state["age"]) + " years old. "
    return state

def third_node(state:AgentState)-> AgentState:
    """This is third node that will update the skills ofthe user"""
    # state["result"] = state["result"] + "I am exper in "+ f" You have skills in:  {", ".join(state["skills"])}"
    state["result"] += f"I am exper in. You have skills in: {', '.join(state['skills'])}"
    return state

graph = StateGraph(AgentState)
graph.add_node("first_node",first_node)
graph.add_node("second_node",second_node)
graph.add_node("third_node",third_node)

graph.set_entry_point("first_node")
graph.add_edge("first_node","second_node")
graph.add_edge("second_node","third_node")
graph.set_finish_point("third_node")

app = graph.compile()
result = app.invoke({"name":"HAmza","age":23,"skills":["OOOP","C++","Python"]})
print(result["result"])
# Get the image bytes from the Mermaid graph
img_bytes = app.get_graph().draw_mermaid_png()

# Save it as exercise_no_1.png in the current directory
with open("exercise_no_3.png", "wb") as f:
    f.write(img_bytes)

print("✅ Image saved as exercise_no_3.png in the current directory.")
