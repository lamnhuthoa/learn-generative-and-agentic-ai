# Chain of Thought Prompting
from openai import OpenAI
from dotenv import load_dotenv
import requests
from pydantic import BaseModel, Field
from typing import Optional
import json
import subprocess

load_dotenv()

client = OpenAI()

def run_command(cmd: str):
    completed = subprocess.run(
        ["powershell", "-Command", cmd],
        capture_output=True,
        text=True
    )
    return completed.stdout or completed.stderr

def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)
    
    if response.status_code == 200:
        return f"The weather in {city} is: {response.text}"
    
    return "Something went wrong"

available_tools = {
    "get_weather": get_weather,
    "run_command": run_command
}

# The model is encouraged to think step by step before arriving at a final answer.
SYSTEM_PROMPT = """
    You're an expert AI Assistant in resolving user queries using chain of thought.
    You work on START, PLAN and OUTPUT steps.
    You need to first PLAN what needs to be done. The PLAN can e multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUPUT.
    You can also a tool if required from the list of available tools.
    For every tool call, wait for the observe step which is the output of the tool call.
    
    Rules:
    - Strictly Follow the given JSON output format
    - Only run one step at a time.
    - the sequence of steps is START (where user gives an input), PLAN (That can be multiple times) and finally OUTPUT (which is going to be displayed to the user).
    
    Output JSON Format:
    { "step": "START" | "PLAN" | "OUTPUT" | "TOOL", "content": string, "tool": "string", "input": "string" }

    Available tools:
    - get_weather(city: str): Takes city name as an input string and returns the current weather information for that city.
    - run_command(cmd: str): Takes a powershell system command as string and executes the command on user's system and returns the output from that command.
    
    Example 1:
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
    
    Example 2:
    START: What is the weather of New York City?
    PLAN: { "step": "PLAN", "content": "Seems like user is interested in getting weather of New York City in the United States" }
    PLAN: { "step": "PLAN", "content": "Lets see if we have any available tools to get the weather information" }
    PLAN: { "step": "PLAN", "content": "Great, we have get_weather tool available for this query"}
    PLAN: { "step": "PLAN", "content": "I need to call get_weather tool for New York as input for city"}
    PLAN: { "step": "TOOL", "tool": "get_weather", "content": "New York"}
    PLAN: { "step": "OBSERVE", "tool": "get_weather", "output": "The temperature in New York is -1°C with clear skies."}
    PLAN: { "step": "PLAN", "content": "Great, I have the weather information for New York City now"}
    OUTPUT: { "step": "OUTPUT", "content": "The current weather in New York City is -1°C with clear skies."}
"""

print("\n\n\n")

class MyOutputFormat(BaseModel):
    step: str = Field(..., description="The ID of the step. Example: PLAN, OUTPUT, TOOL, etc.")
    content: Optional[str] = Field(None, description="The optional string content for the step.")
    tool: Optional[str] = Field(None, description="The ID of the tool to call.")
    input: Optional[str] = Field(None, description="The input params for the tool.")

message_history = [
    { "role": "system", "content": SYSTEM_PROMPT },
]

while True:

    user_query = input("👉 ")
    message_history.append({ "role": "user", "content": user_query })

    while True:
        response = client.chat.completions.parse(
            model="gpt-4o",
            response_format=MyOutputFormat,
            messages=message_history
        )
        
        raw_result = (response.choices[0].message.content)
        message_history.append({ "role": "assistant", "content": raw_result })
        
        parsed_result = (response.choices[0].message.parsed)
        
        if parsed_result.step == "START":
            print("🔥", parsed_result.content)
            continue
        
        if parsed_result.step == "TOOL":
            tool_to_call = parsed_result.tool
            tool_input = parsed_result.input
            print("🔧", f"{tool_to_call} ({tool_input})")
            
            tool_response = available_tools[tool_to_call](tool_input)
            print("🔧", f"{tool_to_call} ({tool_input}) = {tool_response}")
            message_history.append({"role":"developer", "content": json.dumps(
                { "step":"OBSERVE", "tool": tool_to_call, "input": tool_input, "output": tool_response }
            )})
            continue
        
        if parsed_result.step == "PLAN":
            print("🧠", parsed_result.content)
            continue
        
        if parsed_result.step == "OUTPUT":
            print("🧑‍💻", parsed_result.content)
            break

    print("\n\n\n")
