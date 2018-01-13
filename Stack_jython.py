# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from java.util import Stack
a = Stack()
for  k in range(10):
	a.push(k)
print (a.search(7))
print (a.peek())
print (a.pop())
print (type(a))
print (a)
