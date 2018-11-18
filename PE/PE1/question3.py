names = ["bart", "marie", "jo"]
ages = [23, 75, 19]

string = ""
counter = 0

i=0
for name in names:
    t= 0
    for age in ages:
        if i == t:
            string += name + "-" + str(age) + " "
        t += 1
    i += 1

print(string)
