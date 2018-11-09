def count(word, phrase):

    counter = 0

    word = word.lower()
    phrase = phrase.lower()
    phrase = phrase.split()

    for i in phrase:
        if i == word:
            counter += 1
    return counter
