""""""
# Find the first recurring substring of length k

s = input("Enter the string: ")
k = int(input("Enter value of k: "))

found = False

for i in range(len(s) - k + 1):

    sub = s[i:i+k]

    # Check if substring appears again
    for j in range(i + 1, len(s) - k + 1):

        if sub == s[j:j+k]:
            print("First recurring substring:", sub)
            found = True
            break

    if found:
        break

if not found:
    print("No recurring substring found")