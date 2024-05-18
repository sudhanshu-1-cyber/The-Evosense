from playsound import playsound as ps
import eel

# playing evosense sound
@eel.expose
def playEvoSound():
    music_dir = "evo_front\\components\\audio\\start_sound.mp3"
    ps(music_dir)
