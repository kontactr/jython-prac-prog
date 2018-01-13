#use for fraction
from fractions import Fraction

#use for decimal calculations float gives you approximate result
from decimal import Decimal 

def fraction(a,b):
    try:
        return Fraction(int(a),int(b))
    except Exception as e:
        return e

def decimal(num):
    try:
        if isinstance(num,float):
            return Decimal(str(num))
        else:
            return Decimal(num)
    except Exception as e:
        return e

def enc(st,format="utf-8"):
    try:
        return st.encode(str(format))
    except Exception as e:
        return e

def dec(st,format="utf-8"):
    try:
        return st.decode(str(format))
    except Exception as e:
        return e
    
def con_bytes(st,format="utf-8"):
    try:
        return bytes(st,format)
    except Exception as e:
        return e
