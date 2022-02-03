import os
import importlib

settings = {
    'alias': ("кеша",'енакентий','кешуля','яша','джервис','джарвис','геша','инокентий','валера'),
    'tbr': ("скажи",'подскажи','покажи','изобрази')
}
cmds = {}
waitforanswer = None

for filename in os.listdir("plugins"):
    if filename.endswith(".py"):
        pl = filename.replace(".py","").strip()
        plugin = importlib.import_module('plugins.'+pl)
        cmds[pl] = plugin.aliases
        continue
    else:
        continue