"""22. Find the last repeating character. S = "abracadabra ans=r"""
n=input("Enter string = ")

last = ""

for i in range(len(n)):
    
    count = 0

    for j in range(len(n)):
        if n[i] == n[j]:
            count = count + 1

    if count > 1:
        last = n[i]

print("Last repeating character is:", last)