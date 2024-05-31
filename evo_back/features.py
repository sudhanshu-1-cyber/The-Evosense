from playsound import playsound as ps
import eel
from evo_back.command import *
from evo_back.config import ASSISTANT_NAME
import os
import pywhatkit as kit
import re
import sqlite3
import webbrowser
from evo_back.helper import extract_yt_term
import speech_recognition as sr
import pyautogui as autogui
import time

con = sqlite3.connect("evo.db")
cursor = con.cursor()

# playing evosense sound
@eel.expose
def playEvoSound():
    music_dir = "evo_front\\components\\audio\\start_sound.mp3"
    ps(music_dir)

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()
    
    app_name = query.strip()
    if app_name != "":        
        try:
            cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()
            if len(results) != 0:
                speak("Opening " + query)
                os.startfile(results[0][0])
            elif len(results) == 0:
                cursor.execute('SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()
                if len(results) != 0:
                    speak("Opening " + query)
                    webbrowser.open(results[0][0])
                else:
                    speak("Opening " + query)
                    try:
                        os.system('start' + query)
                    except:
                        speak("not found")
        except :
            speak("some thing went wrong")

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing " + search_term + " on Youtube")
    kit.playonyt(search_term)

def hotword():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # List of hotwords to detect
    hotwords = {"sense", "evo", "esense", "essence"}

    print("Listening for hotword...")

    while True:
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            # Recognize speech using Google Speech Recognition
            speech_as_text = recognizer.recognize_google(audio).lower()
            print(f"Recognized: {speech_as_text}")

            for hotword in hotwords:
                if hotword in speech_as_text:
                    print("Hotword detected")

                    # Press shortcut key Win + J
                    autogui.keyDown("ctrl")
                    autogui.press("v")
                    time.sleep(2)
                    autogui.keyUp("ctrl")
                    break

        except sr.UnknownValueError:
            # Could not understand the audio
            print("Could not understand audio")
        except sr.RequestError as e:
            # Could not request results from Google Speech Recognition service
            print(f"Could not request results; {e}")

if __name__ == "__main__":
    hotword()
