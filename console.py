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

    def emptyline(self):
        """do nothing when line is empty"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
