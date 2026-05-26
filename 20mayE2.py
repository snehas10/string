"""
2. Reverse Sentence + Reverse Each Word

Secret Military Communication Decoder
A defense organization stores highly confidential messages in encrypted form.
To decode the message:

1. Reverse the entire sentence.
2. Reverse every individual word.
3. Store the final result back into the original string variable.

You must use the split() method.
Input


Python is powerful


Output:


lufrewop si nohtyP
"""
n=input("enter a string = ")
"""word=n.split()
i=len(word)-1
while i>=0:
    words=word[i]
    rev=""
    j=len(words)-1
    while j>=0:
        rev=rev+words[j]
        j=j-1
    n=rev    
    print(n, end=" ")
    i=i-1    """
rev=n[::-1]
print(rev)

