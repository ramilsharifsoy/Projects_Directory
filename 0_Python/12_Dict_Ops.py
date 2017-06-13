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
