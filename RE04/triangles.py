
'''TRIANGLES'''

side_1 = int(input("Input one side: "))
side_2 = int(input("Input second side: "))
side_3 = int(input("Input third side: "))

if side_1+side_2<side_3 or side_1+side_3<side_2 or side_2+side_3<side_1:
    print("Not a triangle")
elif side_1 == side_2 == side_3:
    print("Equilateral")
elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
    print("Isosceles")
else:
    print("Scalene")
