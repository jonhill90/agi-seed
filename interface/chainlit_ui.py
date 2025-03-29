# chainlit_ui.py
# Minimal Chainlit interface for the AGI Seed

import chainlit as cl
from seed_core.brain import think, daily_reflection
from seed_core.wallet import get_balance

@cl.on_chat_start
async def start():
    await cl.Message(content="🌱 Hello, I am the Seed. Give me a task or ask me to reflect.").send()

@cl.on_message
async def handle_message(message: cl.Message):
    content = message.content.strip().lower()

    if content == "reflect":
        response = daily_reflection()
    elif content == "balance":
        balance = get_balance()
        response = f"[Seed Wallet] Balance: {balance:.4f} tokens"
    else:
        response = think(task=message.content)

    await cl.Message(content=response).send()
