"""19. Find the highest frequency character. S = "abracadabra"""

S = input("enter a string = ")

max_freq = 0
result = ""

for i in range(len(S)):

    # Skip already checked characters
    already = False
    for k in range(i):
        if S[i] == S[k]:
            already = True
            break

    if already:
        continue

    # Count frequency
    count = 0
    for j in range(len(S)):
        if S[i] == S[j]:
            count += 1

    # Find highest frequency
    if count > max_freq:
        max_freq = count
        result = S[i]

print("Highest frequency character:", result)
print("Frequency:", max_freq)