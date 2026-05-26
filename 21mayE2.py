"""
2.
Find the Most Frequently Occurring Word
News Channel Keyword Analyzer

A news agency analyzes breaking news headlines to identify the most repeated keyword in a report.

Write a Python program to find the word with the highest frequency.

Input:
india won the match and india created history
Output:
india"""
n=input("enter a string = ")
word=n.split()
rev=""

i=0
while i<len(word):
    j=0
    f=0
    while j<i:
        if word[i]==word[j]:
            print(word[i],end=" ")
            break
        j=j+1
    i=i+1       