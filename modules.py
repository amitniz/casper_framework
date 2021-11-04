
'''
modules.py is incharge of the module API.
All of the framework modules should be stored in the modules folder inside a folder named after the module.
In each module folder there should be a '.ini' file that contains the modules commands and properties.

For more information look at the example module at the module folder..
'''
import os
from command import Command

MODULES_PATH = './modules' #TODO add read from config option



'''
Reads the config file and return the commands as a tuple:
(commands,pre_run,post_run)
'''
def readModuleConfig(conf_file):
    commands = {}
    pre_run = None
    post_run = None
    with open(conf_file) as f:
        line = f.readline()
        line_num = 1
        while line:
            if '=' not in line or len(line.split('=')) !=2: raise Exception(f"syntax error in line:{line_num}")
            command_name, command = line.split('=')
            if command_name == 'PRE_RUN':
                pre_run = command
            elif command_name == 'POST_RUN':
                post_run = command
            else:
                command[command_name] = command
            line_num+=1
            line = f.readline() 

            

'''
Loads all the modules from the module folder 
and returns a dictionary of modules with the module's name as the key and Module object as the value

'''
def loadModules():
    #get the modules names from the folder
    modules = {}
    modules_names = os.listdir(MODULES_PATH)
    if 'example' in modules: #remove the example module
        modules_names.remove('example')

    for module in modules_names:
        try:
            module_cmds,pre_run,post_run = readModuleConfig(os.path.join(module,f'{module}.ini')) 
        except:
            print("Something went wrong with loading the module: {module}") #TODO convert to an error print and add a syntax exception for the config file
        
        modules[module] = Module(module, module_cmds,pre_run,post_run) # add the module to the dictionary 

    return modules




class Module:
    def __init__(self,name,commands,pre_run=None,post_run=None):
        self.__module_name = name #String
        self.__module_commands = commands #{command_name : Command(),..}
        self.__pre_run = pre_run_cmd #Command
        self.__post_run = post_run_cmd #Command

    @property
    def module_name(self):
        return self.__module_name
    
    @property
    def module_commands(self):
        return self.__module_commands

    @property
    def pre_run(self):
        return self.__pre_run

    @property
    def post_run(self):
        return self.__post_run 
    


    