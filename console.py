#!/usr/bin/python3
"""module documentation"""
import cmd


class HBNBCommand(cmd.Cmd):
    """command prompt class"""
    prompt = '(hbnb)'

    def do_quit(self, argument):
        """closes the program"""
        return True

    def do_EOF(self, argument):
        """exits the program"""
        print("")
        return True


if _name_ == '__main__':
    HBNBCommand().cmdloop()
