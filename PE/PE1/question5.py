num = int(input("Octal Number:"))

octal = 0
place = 0

while num > 0:
    octal += num % 8 * 10 ** place
    num //= 8
    place += 1

print(str(octal))
