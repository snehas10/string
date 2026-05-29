"""147Decompress a run-length encoded string. S = "a3b2c1"""
S = input("enter string = ")

result = ""

for i in range(0, len(S), 2):
    ch = S[i]
    count = int(S[i + 1])
    result = result + (ch * count)

print(result)