L_empty = []
print(L_empty)

L_4items_Index0_3 = [123, 'abs', 1.23, {}]
print(L_4items_Index0_3)
print(L_4items_Index0_3[-1])

L_Nested_Sublists = ['Bob', 40.0, ['dev', 'man']]
print(L_Nested_Sublists)
print(L_Nested_Sublists[-1])

L_Iterable_Item = list('unique')
print(L_Iterable_Item)

L_Successive_Integers = list(range(-4, 5))
print(L_Successive_Integers)

L_Index = L_Successive_Integers[2]
print(L_Index)

L_Index_Of_Index = L_Nested_Sublists[-1][1]
print(L_Index_Of_Index)

L_Slice = L_Successive_Integers[1:3]
print(L_Slice)

L_Length = len(L_4items_Index0_3)
print(L_Length)

L_Concatenate = L_4items_Index0_3 + L_Successive_Integers
print(L_Concatenate)

L_Repeat = L_Iterable_Item * 3
print(L_Repeat)

for x in L_Iterable_Item: print(x)

L_In_True_Memebership = 3 in L_Successive_Integers
print(L_In_True_Memebership)

L_In_False_Membership = 6 in L_Successive_Integers
print(L_In_False_Membership)

L_Append = L_Successive_Integers.append(5)
print(L_Append)
print(L_Successive_Integers)

L_Extend = L_Successive_Integers.extend([6, 7, 8])
print(L_Successive_Integers)

L_Insert = L_Successive_Integers.insert(0, -5)
print(L_Successive_Integers)

L_Index_Show = L_Successive_Integers.index(1)
print(L_Index_Show)

L_Count = L_Successive_Integers.count(5)
print(L_Count)

L_Sort = L_Iterable_Item.sort()
print(L_Sort) # Why None
print(L_Iterable_Item)

L_Reverse = L_Successive_Integers.reverse()
print(L_Successive_Integers)

L_Copy = L_Nested_Sublists.copy()
print(L_Copy)

L_Clear = L_Nested_Sublists.clear()
print(L_Clear)
print(L_Nested_Sublists)

print(L_Iterable_Item.pop(2)) # just keep indexed remove rest
print(L_Iterable_Item.remove('i'))

del L_Successive_Integers[1] # delete 7
print(L_Successive_Integers)

del L_Successive_Integers[3:5] # delete 4, 3
print(L_Successive_Integers)

L_Successive_Integers[3:5] = [] # delete 2, 1
print(L_Successive_Integers)

L_Successive_Integers[3] = 4 # index assignment, chnage 0 to 4
print(L_Successive_Integers)

L_Successive_Integers[3:7] = [3,3,3] # replace number between indexes 3-7 with 3,3,3
print(L_Successive_Integers)

L = [x**2 for x in range(35)]
print(L)
print(L[10])

L_Map = list(map(ord, 'Ramil'))
print(L_Map)