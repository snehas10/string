"""7. Remove Duplicate Words from a String

Voice Assistant Noise Correction System

A voice assistant records spoken commands from users.

Due to microphone disturbance and network lag, some words are repeated multiple times.

The company wants a Python program that removes duplicate words while maintaining the original order.
input: hello hello how are are you
Output: hello how are you"""
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