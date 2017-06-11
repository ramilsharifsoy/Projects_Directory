# array in other languages, where name is more meaningfull than idex number

D_Empty = {}
print(D_Empty)

D_Two_Item = {'name': 'Ramil', 'age': 40}
print(D_Two_Item)

D_Nesting = {'CEO': {'Name': 'Ramil', 'Age': 40}}
print(D_Nesting)
print(D_Nesting)

D_Alternative = dict( name = 'Ramil', age = 40) # same as twp item dictionary
print(D_Alternative)

D_Key_Words = dict([('name', 'Sharifsoy'), ('age', 40), ('Location', 'San Francisco')]) # similar as twp item dictionary
print(D_Key_Words)

D_Keys = dict.fromkeys(['name', 'age'])
print(D_Keys)

D_Zipped = dict(zip(D_Two_Item.keys(), D_Two_Item.values())) # same as twp item dictionary, can be large disctionary
print(D_Zipped)

print(D_Two_Item.keys())
print(D_Two_Item.values())
print(D_Two_Item.items()) # all key_value tuples

D_Nesting_Copy = D_Nesting.copy()
print(D_Nesting_Copy)

D_Clear = D_Empty.clear()
print(D_Clear)

D_Two_Item.update(D_Key_Words)
print(D_Two_Item)

print(len(D_Key_Words))

D_Two_Item['age'] = 37
print(D_Two_Item)

del D_Key_Words['Location']
print(D_Key_Words)

print(list(D_Two_Item.keys())) # list of keys

D_Comprehension = {x: x*2 for x in range(10)}
print(D_Comprehension)