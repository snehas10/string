"""
8.
Find the Second Highest Repeating Character in a String

Social Media Trend Analysis System

A social media company analyzes hashtags and user comments to identify trending character patterns.

The analytics team wants a Python program to find the character with the second highest frequency in a given string.

This helps detect secondary trending patterns in user activity.

Input: aaabbbbccddeee

Output: e
Explanation:
b occurs 4 times → highest
e occurs 3 times → second highest
Condition:
Program should work for both uppercase and lowercase letters.
Spaces should be ignored.
If no second highest frequency exists, print:
Second highest repeating character not found"""

n=input("Enter string = ")
i=0
max1=0
max2=0
ch1=""
ch2=""

while i<len(n):
    count=0
    for j in range(0, len(n)):
        if n[i]==n[j] and n[i]!=" ":
           count=count+1
    if count>max1:

        max2=max1
        ch2=ch1

        max1=count
        ch1=n[i]

    elif count>max2 and count!=max1:

        max2=count
        ch2=n[i]

    i=i+1   
if max2==0:
    print("Second highest frequency not found = ")
else:
    print("Second highest fre =",ch2)
    print("fre=",max2)    

       