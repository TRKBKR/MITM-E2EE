import requests,binascii,time
from Crypto.PublicKey import RSA
from urllib.parse import unquote as un
################################## Hexer #######################
def bin2hex(binStr):
        return binascii.hexlify(binStr)

def hex2bin(hexStr):
        return binascii.unhexlify(hexStr)
################################################################
    
binPubKey =  open('clientb.pub').read()

################################## Algo ########################
def algo(type,binPubKey,msg):
    #key = RSA.generate(2048)
    binPrivKey = hex2bin(open('clientb').read())#key.exportKey('DER')
    #key.publickey().exportKey('DER')
    privKeyObj = RSA.importKey(binPrivKey)
    pubKeyObj =  RSA.importKey(binPubKey)
    if type == "enc":
        return pubKeyObj.encrypt(msg.encode('utf-8'), 'x')[0]
    if type == "dec":
        return privKeyObj.decrypt(msg)
#################################################################

def serConn():
    print('Cheking Pub Key ...')
    pub=requests.get('http://127.0.0.1:8000/data/clientb.pub')
    if requests.get('http://127.0.0.1:8000/data/clienta.pub').status_code == 404:
        requests.post('http://127.0.0.1:8000/data/clienta.pub',data={'pub':open('clientb.pub','r').read()})
        print('Pub Key Sent...')

    if pub.status_code == 200:
        binPubKey=hex2bin(pub.text)
        print('Pub Key Found Decrypting ...')
        def con():
                d=str(input("send ==>: "))
                encmsg=bin2hex(algo('enc',binPubKey,d))
                requests.post('http://127.0.0.1:8000/data/msga',data={'sad':encmsg})
                
                emsg=hex2bin(un(requests.get('http://127.0.0.1:8000/data/msgb').text))
                print(algo('dec',binPubKey,emsg))
                con()
        con()
    else:
        print('Waitng 2 Sec ...')
        time.sleep(2)
        serConn()
        
serConn()
