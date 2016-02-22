"""
stringjumble.py
Author: Mary Feyrer
Credit: Tess Snyder, Daniel Wilson

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""

text = input("Please enter a string of text (the bigger the better): ")
n = len(text)

print("\n") 

for x in range(-1,-n-1, -1):
    print(text[x], end="")

print("\n") 

words=text.split(' ')
list2=reversed(words)
for x in list2:
    print(x, end=" ")
    
print("\n") 

for x in words:
    g=0
    while g < n:
        w=str(x[n-g-1])
        print("{0}".format(w), end" ")
    print(" ", end" ")






