

n = int(input("Input a number: "))

if n == 1:
        print("False")
else:
    for i in range (2 , n, 1):  
        if (n % i) == 0:
            print("False")
            break
    else:
        print("True")