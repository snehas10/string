"""19 Find the highest frequency character. S = "abracadabra"""
S = "aabbcde"

for ch in S:
    count = 0

    for x in S:
        if ch == x:
            count = count + 1

    if count == 1:
        print("First non-repeating character is:", ch)
        break