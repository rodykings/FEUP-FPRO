tS = float(input("Swimming:"))
tC = float(input("Cycling:"))
tR = float(input("Running:"))

vS = 1.5 / 2
vC = 40 / 20
vR = 10 / 8

if tS + tC + tR > 4.0:
    print("Time")
elif tS > vS:
    print("Swimming")
elif tC > vC:
    print("Cycling")
elif tR > vR:
    print("Running")
else:
    print(tS + tC + tR)
