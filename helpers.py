def insert_carriage_return_bytes(b, width):
    ''' Inserts carriage returns for bytearray art
        This I learned from the rich astley block, where 0a encodes for a carriage return.
        https://www.blockchain.com/btc/tx/d29c9c0e8e4d2a9790922af73f0b8d51f0bd4bb19940d9cf910ead8fbe85bc9b
    '''

    new_b = b''
    for i in range(0,len(b), width):
        new_b += b[i : (i + width)] + b'\x0a'

    return new_b
