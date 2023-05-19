def is_perfect_number(number):
    total_sum = 0
    for i in range(1, number):
        if number % i == 0:
            total_sum += i
    if total_sum == number:
        return True
    else:
        return False
number = int(input())
if is_perfect_number(number):
    print("True")
else:
    print("False")