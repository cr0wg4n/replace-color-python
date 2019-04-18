
import os
os.system("mkdir ./cuts")
archivos = os.listdir("./")
for x in range(0,len(archivos)):
	cadena=str(archivos[x])
	cadena=cadena.replace(" ","\ ")
	if cadena[-3:]=="JPG" or cadena[-3:]=="jpg" or cadena[-3:]=="png" or cadena[-3:]=="PNG" or cadena[-4:]=="JPEG" or cadena[-4:]=="jpeg":
		os.system("python rem-color.py "+cadena)

