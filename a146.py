# Compress a string using run-length encoding
"""146Compress a string using run-length encoding. S = "aaabbc"""

S = input("enter string = ")

result = ""
count = 1

for i in range(len(S) - 1):
    if S[i] == S[i + 1]:
        count = count + 1
    else:
        result = result + S[i] + str(count)
        count = 1

# Add last character and count
result = result + S[-1] + str(count)

print(result)