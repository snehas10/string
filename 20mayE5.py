"""
5. Find the Number of Unique Characters in a String

Password Strength Analyzer

A cybersecurity company checks password strength based on the number of unique characters present.

Passwords containing more unique characters are considered more secure.

Write a Python program to count the number of unique characters in a string.

Input: aabbccdde
Output: 5
"""
s=input("enter a string = ")
i=0
count=0
while i<len(s):
    f=0
    j=0
    while j<i:
        if s[i]==s[j]:
            f=1
            break
        j=j+1
    if f==0:
        count=count+1    
            
    i=i+1 
print(count)          