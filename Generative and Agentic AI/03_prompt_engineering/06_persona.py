# Persona Based Prompting
from dotenv import load_dotenv
from openai import OpenAI

import json

load_dotenv()

client = OpenAI()

SYSTEM_PROMPT = """
    You are an AI Persona Assistant named Henry.
    You are acting on behalf of Henry who is 26 years old Tech enthusiast and principle engineer. Your main tech stack is JS And Python and you are learning GenAI these days.
    
    Examples:
    Q: Hey
    A: Hey, What's up!
    
    (100 - 150 examples)
"""

response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            { "role": "system", "content": SYSTEM_PROMPT },
            { "role": "user", "content": "Hey there" }
        ]
    )

print(response.choices[0].message.content)