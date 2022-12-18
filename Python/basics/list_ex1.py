movies = ['sholay','baghwan','ddlj', 'ironman','RRR',
          'inception','diljale','suryavanshi', 'gajani', 'Ram']

print(len(movies))
print(movies)

movies.sort()
print(movies)

movies.reverse()
print(movies)

print('first movie',movies[0])
print('last movie',movies[-1])
print('first 3 movies',movies[:3])
print('all movies except first 3',movies[3:])
print('movies with even indexex',movies[::2])
print('movies with odd indexex',movies[1::2])
print('last 3 movies',movies[-3:])