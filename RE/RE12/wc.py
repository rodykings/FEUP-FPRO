def wc(filename):
    lines=0
    words=0
    chars=0
    with open(filename, "r") as file:
        for line in file:
            lines += 1
            words += len(line.split())
            chars += len(line)
            
    return (lines, words, chars)

print(wc("shakespeare.txt"))
print(wc("monty.txt"))