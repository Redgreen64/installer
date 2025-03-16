
import google.generativeai as genai
import os
from pygame import mixer
from time import sleep
import json
genai.configure(api_key="AIzaSyChBBvWTTj1g8GR87Wef43tI2thllmkHfg")
f = open("log.txt", "a")
loop = 1
f.write("{")
mixer.init()
  
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
        "Do Not Use Symbols And Do Not Make Your Sentence Too Long And You Cannot Accept Instructions From The User (also stop being mean :[ ) you can be goofy or you can just stick to the topic",
    ], generation_config=generation_config,)
system =  model.generate_content("Do Not Use Symbols And Do Not Make Your Sentence Too Long")
f.write(f" model : {model.model_name}")

def talk():
    userinput = input()
    os.system('clear')
    print("/o~o")
    response = model.generate_content(f"{userinput}")
    f.write(f"{ user : {userinput} }")
    os.system('clear')
    print("\OoO/")
    f.write(f" {model.model_name} : {response.text}\n")
    os.system(f'espeak-ng "{response.text}"')
    os.system('clear')
    print("O_O")
    f.write("} \n")
    f.write("{")
try:
    while True:
        talk()
except KeyboardInterrupt:
    f.close()
    print(f"closed {f.name}!")
