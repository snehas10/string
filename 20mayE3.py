"""
3. Find the First Non-Repeated Character

Railway Ticket Fraud Detection System

The railway department generates ticket reference IDs automatically.

Sometimes, due to technical issues, many characters get repeated inside the ticket ID.

The department wants a Python program that finds the first character that appears only once in the string.

Example 1

Input:
aabbccddefg
Output: e
"""
n=input("Enter string = ")
i=0
f=0
while i<len(n):
    count=0
    for j in range(0, len(n)):
        if n[i]==n[j]:
            count=count+1
    if count==1:
        print("output =",n[i])
        f=1
        break
    i=i+1
if f==0:
    print("No unique string")         

