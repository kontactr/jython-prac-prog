from java.lang import *
from java.security import Key
from javax.crypto import Cipher
from javax.crypto import KeyGenerator
from array import array
#must import for dec it is user made file
from dec_file import dec



algo = "RC2"
key = KeyGenerator.getInstance(algo).generateKey()
cipher = Cipher.getInstance(algo)

def enc(text,key,cipher):
	cipher.init(Cipher.ENCRYPT_MODE,key)
	#string = ""
	#for l in text:
	#	string += 
	return  cipher.doFinal(array("b",text.encode("utf-8")))
	#return string

#def dec(byar,key,cipher):
#	cipher.init("Cipher.DECRYPT_MODE,key)
#	print (cipher.doFinal(byar))
	
#key = KeyGenerator.getInstance(algo).generateKey()
#cipher = Cipher.getInstance(algo)
print ("plain-text - hello world")
x = enc("hello world",key,cipher)
print ("cipher-text - ")
print (x)
print ("decrypt-text - ")
print (dec(x,key,cipher))
