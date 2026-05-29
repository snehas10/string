"""7.
Factory Production – Factorial Expansion List

Problem Statement

A factory produces items where production capacity is defined using factorial growth.

Given a list of numbers, replace each number with its factorial value.

Then perform analysis on the resulting list.

Tasks:

Convert each element to factorial
Find sum of all factorial values
Find maximum factorial value
Count how many factorial values are even

Input:
A list of integers

Example 1

Input:
[3, 4, 5]

Processing:
3! = 6
4! = 24
5! = 120

Output:
[6, 24, 120]
Sum = 150
Max = 120
Even Count = 3"""

n=int(input("enter number of list = "))
arr=[]
for i in range(n):
    x=int(input("enter numbers = "))
    arr.append(x)
print(arr)
ls=[]

for i in arr:
    fac=1

    for j in range(1, i+1):
        fac=fac*j

    ls.append(fac)     
print("factorial List = ",ls)    
sum=0
ma=0
count=0
for i in ls:
    sum=sum+i
    if ma<i:
        ma=i
    if i%2==0:
        count=count+1  
print("Sum = ",sum)
print("Max =",ma)
print("even count = ",count)