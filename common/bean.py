import os


class CommandBuilder:

    def __init__(self, command):
        self.command = command

    def add_arg(self, arg):
        if arg is None:
            raise Exception('Null arg')
        self.command = self.command + ' ' + arg
        return self

    def add_args(self, arg1, arg2):
        return self.add_arg(arg1).add_arg(arg2)

    def execute(self, log=True):
        if log:
            print("execute:\n\t" + self.command)
        os.system(self.command)


class Arg:

    args = {}

    def __init__(self, args):
        for arg in args[1:]:
            if arg.startswith('--'):
                arg = arg[2:]
                pos = arg.find('=')
                if pos > 0:
                    self.args[arg[:pos]] = arg[pos + 1:]
            elif arg.startswith('-'):
                arg = arg[1:]
                self.args[arg] = '-'
            else:
                self.args['url'] = arg

    def get(self, key):
        return self.args.get(key)

    def exist(self, key):
        if self.args.get(key) is None:
            return False
        return True
