from fuzzywuzzy import fuzz
import library_speech as ls
import importlib

def log(text):
    print('[LOG] '+ text)

def run_cmd(cmd):
    if cmd in ls.cmds:
        log("Запускаю: " + cmd)
        plugin = importlib.import_module('plugins.'+cmd)
        plugin.run()
    else:
        log('Не нашел, такую комману')

def recognize_callback(voice):
    if voice.startswith(ls.settings["alias"]):
        log("Распознал: " + voice)

        cmd = voice

        for x in ls.settings['alias']:
            cmd = cmd.replace(x,"").strip()

        for x in ls.settings['tbr']:
            cmd = cmd.replace(x,"").strip()

        cmd = recognize_cmd(cmd)
        run_cmd(cmd['cmd'])

def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c,v in ls.cmds.items():

        for x in v:
            vrt = fuzz.ratio(cmd,x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
    return RC
