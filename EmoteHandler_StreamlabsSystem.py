import clr
import sys
import json
import os
import threading
import codecs
import logging

ScriptName = "Emote Handler"
Website = "http://www.github.com/th3bfg"
Description = "Emote Handler for Streamlabs Bot"
Creator = "th3bfg"
Version = "0.0.1"

# Handler Variables
path = os.path.dirname(__file__)
configFile = "config.json"
lock = threading.Lock()
settings = {}
cooldowns = {} # Dict of Dict containing threads
threadsKeepAlive = True;


# Script Methods
def ScriptToggled(state):
	global threadsKeepAlive
	threadsKeepAlive = state
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
	global cooldowns
	outputMessage = ""
	if data.IsChatMessage():
		user = data.UserName
		if data.GetParam(0) == "Kreygasm":
			outputMessage = "Kreygasm"
			# Check if user has a cooldown
			hasCD = False
			lock.acquire()
			if user in cooldowns:
				if outputMessage in cooldowns[user]:
					hasCD = cooldowns[user][outputMessage].isAlive()
			if not hasCD:
				cooldowns[user] = {}
				cooldowns[user][outputMessage] = CreateCooldown()
				Parent.SendStreamMessage(outputMessage)
			lock.release()
	return

def ReloadSettings(jsonData):
	Init()
	return

def OpenReadMe():
    location = os.path.join(os.path.dirname(__file__), "README.md")
    os.startfile(location)
    return

def Tick():
	return
	
# Helpers
def CreateCooldown():
	timeLeft = settings["cdInterval"] * 60
	thread = threading.Thread(target=CooldownThread, args=([timeLeft]))
	thread.start()
	return thread
		
def CooldownThread(time):
	global threadsKeepAlive
	logging.warning("$time")
	while time > 0 and threadsKeepAlive:
		time -= 1
		time.sleep(1)		
	