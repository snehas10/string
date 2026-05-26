"""
2.
Mobile Number Digit Counter

A telecom company wants to count how many digits are present in a customer contact number entered with spaces or symbols.

Input:
Enter contact number: +91 98765-43210

Output:
Total digits: 12

"""
n=input("enter a num = ")
count=0
for i in n:
    if i==" " or i=="-" or i=="+":
        count+=0
    else:
        count+=1
print("Total digit: ",count)

