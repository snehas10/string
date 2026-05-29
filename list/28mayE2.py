"""2.Employee Salary Processing
Store employee salaries in a List and calculate details.

Requirements:

Store salaries
Find average salary
Display salaries greater than average
Remove salaries below 15000

Test Cases:

Input: [10000, 20000, 30000] → Average = 20000, Above Average = 30000
Input: [15000, 15000, 15000] → Average = 15000
Input: [5000, 7000] → Remaining List = []"""
n=int(input("enter number of list = "))
arr=[]
for i in range(n):
    x=int(input("enter salary student = "))
    arr.append(x)
print(arr) 

sum=0  
for i in arr:
    sum=sum+i
       
av=sum/n
print("avg=",av)
above=[]
for i in arr:
    if i>15000 and i>av:
        above.append(i)
print("above Average = ",above)        



      
