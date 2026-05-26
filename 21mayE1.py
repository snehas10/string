"""1.
Find the Longest Substring Without Repeating Characters
Cybersecurity Session Tracking System

A cybersecurity company monitors user session IDs generated during secure login sessions.

To detect suspicious repeated patterns, the company wants a Python program that finds the longest substring containing no repeated characters.

Input:
abcabcbb
Output:
abc

s=input("enter a string = ")
i=0
count=0
rev=""
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
        rev=rev+s[i]   
            
    i=i+1 
print(rev)"""

a=input("enter a string = ")
r=""
h=""
i=0
while i<len(a):
    if a[i] not in r:
        r=r+a[i]
    else:
        if len(r)>len(h):
            h=r
            e=(i-len(r))+r.index(a[i])
            i=e+1
            r=""
            continue
    i=i+1
if len(r)>len(h):
    print(r)
else:
    print(h)        
