"""20. Find the lowest frequency character."""
S = "aabbcde"

min_freq = len(S)
result = ""

for i in range(len(S)):
    
    # Skip if character already checked
    already = False
    for k in range(i):
        if S[i] == S[k]:
            already = True
            break

    if already:
        continue

    # Count frequency using loop
    count = 0
    for j in range(len(S)):
        if S[i] == S[j]:
            count += 1

    # Find minimum frequency
    if count < min_freq:
        min_freq = count
        result = S[i]

    elif count == min_freq:
        result += " " + S[i]

print("Lowest frequency characters:", result)