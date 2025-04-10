
import google.generativeai as genai
import os
from time import sleep
genai.configure(api_key="YOUR_API_KEY")
  
os.system('clear')
print("O O")
print(" V ")

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
    os.system('clear')
    print(" - -")
    print("  ^ ")
    response = chat.send_message(f"{userinput}")
    os.system('clear')
    print("O 0")
    print(" o ")
    print(response.text)
    sleep(4)
    os.system('clear')
    print("O O")
    print(" V ")
try:
    while True:
        talk()
except KeyboardInterrupt:
    print(f"closed {f.name}!")
