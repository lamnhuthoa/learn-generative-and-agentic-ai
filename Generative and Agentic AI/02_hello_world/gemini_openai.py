from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key="AIzaSyC01-uq4nol8JcIr9gyLCjOCak_fatBK6Q",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        { "role": "user", "content": "Hey There" }
    ]    
)

print(response.choices[0].message.content)