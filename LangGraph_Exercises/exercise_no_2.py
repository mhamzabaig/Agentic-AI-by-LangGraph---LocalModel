from typing import TypedDict,Dict
from langgraph.graph import StateGraph
from IPython.display import Image,display
import math
class AgentState(TypedDict):
    name: str
    values: list
    operation: str
    result: str

def calculator_node(state: AgentState) -> AgentState:
    """This function will perform addition or Multiplication on given values"""
    
    if state["operation"] =="+":
        state["result"] = "Hi "+ state["name"] + " Your deseired result of " + state["operation"] + " on these values " + str(state["values"]) + " is " + str(sum(state["values"]))
    elif state["operation"] =="*":
        state["result"] = "Hi "+ state["name"] + " Your deseired result of " + state["operation"] + " on these values " + str(state["values"]) + " is " + str(math.prod(state["values"]))
    return state

graph = StateGraph(AgentState)
graph.add_node("calculator",calculator_node)
graph.set_entry_point("calculator")
graph.set_finish_point("calculator")

app = graph.compile()
result = app.invoke({"name":"Hamza","values":[1,23,4,5],"operation":"*"})

print(result["result"])
# Get the image bytes from the Mermaid graph
img_bytes = app.get_graph().draw_mermaid_png()

# Save it as exercise_no_1.png in the current directory
with open("exercise_no_2.png", "wb") as f:
    f.write(img_bytes)

print("✅ Image saved as exercise_no_2.png in the current directory.")
