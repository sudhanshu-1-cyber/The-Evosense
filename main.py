import os
import eel
from evo_back.features import *

eel.init("evo_front")

playEvoSound()

os.system('start brave.exe --app="http://localhost:8000/index.html"')

eel.start('index.html', mode=None, host='localhost', block=True)
