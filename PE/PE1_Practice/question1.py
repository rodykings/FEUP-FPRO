p=1000.0
t=1.0

def final_amount(r, n):
    return (p * (1+(r/n))**(n*t))

r_1 = float(input("Input a interest rate: "))
n_1 = float(input("Input the payment frequencies: "))

r_2 = float(input("Input another interest rate: "))
n_2 = float(input("Input the payment frequencies: "))

print("For r=" + str(r_1) + " and n=" + str(n_1) + " you'll have " + str(final_amount(r_1, n_1)))
print("For r=" + str(r_2) + " and n=" + str(n_2) + " you'll have " + str(final_amount(r_2, n_2)))
