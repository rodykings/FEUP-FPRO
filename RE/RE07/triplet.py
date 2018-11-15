def triplet(atuple):

    for i in range (0, len(atuple)+1, 1):
        for t in range (i+1, len(atuple), 1):
            for u in range (t+1, len(atuple), 1):
                if atuple[i] + atuple[t] + atuple[u] == 0:
                    return (atuple[i], atuple[t], atuple[u])
    return ()

