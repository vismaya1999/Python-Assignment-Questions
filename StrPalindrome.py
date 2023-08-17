def palindrome(s):
    s = s.lower()
    s = ''.join(filter(str.isalnum, s))
    reversed_s = s[::-1]
    return s == reversed_s

n = input("Enter a string: ")
if palindrome(n):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
