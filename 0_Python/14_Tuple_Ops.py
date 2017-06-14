print((1, 2) + (3 ,4)) # Concatenation (1, 2, 3, 4)
print((1 ,2) * 4)      # repetition (1, 2, 1, 2, 1, 2, 1, 2)

T_1 = (1 ,2 ,3 ,4, 2)
T_2 = T_1[0] ,T_1[1:3]
print(T_2)             # Indexing, slicing (1, (2, 3))

x = (40)               # integer
x = (40,)              # tuple

###### convert tuples > lists > tuples ########################

T = ('aa', 'bb', 'cc', 'dd', 'ee')
T_List = list(T)
print(T_List)

T_Tuple = tuple(T_List)
print(T_Tuple)

L = [x + 20 for x in T_1]
print(L)

print(T_1.index(2))
print(T_1.index(2 ,2))
print(T_1.count(2))

######## conver tuples > dictionaries ###########################

ramil = dict(name='Ramil', age=40.5, jobs=['dev', 'mgr'])
print(ramil)

print(ramil['name'], ramil['jobs'])

##################################################################

from collections import namedtuple
Rec = namedtuple('Rec', ['name', 'age', 'jobs'])
Ram = Rec('Ramil', 40.5, ['dev', 'mgr'])
print(Ram)

O = Ram._asdict()
print(O)

##################################################################