from enum import Enum

class Redirection(Enum):
    NONE = 0
    WRITE = 1
    APPAND = 2
    READ = 3



class Command:
    def __init__(self,command):
        self.properties = {'pipe':False,'redirection':Redirection.NONE,'background': False}
        self.parsed_cmd = self._parseCommand(command)
        #TODO update the command properties

    def _parseCommand(self,command):
        #TODO update to support more complexed parsing.
        return command.split() #temporary!
        
    @property
    def module(self):
        module = self.parsed_cmd[0]
        if module == '!':
            return 'extrernal'
            
        elif module == '?':
            return 'help'
        
        elif module == '??':
            return 'calc'

        else:
            return module

    @property
    def module_args(self):
        end_of_module_args_pos = min(self.parsed_cmd.index(sym) if sym in self.parsed_cmd 
                                    else len(self.parsed_cmd) for sym in ['|','>','>>']) #switch to regex

        return ' '.join(self.parsed_cmd[1:end_of_module_args_pos])