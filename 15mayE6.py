"""
6.
Railway Ticket PNR Analyzer

A railway department wants to verify whether a PNR number is valid.

Conditions:
- PNR must start with "PNR"
- Total length should be 12 characters
- Remaining characters should be digits

Input:
Enter PNR: PNR123456789

Output:
Valid PNR Number
"""
n=input("Enter PNR:")
if n.startswith("PNR") and len(n)==12 and n[3:].isdigit():
    print("Valid PNR number")
else:
    print("Invalid PNR number")