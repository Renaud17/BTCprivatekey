#source https://asecuritysite.com/encryption/bitc  https://www.linkedin.com/pulse/please-pay-1billbitcoin-beauty-bitcoins-vanity-prof-bill/  https://medium.com/coinmonks/having-fun-with-bitcoins-vanity-bitcoin-address-generation-fea28f855173

# Edited by @Searphimjm - Added Hex Secret Exponent, Wif, Compressed address, multiprocessing & seekaddr. edited vanity & code comments
import random
import bit
import ecdsa
import hashlib
import multiprocessing
from multiprocessing import Pool
import time
from ecdsa.util import string_to_number, number_to_string
from bitcoin import *
hex_list=[0,1,2,3,4,5,6,7,8,9]
# secp256k1
_p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
_r = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
_b = 0x0000000000000000000000000000000000000000000000000000000000000007
_a = 0x0000000000000000000000000000000000000000000000000000000000000000
_Gx = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
_Gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
curve_secp256k1 = ecdsa.ellipticcurve.CurveFp(_p, _a, _b)
generator_secp256k1 = ecdsa.ellipticcurve.Point(curve_secp256k1, _Gx, _Gy, _r)
oid_secp256k1 = (1, 3, 132, 0, 10)
SECP256k1 = ecdsa.curves.Curve("SECP256k1", curve_secp256k1, generator_secp256k1, oid_secp256k1)
ec_order = _r
curve = curve_secp256k1
generator = generator_secp256k1

seekaddr = '1GDWUJyvtsyFKNjBvH6hpLE3CdaXx33dxP' #Mainly seeks this address, script will run until it finds an exact match & will then stop.  Addresses matching vanity specified in variable "seq" will be printed onscreeen


def get_key(privkey,search_for):
    address = 'vanity' #do not change this with the expectation of a related result as it is constantly overwritten
    while not search_for in address:
        privkey += 1
        pubkey_point =fast_multiply(G, privkey)
        address = pubkey_to_address(pubkey_point)
        #print (address[:10], end=" ") #this prints alot of stuff onscreen, if you enable this one disable the one below.
        #print ('\r' + address[:10], end=" ")
    return address,privkey


def multip(hex_list):	
     #SEQ can be any part of the "seekaddr" or any other vanity address when searching for mutiple matching addresses.  This prints onscreen, any address encountered which has a match at any position of any address encountered during the search for "seekaddr"
    seq="SSS"
    address = seq
    if (len(sys.argv)>1):
        seq=str(sys.argv[1])
    privkey = random.randrange(2**256)
    print ("Initializing search ...", privkey)
    while not seekaddr in address:
     address,privkey=get_key(privkey,seq)


     privx = bit.Key.from_int(privkey)
   
     if (address==0):
        print ("Could not find sequence. Need a cluster!")
     else:
        print ("\n\n        Vanity Found - matching ", seq)
        print (" Public Bitcoin address is",address, "\n Secret Exponent in Decimal:",privkey, "\n Secret Exponent:",hex(privkey)[2:], "\n Compressed WIF is:",privx.to_wif(), "\n Compressed Address:",privx.address, "\n\n")
        # U/C Priv & Addresses can be found using only Secret Exponent on https://brainwalletx.github.io/#generator
    
    
if __name__ == '__main__':
    p = Pool(processes = 10) #set to 1 or 2 less than your max cpu cores
    start = time.time()
    async_result = p.map_async(multip, hex_list)
    p.close()
    p.join()
    print("Complete")
    end = time.time()
    print('total time (s)= ' + str(end-start))
    print('Finished')
