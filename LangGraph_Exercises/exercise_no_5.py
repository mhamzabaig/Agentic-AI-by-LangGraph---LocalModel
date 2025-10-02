from typing import TypedDict,Dict
from langgraph.graph import StateGraph,START,END
from IPython.display import Image,display
import random
class AgentState(TypedDict):
    guess_count:int
    name:str
    lower_bound:int
    upper_bound:int
    guesses:list
    target:int
    

def setup(state:AgentState)-> AgentState:
    """this function is used to initilaize values of the games"""
    state["guess_count"] = 0
    state["target"] = random.randint(state["lower_bound"],state["upper_bound"])
    return state

def guess(state:AgentState)-> AgentState:
    """This function is used to guess the number in between upper and lower bound"""
    guess = random.randint(state["lower_bound"],state["upper_bound"])
    state["guesses"].append(guess)
    state["guess_count"]+=1
    return state

def hint(state:AgentState)->AgentState:
    """This function will update the hint of the game by using lower or upper bound values"""
    guess = state["guesses"][-1]
    if guess == state["target"]:
        print(f"You found the number {guess}")
    elif guess < state["target"]:
        state["lower_bound"] = guess
    else:
        state["upper_bound"] = guess
    
    return state

def should_continue(state:AgentState)->AgentState:
    """This function will check whether the target is found or we are out of attempts"""
    if state["guesses"][-1] == state["target"]:
        return "end"
    elif state["guess_count"] >=7:
        print(f"You  ran out of attempts. Your guesses were {', '.join(state['guesses'])} ")
        return"end"
    else:
        return "continue"

graph = StateGraph(AgentState)
graph.add_node("setup", setup)
graph.add_node("hint", hint)
graph.add_node("guess", guess)

graph.add_edge(START,"setup")
graph.add_edge("setup","guess")
graph.add_edge("guess","hint")

graph.add_conditional_edges(
    "hint",
    should_continue,
    {
        "continue":"guess",
        "end":END
    }
)

app = graph.compile()
result = app.invoke({"name":"Hamza","guess_count":0,"guesses":[],"lower_bound":0,"target":9,"upper_bound":30})

# Get the image bytes from the Mermaid graph
img_bytes = app.get_graph().draw_mermaid_png()

# Save it as exercise_no_1.png in the current directory
with open("exercise_no_5.png", "wb") as f:
    f.write(img_bytes)

print("✅ Image saved as exercise_no_5.png in the current directory.")

