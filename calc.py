#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculator in infix syntax - requires Python version >= 3.10
"""

import sys
assert sys.version_info >= (3, 10), "Use Python 3.10 or newer !"

from parser_1 import init_parser, parse_token, get_current
from tokenDEF import Token


###################
## the public function of the calculator

def parse(stream=sys.stdin):
    init_parser(stream)
    l = parse_input()
    parse_token(Token.END)
    return l

#########################
## parsing of input

def parse_input():
    print("@ATTENTION: calc.parse_input à corriger !") # LIGNE A SUPPRIMER
    return []


#########################
## run on the command-line

if __name__ == "__main__":
    print("@ Testing the calculator in infix syntax.")
    print("@ Type Ctrl-D to quit")
    print("@ result = ", repr(parse()))
