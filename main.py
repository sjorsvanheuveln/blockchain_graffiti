#!/usr/bin/env python3

''' Engraving ASCII art on the bitcoin blockchain (aka bitcoin graffiti)
    Sjors van Heuveln 06-11-2021
    Description: Serializes ASCII art and envelopes it into a valid bitcoin (testnet) transaction.
    Make your own ASCII: https://cloudapps.herokuapp.com/imagetoascii/
'''

from art import saylor
from helpers import *

width = 40 #in chars -> 80 in hex
saylor_bytes = bytes(saylor, 'ascii')
saylor_return = insert_carriage_return_bytes(saylor_bytes, width)

#print ze art
print('\n')
print(saylor_return.decode('ascii'))
print('\n')
