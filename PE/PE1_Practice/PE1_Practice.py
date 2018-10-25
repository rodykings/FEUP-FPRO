

lower_input = int(input("lower="))
upper_input = int(input("upper="))


def prime_numbers(lower, upper):
    prime_str = ""
    for i in range(lower, upper+1, 1):
        divisors = 0
        for n in range (1, i+1):
            if i % n == 0:
                divisors += 1
        if divisors == 2:
            prime_str += str(n) + " "
    return prime_str

final_str = "Prime numbers between " + str(lower_input) + " and " + str(upper_input) + " are: \n" + prime_numbers(lower_input, upper_input)
print(final_str)


            
