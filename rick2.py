#!/usr/bin/env python

import aiy.audio
import aiy.voicehat
import logging
import random
import os

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
)

def main():
    status_ui = aiy.voicehat.get_status_ui()
    statsu_ui.status('starting')
    button = aiy.voicehat.get_button()
    cwd = os.getcwd()

    while True:
        button.wait_for_press()
        num = random.randint(1,20)
        pth = cwd+"/sounds/rick"+str(num)+".wav"
        statsu_ui.status(pth)
        statsu_ui.status('playin rick')
        os.system('aplay '+pth)

if __name__ == '__main__':
    main()
