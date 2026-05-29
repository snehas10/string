"""4.
Palindrome Number List Checker
Scenario

A system checks lucky numbers which are palindromes.

Requirements
Check palindrome numbers
Store palindrome numbers in list
Count palindrome numbers
Find largest palindrome
Sort palindrome list
Test Cases

Input:
[121, 131, 20, 44, 55, 100]

Output:

Palindromes: [121, 131, 44, 55]
Count: 4
Largest: 131
Sorted: [44, 55, 121, 131]
"""
n=int(input("enter number of list = "))
arr=[]
for i in range(n):
    x=int(input("enter numbers = "))
    arr.append(x)
print(arr)

count=0
rev=[]
for i in range(len(arr)):
    num=arr[i]
    temp=num
    rever=0
    
    while num>0:
        rem=num%10
        rever=rever*10+rem
        num=num//10
    if rever==temp: 
        rev.append(rever)
        count=count+1
print("Palindrome = ",rev)           
print("count = ",count)
ma=0
for i in rev:
     if i>ma:
         ma=i
print("highest = ",ma)  
rev.sort()
print("Sorted list = ",rev)       