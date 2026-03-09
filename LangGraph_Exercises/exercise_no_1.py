from typing import TypedDict,Dict
from langgraph.graph import StateGraph
from IPython.display import Image,display


class AgentState(TypedDict):
    msg : str

def greeting_node(state: AgentState) -> AgentState:
    """This function is used to greet the user """
    state["msg"] = "Hi there " + state["msg"] + "How are you doing?"
    return state

graph = StateGraph(AgentState)
graph.add_node("greeter",greeting_node)
graph.set_entry_point("greeter")
graph.set_finish_point("greeter")

app = graph.compile()

result  = app.invoke({"msg":"hamza"})
print(result["msg"])

# Get the image bytes from the Mermaid graph
img_bytes = app.get_graph().draw_mermaid_png()

# Save it as exercise_no_1.png in the current directory
with open("exercise_no_1.png", "wb") as f:
    f.write(img_bytes)

print("✅ Image saved as exercise_no_1.png in the current directory.")
