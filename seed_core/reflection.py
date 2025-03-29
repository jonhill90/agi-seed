# reflection.py
# Reflection logic for the AGI Seed

def reflect(memory_snippets):
    """
    Review memory and return a reflection summary.
    """
    if not memory_snippets:
        return "[Seed] I have no memory to reflect on."

    summary = "[Seed Reflection]\n"
    summary += f"Reviewed {len(memory_snippets)} events.\n"

    tasks = [entry['event'].get("task", "") for entry in memory_snippets if isinstance(entry['event'], dict)]
    unique_tasks = list(set(tasks))

    summary += f"Noticed these unique tasks: {unique_tasks}\n"
    summary += "I will try to be more efficient and purposeful in future thinking cycles."

    return summary