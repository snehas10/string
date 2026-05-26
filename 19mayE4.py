"""4.  Instant Messaging Word Encryption System

A messaging application wants to temporarily encrypt messages during
transmission. The encryption rule is to reverse every word individually
while keeping the word positions unchanged.

Input: Enter message: java is powerful

Output: Encrypted Message: avaj si lufrewop
"""
n=input("Enter msg :")
words=n.split()
i=0
while i<len(words):
    word=words[i]
    rev=""
    j=len(word)-1
    while j>=0:
        rev=rev+word[j]
        j=j-1
    print(rev,end=" ")
    i=i+1    