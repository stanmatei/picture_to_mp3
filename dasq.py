
from pydub import AudioSegment
from pydub.playback import play
import io
import os
import binascii
import PIL
import math
from PIL import Image
from PIL.ImageEnhance import Color
import base64
import codecs

song = open("yoy.mp3", "rb")
# value = bin(int(binascii.hexlify(song.read()), 16))[2:]
zoink = binascii.hexlify(song.read())
songtxt = str(zoink)
l = len(songtxt)
n = math.ceil(math.sqrt(l))
"""
foli = open("hopa.txt", "w")
im=Image.open("gool.tif", "r")
finna=open("hopa.txt", "a")
width,height =im.size
i = 0
j = 0
k = 2
n = height
pixels=im.load()
pixel=pixels[i,j]
o = str(hex(pixel[0]))
while i < n:
    j=0
    while j < n:
        pixel=pixels[i,j]
        o=str(hex(pixel[0]))
        print(o[2])
        
        j += 1
        finna.write(o[2])
        k+=1
        if k>=l-1:
            break
    if k>=l-1:
        break

    i += 1

o = str(hex(pixel[0]))
print(str(j)+" --> " +str(len(o)))
pixel=pixels[0,1]

#finna.write("'")
"""

AudioSegment.converter=r"C:\ffmpeg\bin\ffmpeg.exe"
data = open(r'C:\Users\Matei\Desktop\songzx\yoy.mp3', 'rb').read()
data2 = open(r'C:\Users\Matei\Desktop\songzx\koss.mp3', 'rb').read()
ror=open("ror.txt","w")
ror.write(str(data))
fof=open("ror.txt","rb").read()



# pick sound file you have in working directory
# or give full path
sound_file = "yoy.mp3"
# use mode = "rb" to read binary file
fin = open(sound_file, "rb")
binary_data = fin.read()
fin.close()
hex_string=open("hopa2.txt","r").read()
# encode binary to base64 string (printable)
#result = codecs.encode(codecs.decode(hex_string, 'hex'), 'base64').decode()
#result = b2a_base64(bytes.fromhex(hex_string))
b64_data = base64.b64encode(bytes.fromhex(hex_string))
#b64_data = base64.b64encode(result)
b64_fname = "original_b64.txt"
# save base64 string to given text file
fout = open(b64_fname, "wb")
fout.write(b64_data)
fout.close()
# read base64 string back in
fin = open(b64_fname, "r")
b64_str = fin.read()
fin.close()
# decode base64 string to original binary sound object
mp3_data = base64.b64decode(b64_str)
song = AudioSegment.from_file(io.BytesIO(mp3_data), format="mp3")
play(song)
