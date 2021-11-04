#!/usr/env python3
__author__="Amit Nizri, https://github.com/AmitNiz"

import os
import readline
from command import Command
import modules
CONFIG_PATH= ['./.casper.conf']
HISTORY_SIZE = 1000

#run the framework as sudo should'nt be allowed.
def sudoCheck():
	if not os.getuid():
		print("[!] Running as Sudo is forbidden!") #TODO update to error print
		exit(1)

class Shell:
	def __init__(self):
		self.prompt_sign = '->'
		self.history = self._createHistFile()
		self.last_commands = []
		self.variables = {}
		self.aliases = {}
		self.modules = modules.loadModules()	

	def begin(self):
		while True:
			cmd = Command(input(self.prompt))
			self.last_commands.append(cmd)
			self.exec(cmd)			


	def exec(self,command):
		print(f"exec: {command.module}: {command.module_args}") #TODO: for debugging. remove later
		#TODO: FORK,EXEC

	def _createHistFile(self):
		pass

	def loadConfig(self):
		pass
	
	@property
	def prompt(self):
		#TODO add more options like hostname etc..
		return self.prompt_sign +' '

if __name__ == '__main__':
	sudoCheck() #check if running as sudo
	shell = Shell()
	shell.begin() #summon casper!
