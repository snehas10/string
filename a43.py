"""Check if two strings are rotations of each other. S1 = "abcde", S2 = "cdeab"""
S1 = "abcde"
S2 = "cdeab"

if len(S1) == len(S2) and S2 in (S1 + S1):
    print("Strings are rotations of each other")
else:
    print("Strings are not rotations")