# works exactly like lists, except tuples can not be changed in place

T = ()
print(T)

T_1Item = (0,)
T_NotTuple = (0)
print(T_1Item)

T_4Item = (0, "Hi", 1.2, 3)
print(T_4Item)

T_4ItemOpen = 0, 'Hi', 1.2, 3
print(T_4ItemOpen)

T_Nested = ('Ramil', ('dev', 'mgi'))
print(T_Nested)

T_Tuple = tuple('Ramil')
print(T_Tuple[1])            # index
print(T_Tuple[1:3])          # slice
print(T_Nested[1][1])        # index of index
print(len(T_Tuple))          # length

T_Concatenate = T_Nested + T_Tuple
print(T_Concatenate)         # ('Ramil', ('dev', 'mgi'), 'R', 'a', 'm', 'i', 'l')

print(T_Tuple * 3)           # Repeat

for x in T_Tuple: print(x)

print('R' in T_Tuple)        # membership True
print('Ramil' in T_Tuple)    # membership False

print([x*2 for x in T_Tuple])

print(T_4Item.index('Hi'))   # search
print(T_4Item.count('Hi'))   # count
