import time
import tts
import music
import date
import random
answers = ["Добрый день сэр"]
aliases = ("привет",'доброе утро','я дома', 'я пришел','я прибыл')

def run():


    music.play()
    time.sleep(3)
    tts.say(text=random.choice(answers))