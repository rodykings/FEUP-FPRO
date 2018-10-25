print("'WELCOME TO FIZZ BUZZ' " + "\n")
max_number = int(input("Input the last number: "))

result_str = ""

for i in range (1, max_number + 1):
    if i % 3 == 0 and i % 5 == 0:
        continue
    elif i % 3 == 0:
        result_str += "Fizz "
    elif i % 5 == 0:
        result_str += "Buzz "
    else:
        result_str += str(i) + " "

print(result_str)
