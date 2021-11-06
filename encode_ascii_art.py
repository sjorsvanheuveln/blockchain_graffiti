#!/usr/bin/env python3

from saylor_string import *
width = 40 #in chars -> 80 in hex

# #convert ascii chars to bytes
# saylor_bytes = bytes(saylor, 'ascii')

# #make a hex dump
# saylor_hex = saylor_bytes.hex()

# #insert hexadecimal carriage returns across the width (note this 2hex per char)
# saylor_formatted = insert_carriage_return_hex(saylor_hex, 2 * width) #this is the data that should be inserted 

# #reserialize to bytes
# saylor_decoded = bytes.fromhex(saylor_formatted) # and this is the serialized thing

# #make the art (without for-loop)
# print(saylor_decoded.decode('ascii'))



saylor_bytes = bytes(saylor, 'ascii')
saylor_return = insert_carriage_return_bytes(saylor_bytes, width)
print(saylor_return.decode('ascii'))



'''improvements
The conversion from bytes to hex to bytes is redundant. I could insert a carriage return in bytes.
'''