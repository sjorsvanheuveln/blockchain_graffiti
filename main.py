#!/usr/bin/env python3

''' Engraving ASCII art on the bitcoin blockchain (aka bitcoin graffiti)
    Sjors van Heuveln 06-11-2021
    Description: Serializes ASCII art and envelopes it into a valid bitcoin (testnet) transaction.
    Make your own ASCII: https://cloudapps.herokuapp.com/imagetoascii/
'''

from art import big_saylor as saylor
from helpers import *

width = 40 #in chars -> 80 in hex
saylor_bytes = bytes(saylor, 'ascii')
print(saylor_bytes.hex())
saylor_return = insert_carriage_return_bytes(saylor_bytes, width)

#print ze art
print('\n')
print(saylor_return.decode('ascii'))
print('\n')
print('hexmessage:', saylor_return.hex(), '\n')
print('Deploy this as a message in the bitcoin node.')

