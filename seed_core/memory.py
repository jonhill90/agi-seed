# memory.py
# Episodic memory system for the AGI Seed

import datetime

# Simple in-memory storage for events
memory_store = []

def remember(event):
    """
    Store an event in memory with a timestamp.
    """
    memory_entry = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "event": event
    }
    memory_store.append(memory_entry)

def recall(limit=10):
    """
    Retrieve the most recent events from memory.
    """
    return memory_store[-limit:]