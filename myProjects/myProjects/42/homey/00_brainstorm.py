#!/usr/bin/env python
categ = ["Reptiles", "Vegetables", "Brands", "Technology", "Colors", "Restaurants", "Countries",  "Books", "Shops", "Plants", "Emotions", "School Subjects", "Cartoons", "Clothes", "Holidays", "Fruits", "Holidays"]

from random import randint
import os
import time
width = os.get_terminal_size().columns
print (width)
print("Hello, vizitor! Welcome to Pycategories! Write ten words that relate to the category '" + categ[randint(0, len(categ) - 1)] + "':")
i = 0
answers = []
start = time.time()
while i < 10:
	answer = input()
	answers.append(answer)
	i = i + 1
end = time.time()
elapsed = end - start
print(time.strftime("%H:%M:%S", time.gmtime(elapsed)))
print("+ -------------------------------------------------------------------------------------------------- +".center(width))
print("|" + "YOUR ANSWERS ARE:".center(width) + "|")
print("|" + " ".center(width) + "|")
for l in answers:
	print("|" + l.center(width) + "|")
	print("|" + " ".center(width) + "|")
print("+ -------------------------------------------------------------------------------------------------- +".center(width))