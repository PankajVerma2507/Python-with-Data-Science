from pprint import pp

movies = {}
movies['Top Gun: Maverik'] = 8.3
movies['everything Everywhere all at once'] = 8.1
movies['spider Man: No Way Home'] =8.2

# pp(movies)

for item in movies:
    print(item)

print('only values')
for item in movies:
    print (movies[item])

print('both key and values')
for key in movies:
    print(key,movies[key])
     
    print('using dict.items()method')
    for k,v in movies.items()
    print(k, v)

#user input
for i in range(3):
    name = input('Movie Name:')
    rating = float(input('Movie rating:'))
    movies[name] = rating

print('using dict.items() method')
for k,v in movies.items():
    print(k,v)
