"""32 Count frequency of each word. S = "apple banana apple"""
S = "apple banana apple"

words = S.split()

checked = ""

for i in range(len(words)):

    if words[i] not in checked:

        count = 0

        for j in range(len(words)):
            if words[i] == words[j]:
                count = count + 1

        print(words[i], "=", count)

        checked = checked + words[i] + " "