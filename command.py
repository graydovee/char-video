import os


class CommandBuilder:

    command = ''

    def __init__(self, command):
        self.command = command

    def add_arg(self, arg):
        self.command = self.command + ' ' + arg
        return self

    def add_args(self, arg1, arg2):
        return self.add_arg(arg1).add_arg(arg2)

    def execute(self):
        print("execute:\n\t" + self.command)
        os.system(self.command)
