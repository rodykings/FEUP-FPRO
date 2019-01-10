
def sort_rule(l):
    if l[1] == "sibling":
        rule = 0
    elif l[1] == "parent":
        rule = 1
    elif l[1] == "cousin":
        rule = 2
    elif l[1] == "grandparent":
        rule = 3

    return (rule, l[0])

def genealogy(l):

    return [tuple(t) for t in sorted([list(i) for i in l], key=sort_rule)]

print(genealogy([("maria", "parent"), ("matilde", "grandparent"),
("geraldes", "grandparent"), ("carlos", "sibling"),
("paulo", "sibling"), ("artur", "grandparent"),
("pedro", "parent"), ("alfredo", "cousin"), ("carla", "cousin")]))