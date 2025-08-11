import csv
with open('movies_1.csv', 'r') as file:
  movie_reader = csv.DictReader(file)
  all_movies = [row for row in movie_reader ]

#movie_budget: dict[str, float] = {}  
"""
print([ movie['Movie_Name'] for movie in all_movies if movie['Release_Year'] == '2006'])
# where lead_actor is Pavan Kalyan or Prabhas and comedy actor brahmanandam
print([ movie['Movie_Name'] for movie in all_movies if (movie['Lead_Actor'] == 'Pawan Kalyan' or movie['Lead_Actor'] == 'Prabhas') and movie['Main_Comedy'] == 'Brahmanandam'])


comedy = len([ movie['Movie_Name'] for movie in all_movies if 'Comedy' in movie['Genre'] ])
total_count = len(all_movies)
print ("Comedy %: ", comedy/total_count * 100)
"""

prabhas_movies = [movie for movie in all_movies if movie['Lead_Actor'] == 'Prabhas']
print(prabhas_movies)