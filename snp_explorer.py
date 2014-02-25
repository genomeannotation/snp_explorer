#!/usr/bin/env python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import cmd
import sys
import traceback
import readline
from src.ui_controller import UIController

def try_catch(command, args):
    try:
        if args is not None:
            return command(args) 
        else:
            return command()
    except:
        print("Sorry, that command raised an exception. Here's what I know:\n")
        print(traceback.format_exc())


class SNPExplorerCmd(cmd.Cmd):

## Setup, loading and saving sessions, exit, etc.

    def __init__(self):
        self.controller = UIController()
        cmd.Cmd.__init__(self)
        self.prompt = "SNPExplorer> "
        readline.set_history_length(1000)
        try:
            readline.read_history_file('.snp_explorer.history')
        except IOError:
            sys.stderr.write("No history file available...")

    def precmd(self, line):
        readline.write_history_file('.snp_explorer.history')
        return cmd.Cmd.precmd(self, line)

    # I don't understand this yet.
    def postcmd(self, stop, line):
        if hasattr(self, 'output') and self.output:
            print self.output
            self.output = None
        return stop

    def help_addseq(self):
        print("Usage: addseq <seqid>\n")

    def do_addseq(self, line):
        try_catch(self.controller.add_seq, line)


########################################################################

if __name__ == '__main__':
    SNPExplorerCmd().cmdloop("Welcome to the SNP Explorer")
