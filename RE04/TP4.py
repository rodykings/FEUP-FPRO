num = int(input("Input a number: "))
num_in = num
reverse = 0
counter = 0

while num > 0:
    num //= 10
    counter += 1

num = num_in
    
while num > 0:
    counter -= 1
    reverse += (10**counter) * (num%10)
    num //= 10
    



if reverse == num_in:
    result = str(num_in) + " is a palindrome."
else:
    result = str(num_in) + " is not a palindrome."

print(result)