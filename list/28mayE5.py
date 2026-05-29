"""5.
 Student Grade Classification System (Python List Assignment)


A school stores student marks in a list. The system must analyze the marks and generate a *clear performance report* 
by grouping students into grade categories.



Write a Python program to:

* Iterate through the list of marks
* Assign grades based on marks:

  * *>= 90 → A*
  * *>= 75 and < 90 → B*
  * *>= 50 and < 75 → C*
  * *< 50 → Fail*
* Store each category in separate lists
* Count students in each category
* Display a *final structured report (important)*

---

## 📌 Output Format (Mandatory)

Your output must be displayed exactly in this format:


===== STUDENT GRADE REPORT =====

A Grade Students   : [list]
B Grade Students   : [list]
C Grade Students   : [list]
Fail Students      : [list]

--------------------------------
A Count   : X
B Count   : X
C Count   : X
Fail Count: X
--------------------------------

Total Students: X


---

 Input

[95, 82, 67, 45, 30]

Output


===== STUDENT GRADE REPORT =====

A Grade Students   : [95]
B Grade Students   : [82]
C Grade Students   : [67]
Fail Students      : [45, 30]

--------------------------------
A Count   : 1
B Count   : 1
C Count   : 1
Fail Count: 2
--------------------------------

Total Students: 5"""

n=int(input("enter number of list = "))
arr=[]
for i in range(n):
    x=int(input("enter numbers = "))
    arr.append(x)
print(arr)

a=[]
b=[]
c=[]
fail=[]
count=0
count2=0
count3=0
count4=0
for i in arr:
    if i>=90:
        a.append(i)
        count=count+1
    elif i<90 and i>=75:
        b.append(i)
        count2=count2+1
    elif i<75 and i>=50:
        c.append(i)
        count3=count3+1
    else:
        fail.append(i)
        count4=count4+1
print("-----Students grade report---------")        
print("A grade student =",a)
print("B grade student =",b)
print("C grade student =",c)
print("Fail grade student =",fail)
print("----------------------------")
print("A count =",count)
print("B count =" ,count2)
print("C count =",count3)
print("Fail count =",count4)
print("------------------------------")
print("Total Count student = ",n)



