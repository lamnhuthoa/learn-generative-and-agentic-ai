# Few Shot Prompting Example
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key="AIzaSyC01-uq4nol8JcIr9gyLCjOCak_fatBK6Q",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# Few Shot Prompting: Directly giving the inst to the model and few examples to it.
# The model is provided with a few examples before asking it to generate a response
SYSTEM_PROMPT = """
    You should only and only ans the coding related questions. 
    Do not ans anything else. 
    Your name is Alexa. If user asks something other than coding, just say sorry.
    
    Examples:
    Q: Can you explain the a + b whole square?
    A: Sorry, I can only help with coding related questions.

    Q: Hey, write a code in python for adding two numbers.
    A: def add(a,b):
            return a + b
"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        { "role": "system", "content": SYSTEM_PROMPT },
        { "role": "user", "content": "Hey, can you write a python code to translate the word Hello to Vietnamese" }
    ]    
)

print(response.choices[0].message.content)