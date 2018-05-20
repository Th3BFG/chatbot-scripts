import clr
import sys
import json
import os
import ctypes
import codecs

ScriptName = "Emote Handler"
Website = "http://www.github.com/th3bfg"
Description = "Emote Handler for Streamlabs Bot"
Creator = "th3bfg"
Version = "0.0.1"

configFile = "config.json"
settings = {}

def ScriptToggled(state):
	return

def Init():
	global settings

	path = os.path.dirname(__file__)
	try:
		with codecs.open(os.path.join(path, configFile), encoding='utf-8-sig', mode='r') as file:
			settings = json.load(file, encoding='utf-8-sig')
	except:
		settings = {}

def Execute(data):
	if data.IsChatMessage():
		outputMessage = "YEEEEEEEEEEEET"
		Parent.SendStreamMessage(outputMessage)
	return

def ReloadSettings(jsonData):
	Init()
	return

def OpenReadMe():
    location = os.path.join(os.path.dirname(__file__), "README.txt")
    os.startfile(location)
    return

def Tick():
	return