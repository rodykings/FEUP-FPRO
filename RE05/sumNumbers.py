def sum_numbers(n):
    sum = 0
    if n < 0:
        sum = n
        return sum
    elif n == 0:
        return sum
    else:
        for i in range(1, n+1, 1):
            sum += i
        return sum

print(sum_numbers(10))
