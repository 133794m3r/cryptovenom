#!/usr/bin/python

#
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#
#                    [====={ CRYPTO VENOM }=====]
#
#     | ATTENTION!: THIS SOFTWARE IS PART OF THE "CRYPTOVENOM FRAMEWORK" |
#
#              ( https://github.com/lockedbyte/cryptovenom )
#
#           << GNU PUBLIC LICENSE >>
#
#                               / CREATED BY LOCKEDBYTE /
#
#                  [ CONTACT => alejandro.guerrero.rodriguez2@gmail.com ]
#                  [ CONTACT => @LockedByte (Twitter) ]
#
#
# AND NOW...HERE THE CODE
#
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#

from twofish import Twofish
import base64
import base58
import binascii

BLOCK_SIZE = 16  
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

def text_to_bits(text, encoding='utf-8'):

    bits = bin(int(binascii.hexlify(text.encode(encoding)), 16))[2:]
    
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def text_from_bits(bits, encoding='utf-8'):

    n = int(bits, 2)
    
    return int2bytes(n).decode(encoding)

def int2bytes(i):

    hex_string = '%x' % i
    
    n = len(hex_string)
    
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

def xor(raw, key):
    
    xored = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(data, cycle(key)))
    return xored
        

def encrypttwofish(importx, filepath, export, expfilepath, inputformat, passwd, raw):

    if keyimport == 'base64':
    
        key = base64.b64decode(passwd)
        
    elif keyimport == 'raw':
    
        key = passwd 
    
    elif keyimport == 'base32':
    
        key = base64.b32decode(passwd)
    
    elif keyimport == 'base16':
    
        key = base64.b16decode(passwd)
    
    elif keyimport == 'base58':
    
        key = base58.b58decode(passwd)
    
    elif keyimport == 'base85':
    
        print('\033[1;31m[-]\033[0m Option not available yet')
    
    elif keyimport == 'hex':
    
        key = passwd.decode('hex')
    
    elif keyimport == 'dec':
    
        print('\033[1;31m[-]\033[0m Option not available yet')
    
    elif keyimport == 'octal':
    
        print('\033[1;31m[-]\033[0m Option not available yet')
    
    elif keyimport == 'binary':
    
        key = text_from_bits(passwd)
        
    else:
    
        print('\033[1;31m[-]\033[0m Unknown error.')
        return False
        

    if importx == 'file':
    
        f = open(impfilepath, 'r')
        raw = f.read()
        f.close()
        
    elif importx == 'print':
    
        raw = raw
        
    else:
    
        print('\033[1;31m[-]\033[0m Unknown error.')
        return False
        
    inp = raw


    if inputformat == 'base64':
    
        iput = base64.b64decode(inp)
    
    elif inputformat == 'base32':
    
        iput = base64.b32decode(inp)
    
    elif inputformat == 'base16':
    
        iput = base64.b16decode(inp)
    
    elif inputformat == 'base58':
    
        iput = base58.b58decode(inp)
    
    elif inputformat == 'base85':
    
        print('\033[1;31m[-]\033[0m Option not available yet')
    
    elif inputformat == 'hex':
    
        iput = inp.decode('hex')
    
    elif inputformat == 'dec':
    
        print('\033[1;31m[-]\033[0m Option not available yet')
    
    elif inputformat == 'octal':
    
        print('\033[1;31m[-]\033[0m Option not available yet')
    
    elif inputformat == 'binary':
    
        iput = text_from_bits(inp)
        
    else:
    
        print('\033[1;31m[-]\033[0m Unknown error.')
        return False
    
    iput = pad(iput)
    e = Twofish(key)
    out = e.encrypt(iput)
        
        
        
    if outputformat == 'base64':
    
        output = base64.b64encode(out)
        
    elif outputformat == 'raw':
    
        output = out
    
    elif outputformat == 'base32':
    
        output = base64.b32encode(out)
    
    elif outputformat == 'base16':
    
        output = base64.b16encode(out)
    
    elif outputformat == 'base58':
    
        output = base58.b58encode(out)
    
    elif outputformat == 'base85':
    
        print('\033[1;31m[-]\033[0m Option not available yet')
    
    elif outputformat == 'hex':
    
        output = out.encode('hex')
    
    elif outputformat == 'dec':
    
        print('\033[1;31m[-]\033[0m Option not available yet')
    
    elif outputformat == 'octal':
    
        print('\033[1;31m[-]\033[0m Option not available yet')
    
    elif outputformat == 'binary':
    
        output = text_to_bits(out)
        
    else:
    
        print('\033[1;31m[-]\033[0m Unknown error.')
        return False
        

    if export == 'file':
    
        f = open(outfilepath, 'w')
        f.write(output)
        f.close()
        return True
        
    elif export == 'print':
    
        return output
        
    else:
    
        print('\033[1;31m[-]\033[0m Unknown error.')
        return False
        


