def find_largest_digit(num):
    largest_digit = 0
    while num > 0:
        digit = num % 10
        if digit > largest_digit:
            largest_digit = digit
        num//=10
    return largest_digit
num = int(input())
largest=find_largest_digit(num)
print(largest)