num = int(input("Input a number: "))
second = 0

if num < 0:
    print("Its is impossible to find the square root")
else:
    first = num/2
    second = (first+(num/first))/2

    while abs(second-first) > 0.01:
        first = second
        second = (second+(num/second))/2
   
print("%.3f" % second)


            
