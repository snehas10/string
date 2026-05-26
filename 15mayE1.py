"""1.Vowel Counter in Customer Feedback

 A company wants to analyze customer feedback messages by counting how many vowels are present in the feedback.

Input: Enter feedback message: Hello Customer Service

Output: Total vowels: 8"""
n=input("Enter feedback message:")
count=0
for i in n:
    if i=="a" or i=="e" or i=="i" or i=="u" or i=="o" or i=="A" or i=="I" or i=="O" or i=="U" or i=="E":
        count=count+1
print("total vowels:",count)        