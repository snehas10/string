"""
5.
Palindrome Product Code Checker

A factory wants to identify whether a product code reads the same forward and backward.

Input:
Enter product code: MADAM

Output:
Palindrome Code

Input:
Enter product code: PRODUCT

Output:
Not a Palindrome Code

"""
n=input("enter product code=")
temp=""
for i in n:
    temp=i+temp

if n==temp:
    print("Palindrome code")
else:
    print("Not Palindrome code")