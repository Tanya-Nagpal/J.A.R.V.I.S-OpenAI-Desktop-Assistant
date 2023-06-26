# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

# import win32com.client
#
# speaker = win32com.client.Dispatch("SAPI.SpVoice")
# while 1:
#     print("Enter the word you want to speak it out by computer")
#     s = input()
#     speaker.Speak(s)

import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import subprocess
import datetime
import random
# import wikipedia
import openai
from config import apikey


chatStr = " "
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Tanya: {query}\n Jarvis:
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo : Wrap this inside a try cache block
    try:
        say(response["choices"][0]["text"])
        chatStr += f"{response['choices'][0]['text']}"\n
        return response['choices'][0]['text']

    with open(f"OpenAI/{' '.join(prompt.split('AI')[1:]).strip()}.txt", "w") as f:
        f.write(text)

def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for prompt: {prompt.split('AI')[1:]} \n-----------------------------------------------------------------------\n"
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt = prompt,
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    # todo : Wrap this inside a try cache block
    try:
        print(response["choices"][0]["text"])
        text += response["choices"][0]["text"]
        if not os.path.exists("OpenAI"):
            os.mkdir("OpenAI")
        with open(f"OpenAI/{' '.join(prompt.split('AI')[1:]).strip()}.txt", "w") as f:
            f.write(text)
    except (KeyError, IndexError) as e:
        print("Error: Failed to retrieve response from OpenAI API")

def say(text):
    # os.system(f"say {text}")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing.....")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred!"

if __name__ == '__main__':
    print('PyCharm')
    say("Hello I'm Jarvis AI")
    while True:
        print("Listening......")
        query = takeCommand()
        # say(query)
        # todo: add more sites
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"], ["instagram", "https://www.instagram.com"] ]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]}........")
                webbrowser.open(site[1])
                # todo :  add a feature to play specific songs
            elif "open music" in query:
                musicPath = r'C:\Users\tanya\Music\YouNeedToCalmDownInstrumental.mp3'
                os.system(f'start "" "{musicPath}"')
            elif "stop music" in query:
                # os.system("taskkill /f /im wmplayer.exe")
                os.system("taskkill /f /t /im C:\\Program Files\\Windows Media Player\\wmplayer.exe")

            elif "the time" in query:
                musicPath = r'C:\Users\tanya\Music\YouNeedToCalmDownInstrumental.mp3'
                strfTime = datetime.datetime.now().strftime("%H:%M:%S")
                say(f"The time is {strfTime}")
            elif "open udemy".lower() in query.lower():
                os.system('start "" "C:\\Users\\tanya\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Chrome Apps\\Udemy.lnk"')
            elif "Using open AI".lower() in query.lower():
                ai(prompt=query)
            elif "Jarvis Quit".lower() in query.lower():
                exit()
            elif "reset chat".lower() in query.lower():
                chatStr = " "

            else:
                chat(query)

  #todo: Detect weather using weather API
  #todo: Detect news using News API
