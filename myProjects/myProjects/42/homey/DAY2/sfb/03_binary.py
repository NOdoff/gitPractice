#!/usr/bin/env python
import sys
array = sys.argv
decimal = int(array[1])
binary = bin(decimal)
octal = oct(decimal)
hexa = hex(decimal)
print(binary)
print(octal)
print(hexa)