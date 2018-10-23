num = input("Input a number: ")
num_int = int(num)

result = num_int + (num_int * 10 + num_int) + (num_int * (10**2) + num_int * 10 + num_int)

print(num + " + " + num + num + " + " + num + num + num + " = " +  str(result))
