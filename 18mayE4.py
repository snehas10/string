"""
4.
Employee ID Validator

A company wants to validate employee IDs before storing them in the database.

Conditions:
- ID must start with "EMP"
- Total length should be 8
- Remaining characters should be digits only

Input:
Enter Employee ID: EMP10234

Output:
Valid Employee ID
"""
n=input("enter a num = ")
f=1
if n[0:3]=="EMP" and len(n)==8:
    for i in n[3:]:
        if i<'0' or i>'9':
           f=0
           break
else:
    f=0
            
if f==1:
    print("valid employeee ID")
else:
    print("Invalid enployee ID ")
