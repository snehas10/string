"""5.
Cybercrime Log Analysis System

A cybersecurity company monitors encrypted login activity stored as character-based security logs.

During investigation, analysts need to identify the last character that repeats in the log sequence.
This helps detect the most recent duplicated activity pattern before a possible security breach.

Write a Python program to find the last repeating character in a given string.

If no repeating character exists, print:

No repeating character found
Input:
abccdbefga
Output:
a"""
n=input("Enter string = ")

f=0
for i in range(len(n)-1, -1, -1):
    count=0
    for j in range(len(n)-1, -1, -1):
        if n[i]==n[j]:
            count=count+1
    if count<len(n):
        print("output =",n[i])
        f=1
        break

if f==0:
    print("No repeating string") 