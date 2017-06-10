print(len([1, 2, 3, 4])) # length

print([1, 2, 3] + [4, 5, 6, 7]) #concatination

print(['Hi! ']*4) # repat as a new list

print(str([1, 2]) + "34") # strage string ???

print([1, 2] + list("34")) # 3 and 4 are not numbers

print(3 in [1, 2, 3]) # check membership => True

for x in [1, 2, 3]:
	print(x, end = ' ')
print('\n')

res = [c * 4 for c in "RAMIL"] # build list with for inline
print(res)

# or build list with for loop:

res = []
for c in 'RAMIL':
	res.append(c * 5)
print(res, '\n')

listmap = list(map(abs, [-2, -1, 0, 1, 2]))
print(listmap)
print('\n')

L = ['Ramil', 'Sharifsoy', 'Founder', 'Engineer', 'Smiler']

r = 0
p = 5-r
for o in L:
	print( L[r:p])
	if r < 5:
		r += 1

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(matrix[2][1]) # 3rd row 2nd item

L = L + ['Awsome', 'Python', 'C++']
L[-1] = 'Python'
L[-3:-1] = ['C++', 'Awsome']
print(L) # sliced, indexed, replaced

L.sort(key = str.lower, reverse = True)
print(L)

Lsorted = sorted(L, key = str.lower, reverse = False)
print(Lsorted)

print(sorted([x.lower() for x in L], reverse = True)) #lower all letters = different than previous types !!!

LastName = 'Sharifov'
print(LastName)
LastName = LastName.replace('ov', 'soy')
print(LastName)

