import os
import codecs
import json

# Script Info
ScriptName = "Emote Handler"
Website = "https://www.github.com/th3bfg"
Creator = "th3bfg"
Version = "0.0.1"
Description = "Handles how the chatbot responds to Emotes in chat."
SettingsFile = os.path.join(os.path.dirname(__file__), "settings.json")

class Settings(object):
    def __init__(self, settingsfile=None):
        try:
            with codecs.open(settingsfile, encoding="utf-8-sig", mode="r") as f:
                self.__dict__ = json.load(f, encoding="utf-8")
        except:               

    def reload(self, jsondata):
        self.__dict__ = json.loads(jsondata, encoding="utf-8")
        return

    def save(self, settingsfile):
        try:
            with codecs.open(settingsfile, encoding="utf-8-sig", mode="w+") as f:
                json.dump(self.__dict__, f, encoding="utf-8")
            with codecs.open(settingsfile.replace("json", "js"), encoding="utf-8-sig", mode="w+") as f:
                f.write("var settings = {0};".format(json.dumps(self.__dict__, encoding='utf-8')))
        except:
            Parent.Log(ScriptName, "Failed to save settings to file.")
        return

# Bot functions
def Init():
    global ScriptSettings
	ScriptSettings = Settings(SettingsFile)
    return

def ReloadSettings(jsondata):
    global ScriptSettings
    ScriptSettings.reload(jsondata)
    return

def Execute(data):
    return
       
def Tick():
	return