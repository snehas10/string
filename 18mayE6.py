"""
6.

Product Code Verification System

An e-commerce company wants to verify whether two product codes are rearranged versions of each other.

Conditions:
- Ignore spaces
- Ignore case sensitivity

Input:
Enter first product code: Dormitory
Enter second product code: Dirty Room

Output:
Both Product Codes are Matching"""
n1=input("enter first product code:")
n2=input("enter second product code:")
f=1
for ch in n1:
    if ch==" ":
          continue
    if n1.count(ch)!=n2.count(ch):
           f=0
           break
if f==1:
    print("both Product codes are matching")        
else:
    print("Not both product match")
