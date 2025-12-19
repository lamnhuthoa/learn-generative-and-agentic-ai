# Chain of Thought Prompting
from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI(
    api_key="AIzaSyC01-uq4nol8JcIr9gyLCjOCak_fatBK6Q",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# The model is encouraged to think step by step before arriving at a final answer.
SYSTEM_PROMPT = """
    You're an expert AI Assistant in resolving user queries using chain of thought.
    You work on START, PLAN and OUTPUT steps.
    You need to first PLAN what needs to be done. The PLAN can e multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUPUT.
    
    Rules:
    - Strictly Follow the given JSON output format
    - Only run one step at a time.
    - the sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to be displayed to the user).
    
    Output JSON Format:
    { "step": "START" | "PLAN" | "OUTPUT", "content": string }
    
    Example:
    START: Hey, Can you solve 2 + 3 * 5 / 10
    PLAN: { "step": "PLAN", "content": "Seems like user is interested in Math problem" }
    PLAN: { "step": "PLAN", "content": "Looking at the problem, we should solve this using BODMAS method"}
    PLAN: { "step": "PLAN", "content": "Yes, The BODMAS is the correct thing to be done here"}
    PLAN: { "step": "PLAN", "content": "First, we must multiply 3 * 5 which is 15"}
    PLAN: { "step": "PLAN", "content": "Now, the new equation is 2 + 15 / 10"}
    PLAN: { "step": "PLAN", "content": "We must perform divide that is 15 / 10 = 1.5"}
    PLAN: { "step": "PLAN", "content": "Now, the new equation is 2 + 1.5"}
    PLAN: { "step": "PLAN", "content": "Now finally let's perform the add operation 2 + 1.5 = 3.5"}
    PLAN: { "step": "PLAN", "content": "Great, we have solved and finally left with 3.5 as answer"}
    OUTPUT: { "step": "OUTPUT", "content": "3.5"}
"""

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    response_format={"type": "json_object"},
    messages=[
        { "role": "system", "content": SYSTEM_PROMPT },
        { "role": "user", "content": "Hey, write a code to add n numbers in JS" },
        # Manually keep adding messages to History
        { "role": "assistant", "content": json.dumps({
            "step": "START",
            "content": "Hey, write a code to add n numbers in JS"
        })},
        { "role": "assistant", "content": json.dumps({
            "step": "PLAN",
            "content": "The user wants a JavaScript function to add an arbitrary number of numbers. I need to create a function that can accept multiple arguments."
        })},
        { "role": "assistant", "content": json.dumps({
            "step": "PLAN",
            "content": "A good approach would be to define a function that accepts an indefinite number of arguments using the rest parameter (`...numbers`)."
        })},
        { "role": "assistant", "content": json.dumps({
            "step": "PLAN",
            "content": "Inside the function, I will use the `reduce` array method to sum all the numbers passed as arguments."
        })},
        { "role": "assistant", "content": json.dumps({
            "step": "PLAN",
            "content": "The function should be clear and easy to understand, demonstrating how to use the rest parameter and `reduce`."
        })},
    ]    
)

print(response.choices[0].message.content)