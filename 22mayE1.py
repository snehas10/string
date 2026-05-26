"""
1. Smart Log File Error Pattern Detector

A cybersecurity company stores server logs containing repeated system activity characters.

To detect suspicious looping behavior, the analytics team wants a Python program that finds the longest repeating substring present in the log file.

If multiple substrings have the same length, print the first one found.

 Input:

text
abcabcbb


Output:

text
abc"""


s = input("Enter the string: ")

longest = ""
current = ""

for ch in s:
    if ch in current:
        index = current.index(ch)
        current = current[index + 1:]

    current += ch

    if len(current) > len(longest):
        longest = current

print("Longest first substring without repeating characters:", longest)