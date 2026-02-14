
import google.generativeai as genai
import os
import sys
from pygame import mixer
from time import sleep
genai.configure(api_key="YOUR_API_KEY")
loop = 1
mixer.init()
  
sys.stdout.flush()
print("O_O")

generation_config = {
  "temperature": 2,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(model_name="gemini-2.0-flash",
                              system_instruction=[
        "",
    ], generation_config=generation_config,)
chat = model.start_chat(history=[])

def talk():
    userinput = input()
    sys.stdout.flush()
    print("/-_-\")
    response = chat.send_message(f"{userinput}")
    sys.stdout.flush()
    print("\OoO/")
    os.system(f'espeak-ng "{response.text}"')
    sys.stdout.flush()
    print("O_O")
try:
    while True:
        talk()
except KeyboardInterrupt:
    print("closed")