def decrypttwofish(importx, filepath, export, expfilepath, inputformat, passwd, raw, keyimport):

    if keyimport == 'base64':
    
        key = base64.b64decode(passwd)
        
    elif keyimport == 'raw':
    
        key = passwd 
    
    elif keyimport == 'base32':
    
        key = base64.b32decode(passwd)
    
    elif keyimport == 'base16':
    
        key = base64.b16decode(passwd)
    
    elif keyimport == 'base58':
    
        key = base58.b58decode(passwd)
    
    elif keyimport == 'base85':
    
        print('\033[1;31m[-]\033[0m Option not available yet')
    
    elif keyimport == 'hex':
    
        key = passwd.decode('hex')
    
    elif keyimport == 'dec':
    
        print('\033[1;31m[-]\033[0m Option not available yet')
    
    elif keyimport == 'octal':
    
        print('\033[1;31m[-]\033[0m Option not available yet')
    
    elif keyimport == 'binary':
    
        key = text_from_bits(passwd)
        
    else:
    
        print('\033[1;31m[-]\033[0m Unknown error.')
        return False
        

    if importx == 'file':
    
        f = open(impfilepath, 'r')
        raw = f.read()
        f.close()
        
    elif importx == 'print':
    
        raw = raw
        
    else:
    
        print('\033[1;31m[-]\033[0m Unknown error.')
        return False
        
    inp = raw


    if inputformat == 'base64':
    
        iput = base64.b64decode(inp)
    
    elif inputformat == 'base32':
    
        iput = base64.b32decode(inp)
    
    elif inputformat == 'base16':
    
        iput = base64.b16decode(inp)
    
    elif inputformat == 'base58':
    
        iput = base58.b58decode(inp)
    
    elif inputformat == 'base85':
    
        print('\033[1;31m[-]\033[0m Option not available yet')
    
    elif inputformat == 'hex':
    
        iput = inp.decode('hex')
    
    elif inputformat == 'dec':
    
        print('\033[1;31m[-]\033[0m Option not available yet')
    
    elif inputformat == 'octal':
    
        print('\033[1;31m[-]\033[0m Option not available yet')
    
    elif inputformat == 'binary':
    
        iput = text_from_bits(inp)
        
    else:
    
        print('\033[1;31m[-]\033[0m Unknown error.')
        return False
        
    e = Twofish(key)
    out = e.decrypt(iput)
    
    out = unpad(out)
        
        
        
    if outputformat == 'base64':
    
        output = base64.b64encode(out)
        
    elif outputformat == 'raw':
    
        output = out
    
    elif outputformat == 'base32':
    
        output = base64.b32encode(out)
    
    elif outputformat == 'base16':
    
        output = base64.b16encode(out)
    
    elif outputformat == 'base58':
    
        output = base58.b58encode(out)
    
    elif outputformat == 'base85':
    
        print('\033[1;31m[-]\033[0m Option not available yet')
    
    elif outputformat == 'hex':
    
        output = out.encode('hex')
    
    elif outputformat == 'dec':
    
        print('\033[1;31m[-]\033[0m Option not available yet')
    
    elif outputformat == 'octal':
    
        print('\033[1;31m[-]\033[0m Option not available yet')
    
    elif outputformat == 'binary':
    
        output = text_to_bits(out)
        
    else:
    
        print('\033[1;31m[-]\033[0m Unknown error.')
        return False
        

    if export == 'file':
    
        f = open(outfilepath, 'w')
        f.write(output)
        f.close()
        return True
        
    elif export == 'print':
    
        return output
        
    else:
    
        print('\033[1;31m[-]\033[0m Unknown error.')
        return False
    
         
    


