from dotenv import load_dotenv

from agents import Agent, Runner

load_dotenv()

hello_agent = Agent[Any](
    name="Hello World Agent",
    instructions="You're an agent who greets the user and helps them answer using emojis and in funny ways"
)

result = Runner.run_sync(hello_agent, "Hey, my name is Henry")

print(result.final_output)