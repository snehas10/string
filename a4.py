"""4. Compare two strings (case-sensitive)."""
s1=input("enter a string = ".title())
s2=input("enter second string = ".title())
w=s1.split()
w1=s2.split()
for i in range(0, len(w)):
    r=0
    for j in range(0, len(w1)):

       if w[i]==w1[i]:
          r=1
          break
if r==0:
    print("Not match") 
else:
    print("match")       
