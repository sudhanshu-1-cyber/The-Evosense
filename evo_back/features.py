import re
from playsound import playsound as ps
import eel
from evo_back.command import *
import os
from evo_back.config import ASSISTANT_NAME
import pywhatkit as kit

# playing evosense sound
@eel.expose
def playEvoSound():
    music_dir = "evo_front\\components\\audio\\start_sound.mp3"
    ps(music_dir)

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()
    
    if query != "":
        speak("Opening " + query)
        os.system("start " + query)
    
    else:
        speak("not found")

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing " + search_term + " on youtube")
    kit.playonyt(search_term)

def extract_yt_term(command):
    #Define a regular expression pattern to capture the song name
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    #Use re.search to find the match in the command
    match = re.search(pattern, command, re.IGNORECASE)
    #if a match is found, return the extracted song name; otherwise, return None
    return match.group(1) if match else None
