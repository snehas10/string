"""4.

Find All Characters with Maximum Frequency
Website Traffic Analysis System

A web analytics company tracks user activity symbols in server logs.

The company wants to identify all characters having the maximum frequency in the given string.

Input:
aabbbccddd
Output:
b d"""
n=input("enter string=")

max=0
i=0
while i<len(n):
    count=0
    j=0
    while j<len(n):
            if n[i]==n[j] and n[i]!=" ":
                count=count+1
            j=j+1
    if count>max:
        max=count
        
    i=i+1
i=0
while i<len(n):
    count=0
    j=0
    while j<len(n):
        if n[i] == n[j] and n[i] != " ":
            count=count+1
        j=j+1
    if count==max:
        k=0
        f=0
        while k<i:
            if n[i]==n[k]:
                  f=1
                  break
            k=k+1
        if f==0:
             print(n[i],end=" ")                 
    i=i+1  


