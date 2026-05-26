"""5. Compare two strings ignoring case"""
s1=input("enter a string = ")
s2=input("enter second str = ")
for i in range(0, len(s1)):
    if s1[i].lower()==s2[i].lower():
        print("Match")
        break
    else:
        print("Not match")