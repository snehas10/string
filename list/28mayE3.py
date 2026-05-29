"""3.
# Assignment: Prime Number Analyzer using List (Python)

## Scenario
A coaching institute stores student lucky numbers in a Python List.
Your task is to analyze the list and identify prime numbers for a scholarship selection process.

You must iterate through every element of the list and perform prime number analysis.

---

# Requirements

Write a Python program to:

1. Store integer values in a List
2. Iterate through all elements of the List
3. Check whether each number is prime or not
4. Display all prime numbers
5. Count total prime numbers
6. Count total non-prime numbers
7. Find the largest prime number from the List
8. Store all prime numbers into another List
9. Sort the prime numbers in ascending order and display them

---

# Test Case 1

## Input

[2, 3, 4, 5, 6, 7, 8]

## Expected Output

Prime Numbers: 2 3 5 7
Prime Count: 4
Non-Prime Count: 3
Largest Prime Number: 7
Prime List: [2, 3, 5, 7]
Sorted Prime List: [2, 3, 5, 7]

---

# Test Case 2

## Input

[10, 11, 12, 13, 14, 15]

## Expected Output

Prime Numbers: 11 13
Prime Count: 2
Non-Prime Count: 4
Largest Prime Number: 13
Prime List: [11, 13]
Sorted Prime List: [11, 13]

---

# Test Case 3

## Input

[1, 2, 17, 19, 20, 25]

## Expected Output

Prime Numbers: 2 17 19
Prime Count: 3
Non-Prime Count: 3
Largest Prime Number: 19
Prime List: [2, 17, 19]
Sorted Prime List: [2, 17, 19]

---

# Test Case 4

## Input

[4, 6, 8, 9, 10]

## Expected Output

Prime Numbers: None
Prime Count: 0
Non-Prime Count: 5
Largest Prime Number: Not Available
Prime List: []
Sorted Prime List: []

---

# Test Case 5

## Input

[29, 31, 37, 41]

## Expected Output

Prime Numbers: 29 31 37 41
Prime Count: 4
Non-Prime Count: 0
Largest Prime Number: 41
Prime List: [29, 31, 37, 41]
Sorted Prime List: [29, 31, 37, 41]

---
"""
n=int(input("enter number of list = "))
arr=[]
for i in range(n):
    x=int(input("enter numbers = "))
    arr.append(x)
print(arr)
count1=0
count2=0

nonprime=[]
prime=[]

for i in arr:
  
  if i<=1:
    x=1
  else:
    x=0
    for j in range(2, i):
        if i%j==0:
            x=1
            break
    if x==0:
        prime.append(i)
        count1=count1+1
    else:
        nonprime.append(i)
        count2=count2+1
print("Prime Number = ",prime)    
print("Prime count = ",count1)
print("Non Prime count = ",count2)    

print("Non Prime Number = ",nonprime)  

ma=0
for i in prime:
   if i>ma:
      ma=i   
print("Max prime = ",ma)
prime.sort()
print("Sorted List of Prime = ",prime)





