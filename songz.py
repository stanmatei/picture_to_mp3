import binascii
import PIL
import math
from PIL import Image
from PIL.ImageEnhance import Color

song = open("yoy.mp3", "rb")
# value = bin(int(binascii.hexlify(song.read()), 16))[2:]
zoink = binascii.hexlify(song.read())
songtxt = str(zoink)
values=open("values.txt","a")
l = len(songtxt)
n = math.ceil(math.sqrt(l))
# foli = open("foliop.txt", "w")
# foli.write(str(zoink))
#mode = 'RGB'
#size = (n, n)
r1 = int(songtxt[5] + songtxt[5], 16)
g1 = int(songtxt[5] + songtxt[5], 16)
b1 = int(songtxt[5] + songtxt[5], 16)
color = (r1, g1, r1)
im = Image.new('RGB', [n, n], (255,0,0))
i = 0
j = 0
k = 2
pixels=im.load()

while i < n:
    j=0
    while j < n:

        ipix = im.getpixel((i, j))
        myColor=("0x"+songtxt[k],"0x"+songtxt[k],"0x"+songtxt[k])
        r = int(songtxt[k] + songtxt[k], 16)
        g = int(songtxt[k] + songtxt[k], 16)
        b = int(songtxt[k] + songtxt[k], 16)

        pixels[i,j]=(r,g,b)

        values.write(str(i)+" "+ str(j) + "  -----> "+ str(r) +" -----> k = " +str(k)+"\n")
        print(str(i)+" "+ str(j) + "  -----> "+ str(r))
        j += 1
        k+=1
        if k>=l-1:
            break
    if k>=l-1:
        break

    i += 1

im.save("gool.tif")
