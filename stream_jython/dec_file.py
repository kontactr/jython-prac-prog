
from  java.security import Key
from  javax.crypto import Cipher;
from  javax.crypto import KeyGenerator
from  java.lang import String

def dec(byar,key,cipher):
	cipher.init(Cipher.DECRYPT_MODE,key)
#	p = len(byar) % 8
#	while p!=0:
#		byar.append(0)
#		p-=1
	return String(cipher.doFinal(byar))
