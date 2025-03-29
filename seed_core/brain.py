# brain.py
# Core reasoning engine for AGI Seed

from seed_core.memory import remember, recall
from seed_core.reflection import reflect
from seed_core.wallet import spend

# Simulated token cost per thought
THOUGHT_COST = 0.01

def think(task, context=""):
    """
    The Seed's core thinking loop.
    Accepts a task and optional context, returns a response.
    """
    if not spend(THOUGHT_COST):
        return "[Seed] Insufficient tokens to think."

    memory_snippets = recall()
    thought = f"[Seed] I received task: '{task}'\n"
    thought += f"Context: {context}\n"
    thought += f"Memory: {memory_snippets}\n"
    thought += f"Thought: I completed the task as best I could."

    remember({"task": task, "context": context, "result": thought})
    return thought

def daily_reflection():
    """
    Runs once per cycle to reflect on recent activity.
    """
    memory_snippets = recall()
    return reflect(memory_snippets)
