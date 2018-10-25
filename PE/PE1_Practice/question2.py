
num = int(input("Input an int number: "))
divisors = ""
sum = 0

for i in range (1, num+1):
    if num % i == 0:
        divisors += str(i)
        sum += i
        if i != num:
            divisors += "+"
    else:
        continue

final_str = str(sum) + " (" + divisors + ")"
print(final_str)
