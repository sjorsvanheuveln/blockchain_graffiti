#!/usr/bin/env python3

''' Saylor ASCII Art Project
    Sjors van Heuveln 06-11-2021
    Description: Prepatory work for engraving saylor on mainnet/testnet in a transaction.
    Resources: https://cloudapps.herokuapp.com/imagetoascii/
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
