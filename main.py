import os
import eel

eel.init("evo_front")

os.system('start brave.exe --app="http://localhost:8000/index.html"')

eel.start('index.html', mode=None, host='localhost', block=True)

