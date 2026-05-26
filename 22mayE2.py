"""# 2. AI Auto-Correct Consecutive Word Remover

An AI-powered typing assistant often captures duplicate consecutive words while converting speech into text.

The company wants a Python program that removes only consecutive duplicate words while preserving the original sentence structure.

### Input:

text
hello hello hello team meeting meeting started


### Output:

text
hello team meeting started"""
n=input("enter a string =")
word=n.split()
rev=""
for i in range(0, len(word)):
    f=0
    for j in range(0, i):
        if word[i]==word[j]:
            f=1
            break
    if f==0:
        rev=rev+word[i]+" "
print(rev)            
