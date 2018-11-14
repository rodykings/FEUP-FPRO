def palindrome(astring):
    counter = 0
    for t in range (2, len(astring) + 1):
        for i in range (0, len(astring)):
            string = astring[i:(i+t)]
            if len(string) != t:
                continue
            else:
                if  string == string[::-1]:
                    counter += 1
    return ("For string '{}': {} palindrome substrings").format(astring, str(counter))

print(palindrome("banana"))
