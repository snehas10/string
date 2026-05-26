"""5.
Advanced Password Security Checker

A cyber security company wants to verify whether employee passwords are highly secure before giving system access.

Conditions: Password must:

Start with an uppercase letter
End with a digit
Contain at least 2 digits
Contain at least 1 special character (@ # $ % & *)
Must not contain spaces
Length should be between 8 and 15 characters

Input: Enter password: Python@45

Output: Secure Password

"""
n=input("Enter password:")
count=0
upper=0
lower=0
digit=0
space=0
special=0
for i in range(len(n)):
    ch=n[i]
    if len(n)>=8 and len(n)<=15:
        if ch>="A" and ch<="Z" and ch.startswith(ch):
            upper=1
        elif ch>="a" and ch<="z":
            lower=1
        elif ch>="0" and ch<="9" and ch.isdigit():
            digit=1
        elif ch==" ":
            space=1
        else:
            special=1        

if upper==1 and lower==1 and digit==1 and space==0 and special==1:
    print("Secured passwrod")
else:
    print("unsecured password")
    
