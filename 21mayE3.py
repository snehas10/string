"""3.
Replace Consecutive Duplicate Characters with Single Character
Data Compression System

A cloud storage company wants to reduce unnecessary repeated characters in text logs.

Write a Python program that replaces consecutive duplicate characters with a single occurrence.

Input:
aaabbbccccdddaa
Output:
abcda
"""
n=input("enter string= ")
rev=""
i=0
while i<len(n):
        if i==0 or n[i]!=n[i-1]:
            print(n[i],end="")    
        i=i+1
