
import google.generativeai as genai
import os
from time import sleep
genai.configure(api_key="YOUR_API_KEY")
  
os.system('clear')
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
def talk():
    userinput = input()
    os.system('clear')
    print("/o~o")
    response = model.generate_content(f"{userinput}")
    os.system('clear')
    print("\OoO/")
    print(response.text)
    sleep(4)
    os.system('clear')
    print("O_O")
try:
    while True:
        talk()
except KeyboardInterrupt:
    print(f"closed {f.name}!")
