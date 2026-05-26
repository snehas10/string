"""
1.
Email Username Validator

A company wants to check whether an employee email username is valid before creating an official account.

Conditions:
- Username should start with a letter
- Username can contain letters, digits, underscore (_)
- No spaces allowed
- Length should be between 5 and 12 characters

Input:
Enter username: ajay_123

Output:
Valid Username

"""
n=input("Enter username = ")
dig=0
under=0
spa=0
d=0
digit=0

for i in n:
    if len(n)>=5 and len(n)<=12:
        d=1
    if i[0]>="a" and i[0]<="z":
        dig=1
    if i=="_":
        under=1
    if i==" ":
        spa=1
    else:
        digit=1
if d==1 and dig==1 and digit==1 and under==1 and spa==0:
    print("valid Username")
else:
    print("Invalid Username")