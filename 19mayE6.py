"""
6.
 Advanced Student Registration Data Processing System

A national university is developing an intelligent registration portal.
Students enter registration codes using uppercase letters, lowercase
letters, digits, and special symbols. Due to inconsistent data entry,
the administration wants the system to standardize and process the
information before storing it.

Conditions: - Ignore all special characters (@ # $ % & * - _) - Separate
alphabets and digits - Convert all alphabets to lowercase - Remove
duplicate alphabets - Arrange alphabets in ascending order - Arrange
digits in descending order - Display alphabets first and digits later -
If no digits are found, display “No Digits Found”

Test Case 1 Input: Enter registration code: zBc@638

Output: Result: bcz863

Test Case 2 Input: Enter registration code: 5Br$dE654b

Output: Result: bder6554

Test Case 3 Input: Enter registration code: A9@C3d#6B1a

Output: Result: abcd9631

Test Case 4 Input: Enter registration code: X#X@M2A4x7

Output: Result: amx742

Test Case 5 Input: Enter registration code: r@T#y

Output: Result: rty No Digits Found

"""
s=input("Enter String = ")
s1=""
s2=""
result=""

for i in s:
    if i.isalpha():
        if i.lower() not in s1.lower():
             s1=s1+i
    elif i=="!" or i=="@" or i=="#" or i=="&" or i=="%" or i=="$" or i=="*": 
        continue    
    else:
        s2=s2+i

for i in sorted(s1): 
        result=result+i
for i in sorted(s2)[::-1]:
    result=result+i
    

 
print(result.lower())    