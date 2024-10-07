import os
import platform

ascii_art="""
                      .__     
  _____   ____   ____ |  |__  
 /     \ /  _ \ / ___\|  |  \  
|  Y Y  (  <_> ) /_/  >   Y  \ 
|__|_|__/\____/\___  /|___|  / 
              /_____/      \/ 

"""

print(ascii_art)

def clear_terminal():
    sistema = platform.system()
    if sistema == "Windows":
        os.system('cls')
    else:
        os.system('clear')