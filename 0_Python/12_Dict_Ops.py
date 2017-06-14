# dict assignes items to keys
# list assignes items to position = index

D = {'name': 'Ramil', 'title': 'MLE & Founder', 'location': 'San Francisco, CA'}
print(D['name'])

print(D)

print(len(D))

print('name' in D) #True
print('Ramil' in D) #False

D['title'] = 'Machine Learning Engineer & Founder'
print(D)

D['transportation'] = 'Self-Driving Car'
print(D)

D['style'] = 'free'
print(D)

print(list(D.keys()))
print(list(D.values()))
print(list(D.items()))


del D['style']
print(D)

print(D.pop('transportation')) # Delete and return from key
print(D)

#####################################################

table = {'1975': 'Holy Grail', 
         '1979': 'Life of San Francisco',
         '1983': 'The Meaning of Life'}

year = '1983'
movie = table[year]
print(movie)

for year in table:
	print(year + '\t' + table[year])

#####################################################

Matrix = {}
Matrix[(2 ,3 ,4)] = 88
Matrix[(7 ,8 ,9)] = 99
Matrix[(0, 1, 5)] = 77
Matrix[(6, 9, 0)] = 66
Matrix[(3, 7, 1)] = 55 # forms dictinary, matirx is the key doubles are values

X = 2; Y = 3; Z = 4
print(Matrix[(X, Y, Z)])
print(Matrix)

if (2, 3, 6) in Matrix:
	print(Matrix[(2 ,3 ,6)])
else:
	print('Did not find!')

try:
	print(Matrix[(2, 3, 6)])
except KeyError:
	print('I can not find!')

print(Matrix.get((2 ,3 ,4), 'Still can not get!'))

######################################################

rec = {'name': 'Ramil',
       'jobs': ['Servant', 'Awsome', 'Hugger'],
       'web': 'www.ramilsoy.com',
       'home': {'state': 'Coastal', 'city': 'Ocean'}}

print(rec)
print(rec['home']['city'])

######################################################

db = []
db.append(rec) # turn list into dictionary 
print(db)

######################################################

Dictionary = dict(zip(['a', 'b', 'c'], [1 ,2 ,3]))
print(Dictionary)

######################################################

Diction = {x: x ** 2 for x in [1 ,2 ,3 , 4]}
print(Diction)

######################################################

Diction = {x: x ** 2 for x in range(66)}
print(Diction)

######################################################