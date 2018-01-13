# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from java.io import BufferedOutputStream as BO
from java.io import BufferedInputStream  as BI
from java.io import FileInputStream	as FI
from java.io import FileOutputStream as FO

f_read = FI("file1.txt")
b_read = BI(f_read)

f_write = FO("file2.txt")
b_write = BO(f_write)

while True:
	ch = b_read.read()
	if ch != -1:
		b_write.write(ch)
	else:
		break

b_read.close()
f_read.close()
b_write.close()
f_write.close()