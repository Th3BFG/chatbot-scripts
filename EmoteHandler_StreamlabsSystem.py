import clr
import sys
import json
import time
import os
import threading
import codecs

ScriptName = "Emote Handler"
Website = "http://www.github.com/th3bfg"
Description = "Emote Handler for Streamlabs Bot"
Creator = "th3bfg"
Version = "0.0.1"

# Handler Variables
path = os.path.dirname(__file__)
configFile = "config.json"
settings = {}
timeFromLastTick = time.time()
cooldownActive = False;
threadsKeepAlive = True;
cooldown = {
    "fileName": "cooldown.txt",
    "timeLeft": 0,
    "running": False,
}

# Script Methods
def ScriptToggled(state):
	global threadsKeepAlive
	if state:
		threadsKeepAlive = True
	else:
		ResetCooldown()
		threadsKeepAlive = False
	return

def Init():
	global settings, path, configFile

	path = os.path.dirname(__file__)
	try:
		with codecs.open(os.path.join(path, configFile), encoding='utf-8-sig', mode='r') as file:
			settings = json.load(file, encoding='utf-8-sig')
	except:
		settings = {
			"cdInterval": 3,
		}

def Execute(data):
	global settings, cooldown
	outputMessage = ""
	if data.IsChatMessage():
		if data.GetParam(0) == "Kreygasm":
			# Check if user has a cooldown
			if not cooldownActive:
				outputMessage = "Kreygasm"
				StartCooldown()
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
	
# Helpers
def StartCooldown():
	global cooldown, settings, cooldownActive
	cooldown["running"] = True
	if not cooldownActive:
		threading.Thread(target=CooldownThread, args=()).start()
		
def ResetCooldown():
	global cooldown, settings
	cooldown["timeLeft"] = settings["cdInterval"] * 60
	cooldown["running"] = False;
	with codecs.open(os.path.join(path, cooldown["fileName"]), encoding='utf-8-sig', mode='w+') as file:
		file.write(" ")
		
def CooldownThread():
	global cdVariables, cooldown, settings, timeFromLastTick, cooldownActive, threadsKeepAlive
	cooldownActive = True
	while cooldown["running"] and threadsKeepAlive:
		cooldown["timeLeft"] -= 1
		if cooldown["currentTime"] < 0:
			cooldown["timeLeft"] = False
		time.sleep(1)
	cooldownActive = False
		
	