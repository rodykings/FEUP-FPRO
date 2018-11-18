num = int(input("Number:"))
op = num
result = 0

while op > 0:
    result += (op % 10)**3  
    op = op // 10

if num == result:
    print(True)
else:
    print(False)
