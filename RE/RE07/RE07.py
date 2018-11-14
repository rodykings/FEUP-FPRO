
from operator import itemgetter, attrgetter

def sort_grades(records):
    average = ()
    for i in records:
        average += ((i[2][0] + i[2][1])/2, )

    return tuple(sorted(records, key=itemgetter(2,0,1)))

records=(('João', 'up20186042', (90, 87)),
('Ana', 'up20186040', (90, 90)),
('José', 'up20186063', (70, 90)),
('Ana', 'up20186061', (90, 90)),
('Tiago', 'up20186070', (100, 90)))

print(sort_grades(records))        