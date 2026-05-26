"""
4.
Consonant Counter in Student Name Record

A school management system wants to count how many consonants are present in student names.

Input: Enter student name: Ajay Singh Thakur

Output: Total consonants: 11"""
n=input("Enter student name=")
count=0
for i in n:
    if i!="a" and i!="e" and i!="i" and i!="u" and i!="o" and i!="A" and i!="I" and i!="O" and i!="U" and i!="E" and i!=" ":
        count+=1

print("total consonants: ",count)


