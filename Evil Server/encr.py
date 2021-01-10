import requests,binascii,time
from Crypto.PublicKey import RSA
from urllib.parse import unquote as un

################################## Hexer #######################
def bin2hex(binStr):
        return binascii.hexlify(binStr)

def hex2bin(hexStr):
        return binascii.unhexlify(hexStr)
################################################################

binPubKey =  hex2bin(open('serverE.pub','r').read())

################################## Algo ########################
def algo(type,binPubKey,msg):
    #key = RSA.generate(2048)
    binPrivKey = hex2bin(open('serverE').read())#key.exportKey('DER')
    #key.publickey().exportKey('DER')
    privKeyObj = RSA.importKey(binPrivKey)
    pubKeyObj =  RSA.importKey(binPubKey)
    if type == "enc":
        return pubKeyObj.encrypt(msg, 'x')[0]
    if type == "dec":
        return privKeyObj.decrypt(msg)
#################################################################
