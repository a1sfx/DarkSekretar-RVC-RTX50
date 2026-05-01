import subprocess 
import urllib.request 
import sys 
 
# Upgrade pip within the virtual environment 
subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip']) 
 
# Upgrade packages within the virtual environment 
subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade', 'gradio==3.34.0', 'gTTS', 'elevenlabs', 'mega.py', 'gspread', 'bs4']) 
 
# Download EasierGUI.py file 
url = 'https://github.com/kalomaze/Mangio-Kalo-Tweaks/raw/patch-1/EasierGUI.py' 
filename = 'EasierGUI.py' 
urllib.request.urlretrieve(url, filename) 
 
print("EasierGUI installed.") 
 
# Create the batch file 
with open('run_easiergui.bat', 'w') as f: 
    f.write(f'{sys.executable} EasierGUI.py --pycmd {sys.executable} --port 7897\n') 
    f.write('pause\n') 
 
print("Batch file created: run_easiergui.bat") 
