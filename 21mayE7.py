"""7.
Customer Feedback Analysis System

An e-commerce company receives thousands of customer reviews every day for its products.

To analyze customer opinions efficiently, the analytics team wants a Python program that counts how many times each word appears in a review message.

This helps the company identify frequently used words such as:

good
bad
delivery
quality
service

Write a Python program to count the frequency of every word in a given sentence.

Input:
delivery was fast and delivery service was good
Output:
delivery : 2
was : 2
fast : 1
and : 1
service : 1
good : 1"""
s=input("enter string = ")
word=s.split()
for i in range(0, len(word)):
    f=0
    for k in range(0,i):
        if word[i]==word[k]:
            f=1
            break
    if f==0:    
        j=0
        count=0
        while j<len(word):
            if word[i]==word[j]:
                count=count+1  
            j=j+1 
        print(word[i], ":" ,count)

        
