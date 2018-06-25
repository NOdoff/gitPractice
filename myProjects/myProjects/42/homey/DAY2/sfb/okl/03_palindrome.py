#!/usr/bin/env/ python
import re
def is_palindrome(text):
    cont = [char for char in text.lower() if char.isalnum()]
    return cont == cont[::-1]

text = input("Hello, guys! Let's check if your input is a polyndrome. Please, enter the text on the next line:\n") 
if is_palindrome(text):
    print("Wow! This input IS really a polyndrome!")
else:
    print("This input ISN'T a polydrome, but do not worry you can try again!")
