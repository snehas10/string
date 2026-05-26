"""6.
AI Voice-to-Text Correction System

A company has developed an AI-based voice-to-text application for virtual meetings.

Due to microphone disturbances and speech recognition delays, some words are captured multiple times consecutively in the generated text.

Before saving the meeting transcript, the system must remove duplicate words while maintaining the original order of words.

Write a Python program to remove repeated words from a sentence.

Input:
hello hello team team meeting meeting started
Output:
hello team meeting started
"""
s=input("enter a string = ")
word=s.split()
rev=""
i=0

while i<len(word):
    f=0
    j=0
    while j<i:
        if word[i]==word[j]:
            f=1
            break
        j=j+1
    if f==0:
        rev=rev+word[i]+" "    
    i=i+1
print(rev)