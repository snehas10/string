"""Anagram or not """
S1 = "listen"
S2 = "silent"

if len(S1) != len(S2):
    print("Not Anagrams")

else:
    flag = True

    for ch in S1:

        count1 = 0
        count2 = 0

        for x in S1:
            if ch == x:
                count1 = count1 + 1

        for y in S2:
            if ch == y:
                count2 = count2 + 1

        if count1 != count2:
            flag = False

    if flag:
        print("Strings are Anagrams")
    else:
        print("Strings are Not Anagrams")