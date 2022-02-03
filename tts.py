def say(text):
    import pyttsx3 as pt
    a = pt.init()
    a.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_ruRU_PavelM")
    a.setProperty('rate', 150)
    a.say(text)
    a.runAndWait()