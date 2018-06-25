#!/usr/bin/env python
import sys
array = sys.argv
for i in range(0,len(array) - 1):
	print("Argv of " + str(i) + " is " + array[i])
sorted_array = sorted(array, key = len)
reversed_array = list(reversed(sorted_array))
for i in range(0, len(array - 1)):
	print(reversed_array[i])