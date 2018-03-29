from playsound import playsound
import random
import os
cwd = os.getcwd()

while True:
    item=raw_input("press enter to play a RickSound")
    num = random.randint(1,20)
    playsound(cwd+"/sounds/rick"+str(num)+".wav")
    if(item=='q'):
        break
