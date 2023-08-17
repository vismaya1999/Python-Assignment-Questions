def armstrong(n):
    n_str = str(n)
    num_digits = len(n_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in n_str)
    return armstrong_sum == n
num = int(input("Enter a number: "))
if armstrong(num):
    print(num, "Is an Armstrong number")
else:
    print(num, "Is not an Armstrong number")
