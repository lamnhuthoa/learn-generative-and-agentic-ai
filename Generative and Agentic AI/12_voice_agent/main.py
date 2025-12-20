from dotenv import load_dotenv

import speech_recognition as sr
from openai import OpenAI

load_dotenv()

client = OpenAI()

def main():
    r = sr.Recognizer() # Speech to Text
    
    with sr.Microphone() as source: # Mic Access
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 2
        
        print("Speak Something...")
        audio = r.listen(source)
        
        print("Processing Audio... (STT)")
        stt = r.recognize_google(audio)
        
        print("You Said:", stt)
        
        SYSTEM_PROMPT = f"""
            You are an expert voice agent. You are given the transcript of what user has said using voice.
            You need to output as if you are an voice agent and whatever you speak will be converted back to audio using AI and played back to users.
        """
        
        responst = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": stt}
            ]
        )
        
        print("AI Response:", responst.choices[0].message.content)
        
main()