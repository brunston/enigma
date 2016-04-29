#class versions of all the other files
import sys
import random
import math

class NumberSet:
    "common base class for all number manipulations"

    def __init__(self, x=-1, z=-1, a=-1):
        pass

class RSA64:
    """generates RSA keys and decrypts/encrypts up to keys of 64 bits
       not cryptographically secure, also a textbook implementation"""

    def __init__(self, key_size):
        if key_size > 64:
            sys.exit("key_size too large. try with bit < 64")            
        self.key_size = key_size
        
