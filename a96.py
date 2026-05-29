# Find the second most frequent word

S = "a b a c b"

words = S.split()

max1 = 0
max2 = 0
word1 = ""
word2 = ""

# Find frequencies using loops
for i in range(len(words)):
    count = 0
    
    for j in range(len(words)):
        if words[i] == words[j]:
            count = count + 1

    # Update first and second highest
    if count > max1:
        max2 = max1
        word2 = word1

        max1 = count
        word1 = words[i]

    elif count > max2 and words[i] != word1:
        max2 = count
        word2 = words[i]

print("Second most frequent word:", word2)