import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import os
import subprocess
import wikipedia
import pyjokes
import webbrowser
import operator
from datetime import date
from datetime import time

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voices)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who  is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk(date.today())
    elif 'notepad'in command:
        talk(subprocess.call('notepad'))
    elif'youtube' in command:
        talk(webbrowser.open('https://www.youtube.com'))  
    elif 'spotify' in command:
        talk(subprocess.call('spotify'))
         
    
    elif 'joke' in command:
        talk(pyjokes.get_joke())
      
    elif 'open a browser'or 'google' in command:
        talk(webbrowser.open('http://google.com'))
    elif'weather'or'temperature'or 'humidity'in command:
        talk(webbrowser.open('http://weather.com'))
    else:
        talk('Please say the command again.')


while True:
    run_alexa()
