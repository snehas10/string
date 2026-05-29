"""1.Student Marks Management
Create a program to store student marks in a List and perform operations.

Requirements:

Add student marks into a List
Display all marks
Find highest and lowest marks
Count students who scored above 75

Test Cases:

Input: [45, 67, 89, 90, 76] → Highest = 90, Lowest = 45, Count Above 75 = 3
Input: [10, 20, 30] → Highest = 30, Lowest = 10, Count Above 75 = 0
Input: [100, 99, 98] → Highest = 100, Lowest = 98, Count Above 75 = 3"""
n=int(input("enter number of list = "))
arr=[]
for i in range(n):
    x=int(input("enter marks of student = "))
    arr.append(x)
print(arr) 
  

high=arr[0]
low=arr[0]

for i in range(1, len(arr)):
    if arr[i]>high:
        high=arr[i]  
    if arr[i]<low:
        low=arr[i]
print("highest = ",high)         
print("lowest = ",low)        

count=0
for i in arr:
    if i > 75:
        count=count+1

print("count",count)    



