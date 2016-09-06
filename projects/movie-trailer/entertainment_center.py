import fresh_tomatoes
import json
import media
import re
import urllib.request

# This is a helper method to retrieve data from various apis.
def get_movie_info(name, get_trailer_from_trailersapi=False):
    parsed_movie_name = name.replace(' ', '%20')
    connection = urllib.request.urlopen('http://www.omdbapi.com/?t=' + parsed_movie_name)
    data = json.loads(connection.read().decode('utf8'))
    connection.close()

    if get_trailer_from_trailersapi:
        trailer_connection = urllib.request.urlopen('http://trailersapi.com/trailers.json?movie=' + parsed_movie_name)
        trailer_data = trailer_connection.read().decode('utf8')

        print('trailer_data: ' + trailer_data)

        if re.search(name.lower(), trailer_data.lower()) != None:
            trailer_data = re.split(r'embed', trailer_data)
            trailer_data = re.split(r'\\', trailer_data[1])
            trailer_data = re.split(r'/', trailer_data[1])
            trailer_data = trailer_data[1]
            print('')
            # print('trailer: ' + name + ' -> ' + trailer_data[0])
            print(name + ' trailer -> ' + trailer_data)
            print('')
            trailer_connection.close()

            data['Trailer'] = 'https://www.youtube.com/watch?v=' + trailer_data

    return data

# Create and populate a Movie object (using a manual youtube trailer link if
# no trailer can be obtained externally.)
def populate_media_movie(movie_name, manual_movie_trailer_link = ''):
    movie = get_movie_info(movie_name, True)
    if 'Trailer' in movie:
        trailer = movie['Trailer']
    else:
        trailer = manual_movie_trailer_link

    return media.Movie(
        movie['Title'],
        movie['Plot'],
        movie['Poster'],
        trailer)

def load_movie_cache():
    cache = dict()

    with open('movie_cache.json') as json_file:
        movie_cache = json.load(json_file)

        for movie in movie_cache:
            cache[movie['title'].lower()] = media.Movie(movie['title'], movie['storyline'], movie['poster_image_url'], movie['trailer_youtube_url'])

    return cache

def save_movie_cache(movies_dict):
    with open('movie_cache.json', 'w') as json_file:
        json.dump([m.__dict__ for m in movies_dict.values()], json_file, indent = 4)

###############################################################################

movies_cache = load_movie_cache()

###############################################################################
# Load all the movies from the list, but skip over previously loaded movies.
# There's a hardcoded trailer  that
movies_to_load = [
    {'title':'Deadpool', 'hardcoded_trailer_youtube_url':'https://www.youtube.com/watch?v=ONHBaC-pfsk'},
    {'title':'Toy Story', 'hardcoded_trailer_youtube_url':'https://www.youtube.com/watch?v=vwyZH85NQC4'},
    {'title':'Avatar', 'hardcoded_trailer_youtube_url':'https://www.youtube.com/watch?v=-9ceBgWV8io'},
    {'title':'School of Rock', 'hardcoded_trailer_youtube_url':'https://www.youtube.com/watch?v=3PsUJFEBC74'},
    {'title':'Ratatouille', 'hardcoded_trailer_youtube_url':'https://www.youtube.com/watch?v=c3sBBRxDAqk'},
    {'title':'Midnight in Paris', 'hardcoded_trailer_youtube_url':'https://www.youtube.com/watch?v=atLg2wQQxvU'},
    {'title':'The Dark Knight Rises', 'hardcoded_trailer_youtube_url':'https://www.youtube.com/watch?v=9l3DDSXkEQ0'},
    {'title':'The Dark Knight', 'hardcoded_trailer_youtube_url':'https://www.youtube.com/watch?v=9l3DDSXkEQ0'},
    {'title':'Big Trouble In Little China', 'hardcoded_trailer_youtube_url':'https://www.youtube.com/watch?v=592EiTD2Hgo'},
    {'title':'Footloose'},
    {'title':'Miss Congeniality'},
    {'title':'Inside Out'},
    {'title':'House of Cards'},
    {'title':'Star Trek'}
]

movies_dict = {}

for movie in movies_to_load:
    key = movie['title'].lower()
    if 'hardcoded_trailer_youtube_url' in movie:
        hardcoded_trailer_youtube_url = movie['hardcoded_trailer_youtube_url']
    else:
        hardcoded_trailer_youtube_url = ''

    if key in movies_cache:
        movies_dict[key] = movies_cache[key]
        print('CACHE HIT: ' + key)
    else:
        movies_dict[key] = populate_media_movie(key, hardcoded_trailer_youtube_url)
        print('NON-CACHE HIT: ' + key)
###############################################################################

save_movie_cache(movies_dict)

###############################################################################
# Give the front-end UI the data it wants and launch it.
movies = movies_dict.values()
fresh_tomatoes.open_movies_page(movies)
###############################################################################
