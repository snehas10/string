""" 8. Toggle the case of each character.
s=input("enter a string = ")
print(s.swapcase())

9. Check whether a string is empty
s=input("enter a string = ")
s1=input("enter second str= ")
print(s.isspace())
print(s1.isspace())

10. 0Trim leading, trailing, or extra spaces.
s=input("enter a string = ")
print(s.strip())

11. Get the character at a given index.
s=input("enter a str = ")
print(s[2])

12. Get the Unicode code point of a character at index.
s=input("enter str = ")
print(ord(s[0]))

13 . Get the Unicode code point before index.
s=input("enter str ")
print(ord(s[0]))

14. Find the first occurrence of a character.
s=input("enter str = ")
cha=input("Enter str = ")
for i in range(1, len(s)):
    if s[i]==cha:
        print(s.index(cha))
        break

15. Find the last occurrence of a character
s=input("enter str = ")
cha=input("Enter str = ")
print(s.rfind(cha))

16. Count total occurrences of a character.
s=input("enter str = ")
cha=input("Enter str = ")
print(s.count(cha))

17. Remove occurrences of a character

s=input("enter str = ")
cha=input("Enter str = ")
print(s.replace(cha,""))

18. Replace occurrences of a character.
s=input("enter str = ")
cha=input("Enter str = ")
print(s.replace(cha,"x"))

19.Find the highest frequency character."""
s=input("enter str = ")
cha=input("Enter str = ")
print(s.find(cha))