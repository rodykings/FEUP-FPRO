def sort_rule(records):

    mean = -(float(sum(records[2])/max(len(records[2]), 1)))
    return (mean, records[0], records[1])

def sort_grades(records):

    return tuple(sorted(records, key=sort_rule, reverse=False))

