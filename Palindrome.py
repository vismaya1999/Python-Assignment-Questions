def palindrome(n):
    num_str = str(n)
    rev_str = num_str[::-1]
    return num_str == rev_str
n = int(input("Enter a number to Check: "))
if palindrome(n):
    print(n, "is a palindrome")
else:
    print(n, "is not a palindrome")
