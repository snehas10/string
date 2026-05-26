"""if all character are unique or not """
S1 = "abc"
S2 = "abca"

# Checking S1
unique = True

for i in range(len(S1)):
    for j in range(i + 1, len(S1)):
        if S1[i] == S1[j]:
            unique = False

if unique:
    print("S1: All characters are unique")
else:
    print("S1: Characters are not unique")


# Checking S2
unique = True

for i in range(len(S2)):
    for j in range(i + 1, len(S2)):
        if S2[i] == S2[j]:
            unique = False

if unique:
    print("S2: All characters are unique")
else:
    print("S2: Characters are not unique")