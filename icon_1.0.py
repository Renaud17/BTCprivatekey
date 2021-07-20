#! python
import sys
from bitcoin import *
from datetime import datetime
from hashlib import sha256
import random

RANDOM = random.randrange(0,674453131596581044224)

addrCount = RANDOM

def nextChar(currAddr,nextPos):
    global addrCount
    if nextPos < totalChars-1:
        for x in range(len(pkeychars[nextPos])):
            currAddr += pkeychars[nextPos][x]
            nextChar(currAddr, nextPos+1)
            currAddr = currAddr[:-1]
    else:
        for x in range(len(pkeychars[nextPos])):
            currAddr += pkeychars[nextPos][x]
            addrCount += 1
            result = b58decode(currAddr)
            result, check = result[:-4], result[-4:]
            digest = sha256(sha256(result).digest()).digest()
            if check == digest[:4]:
                print('We have a possible winner!: ',currAddr)
                f.write(currAddr+'\n')
            if addrCount%1000000 == 0:
                print(str(addrCount) + ' Addresses ' + str(datetime.now()))
            
            currAddr = currAddr[:-1]

def b58decode(v):
    '''Decode a Base58 encoded string'''

    if not isinstance(v, str):
        v = v.decode('ascii')

    origlen = len(v)
    v = v.lstrip(b58_digits[0])
    newlen = len(v)

    p, acc = 1, 0
    for c in v[::-1]:
        acc += p * b58_digits.index(c)
        p *= 58

    result = []
    while acc > 0:
        acc, mod = divmod(acc, 256)
        result.append(mod)

    return (bseq(result) + b'\0' * (origlen - newlen))[::-1]

if bytes == str:  # python2
    iseq = lambda s: map(ord, s)
    bseq = lambda s: ''.join(map(chr, s))
    buffer = lambda s: s
else:  # python3
    iseq = lambda s: s
    bseq = bytes
    buffer = lambda s: s.buffer

pkeychars = []

pkeychar0 = ['5']
pkeychar1 = ['J','H','K',] #UPPERCASE lightGreen #Jobs
pkeychar2 = ['K','k','Z','z'] #Kevlar
pkeychar3 = ['P'] #UPPERCASE lightGreen #Pi
pkeychar4 = ['1','2','3','4','5','6','7','8','9','a','A'] #Atari
pkeychar5 = ['p'] #lowercase BLUE #Parachute
pkeychar6 = ['j','J'] #Jet
pkeychar7 = ['w','W'] #Wingtip??
pkeychar8 = ['g','G'] #Gutenberg
pkeychar9 = ['y'] #lowercase BLUE #yoyo
pkeychar10 = ['E'] #UPPERCASE lightGreen # mc^2 = E
pkeychar11 = ['i'] #lowercase BLUE #iron
pkeychar12 = ['j','p','J','P'] #jigsaw puzzle
pkeychar13 = ['3'] #UPPERCASE lightGreen  #Morse code date
pkeychar14 = ['s','S'] #scissors
pkeychar15 = ['x'] #lowercase BLUE #xray
pkeychar16 = ['Y'] #UPPERCASE lightGreen #Yale
pkeychar17 = ['r','R'] #radar
pkeychar18 = ['C','A'] #UPPERCASE lightGreen #concertina/aspirin?
pkeychar19 = ['e','E'] #Eiffel Tower
pkeychar20 = ['n','N'] #Nobel
pkeychar21 = ['i','s'] #lowercase BLUE #ice skate
pkeychar22 = ['x','X'] #XX
pkeychar23 = ['y','Y'] #XY
pkeychar24 = ['i'] #lowercase BLUE #igloo
pkeychar25 = ['f','F','n','N'] #negatives? film?
pkeychar26 = ['g','G'] #Galileo
pkeychar27 = ['x','X'] #Xerox
pkeychar28 = ['q','Q'] #Question
pkeychar29 = ['k'] #lowercase BLUE #NaKamoto
pkeychar30 = ['V','E'] #UPPERCASE lightGreen #E-cig - Vaporiser
pkeychar31 = ['h','H'] #SatosHi
pkeychar32 = ['g','p','G','P'] #Phonograph, Gramophone
pkeychar33 = ['Z'] #UPPERCASE lightGreen #zipper
pkeychar34 = ['x','X'] #alphabet X
pkeychar35 = ['v','p'] #lowercase BLUE #Pfizer- Viagra?
pkeychar36 = ['9'] #Euro - 1996
pkeychar37 = ['b','B'] #Braile for B or 2
pkeychar38 = ['W'] #UPPERCASE lightGreen #Wifi
pkeychar39 = ['W','w'] #Windows
pkeychar40 = ['k'] #lowercase BLUE #Krypton element
pkeychar41 = ['n'] #lowercase BLUE #DNA
pkeychar42 = ['B'] #UPPERCASE lightGreen #Balloon
pkeychar43 = ['e','E'] #Einstein
pkeychar44 = ['x'] #lowercase BLUE #2009 MMIX
pkeychar45 = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','J','K','L','M','N','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] #Etch a Sketch
pkeychar46 = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','J','K','L','M','N','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] #Gameboy
pkeychar47 = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','J','K','L','M','N','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] #lowercase BLUE #Xeon element
pkeychar48 = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','J','K','L','M','N','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] #1927 LED invention date or maybe 1962?
pkeychar49 = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','J','K','L','M','N','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] #Tesla
pkeychar50 = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','J','K','L','M','N','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] #Allcase #Mouse


pkeychars = [pkeychar0, pkeychar1, pkeychar2, pkeychar3, pkeychar4, pkeychar5, pkeychar6, pkeychar7, pkeychar8, pkeychar9, pkeychar10, pkeychar11, pkeychar12, pkeychar13, pkeychar14, pkeychar15, pkeychar16, pkeychar17, pkeychar18, pkeychar19, pkeychar20, pkeychar21, pkeychar22, pkeychar23, pkeychar24, pkeychar25, pkeychar26, pkeychar27, pkeychar28, pkeychar29, pkeychar30, pkeychar31, pkeychar32, pkeychar33, pkeychar34, pkeychar35, pkeychar36, pkeychar37, pkeychar38, pkeychar39, pkeychar40, pkeychar41, pkeychar42, pkeychar43, pkeychar44, pkeychar45, pkeychar46, pkeychar47, pkeychar48, pkeychar49, pkeychar50]

b58_digits = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

totalChars = len(pkeychars)
print('\n#Chars: ', totalChars)

totalKeys = 1
for x in pkeychars:
   totalKeys *= len(x)

print("Checking [" + str(totalKeys) + "] Keys...")

nextPos = 0

addr = '1GDWUJyvtsyFKNjBvH6hpLE3CdaXx33dxP'

f = open('goodKeys2.txt', 'w')

starttime = datetime.now()
print('Start: ' + str(starttime))
f.write('Start: ' + str(starttime) + '\n')

nextChar(addr, nextPos)

endtime = datetime.now()
f.write('End: ' + str(endtime) + '\n')
f.write('Total: ' + str(endtime - starttime)  + '\n')
f.close()
