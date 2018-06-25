#!/usr/bin/env python
import sys
array = sys.argv
a = int(array[1])
b = int(array[2])
divide = divmod(a, b)
x, y = divide
print(str(a) + " divided by " + str(b) + " equals " + str(x) + " remainder " + str(y))
m = 12
n = 23.98
z = 43 + 65j
w = sys.maxsize

def getType(val):
	ty = str(type(val))
	ind1 = ty.find('\'')
	ind2 = ty.find('\'', ind1 + 1)
	typ = ty[ind1 + 1: ind2]
	return typ
print("Variable m contains: " + str(m) + " which is of type: " + getType(m))
print("Variable n contains: " + str(n) + " which is of type: " + getType(n))
print("Variable z contains: " + str(z) + " which is of type: " + getType(z))
print("Variable w contains: " + str(w) + " which is of type: " + getType(w))

