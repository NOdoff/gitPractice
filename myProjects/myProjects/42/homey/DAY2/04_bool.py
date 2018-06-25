#!/usr/bin/env python
import random
array1 = [False, True, True, None, True, None, None, False, False, None, True, False]
array2 = ["or", "or", "or", "==", "!=", "==", "and", "==", "!=", "and", "!=", "and"]
array3 = [False, False, None, None, True, True, False, True, None, False, True, None]
x = 0
while x < 10:
	i = random.randint(0, len(array1) - 1)
	j = random.randint(0, len(array2) - 1)
	k = random.randint(0, len(array3) - 1)
	if array2[j] == "or":
		print(str(array1[i]) + " or " + str(array3[k]) + " => " + str(array1[i] or array3[k]))
	elif array2[j] == "==":
		print(str(array1[i]) + " == " + str(array3[k]) + " => " + str(array1[i] is array3[k]))
	elif array2[j] == "!=":
		print(str(array1[i]) + " != " + str(array3[k]) + " => " + str(array1[i] is not array3[k]))
	elif array2[j] == "and":
		print(str(array1[i]) + " and " + str(array3[k]) + " => " + str(array1[i] and array3[k]))
	x = x + 1
