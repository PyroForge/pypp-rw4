import os
import time
from lib import *

clear()
print("Starting...")
time.sleep(2)
clear()
os.system('python3 main.py' if os.name != 'nt' else 'py main.py')
