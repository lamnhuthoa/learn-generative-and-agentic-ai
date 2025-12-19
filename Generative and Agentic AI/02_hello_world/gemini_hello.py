from google import genai

client = genai.Client(
    api_key="AIzaSyC01-uq4nol8JcIr9gyLCjOCak_fatBK6Q"
)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
)

print(response.text)