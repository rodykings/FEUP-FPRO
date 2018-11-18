d = int(input("d:"))
num = int(input("num:"))
op = num
result = 0

while op > 0:
    if (op % 10) > d:
        result += 2 * (op % 10)
    op //= 10

print(result)
