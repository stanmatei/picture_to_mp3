
import binascii
import PIL
import math
from PIL import Image
from PIL.ImageEnhance import Color

song = open("yoy.mp3", "rb")
# value = bin(int(binascii.hexlify(song.read()), 16))[2:]
zoink = binascii.hexlify(song.read())
songtxt = str(zoink)
l = len(songtxt)
n = math.ceil(math.sqrt(l))
# foli = open("foliop.txt", "w")
# foli.write(str(zoink))
im=Image.open("gool.tif", "r")
#finna=open("hopa.txt", "w")
#finna.append("b'")
i = 0
j = 0
k = 2
"""
while i < n and k < l - 1:
    j=0
    while j < n and k < l - 1:
        ipix = im.getpixel((i, j))
        ipix.getC
        j+=1
        print(str(i)+" "+ str(j) +)
        k+=1

    i += 1
im.save("gool.jpg")
"""
pxl=im.load()
pixel=pxl[0,0]
o = str(hex(pixel[0]))
print(o[2])



