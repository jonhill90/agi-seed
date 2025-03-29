# script_writer.py
# Simple script generation tool for AGI Seed

def generate_script(language, task_description):
    """
    Returns a boilerplate script in the specified language for a described task.
    """
    if language.lower() == "bash":
        return f"# Bash script: {task_description}\n#!/bin/bash\necho \"{task_description}\""
    elif language.lower() == "python":
        return f"# Python script: {task_description}\nprint(\"{task_description}\")"
    elif language.lower() == "powershell":
        return f"# PowerShell script: {task_description}\nWrite-Output \"{task_description}\""
    else:
        return f"# Unsupported language: {language}\n# Task: {task_description}"