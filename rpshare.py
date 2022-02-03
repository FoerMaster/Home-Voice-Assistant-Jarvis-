import reword,os,library_speech,importlib,json
import os.path
import codecs

def write(file,text):
    f = codecs.open("phares/"+file+".txt", "a", encoding='utf-8')
    f.write(text)
    f.close()

def init():
    for filename in os.listdir("plugins"):
        if filename.endswith(".py"):
            pl = filename.replace(".py","").strip()
            plugin = importlib.import_module('plugins.'+pl)

            if not os.path.isfile("phares/"+pl+".txt"):
                prepare = list()
                if hasattr(plugin, 'answers'):
                    for word in plugin.answers:

                        print("Rewording: " + str(word))
                        for i in range(0, 50):
                            rew = reword.paraphrase(word, gram=2, do_sample=True)
                            check = rew.replace(".","")
                            check = check.replace(".", "")
                            check = check.replace(",", "")
                            check = check.replace("!", "")
                            check = check.replace("?", "")
                            if not word in prepare:
                                prepare.append(word)
                                print("To: " + str(word))
                            if not check in prepare:
                                prepare.append(check)
                                print("To: " + str(check))

                    write(pl,json.dumps(prepare, ensure_ascii=False))
                    plugin.answers = prepare
            else:
                plugin.answers = json.loads(codecs.open("phares/"+pl+".txt", "r", encoding='utf-8').read())
            continue
        else:
            continue