import fresh_tomatoes
import json
import media
import re
import urllib.request

# This is a helper method to retrieve data from various apis.
def get_movie_info(name, get_trailer_from_trailersapi=False):
    # Obtain data from omdbapi first.
    parsed_movie_name = name.replace(' ', '%20')
    connection = urllib.request.urlopen('http://www.omdbapi.com/?t=' + parsed_movie_name)
    data = json.loads(connection.read().decode('utf8'))
    connection.close()

    if connection.getcode() is not 200:
        return None

    if 'Title' not in data:
        return None

    # Obtain data from trailersapi (experimental)
    if get_trailer_from_trailersapi:
        trailer_connection = urllib.request.urlopen('http://trailersapi.com/trailers.json?movie=' + parsed_movie_name)
        trailer_data = trailer_connection.read().decode('utf8')

        if re.search(name.lower(), trailer_data.lower()) is not None:
            trailer_data = re.split(r'embed', trailer_data)
            trailer_data = re.split(r'\\', trailer_data[1])
            trailer_data = re.split(r'/', trailer_data[1])
            trailer_data = trailer_data[1]
            trailer_connection.close()

            data['Trailer'] = 'https://www.youtube.com/watch?v=' + trailer_data
            print('Found a trailer for ' + name + '! This is my best guess! ' + data['Trailer'])
        else:
            print('Failed to find a trailer for ' + name + '!')

    return data


# Create and populate a Movie object. If there's no manual movie trailer link,
# then attempt to populate the trailer link using trailersapi.
def populate_media_movie(movie_name, manual_movie_trailer_link = ''):
    if manual_movie_trailer_link:
        check_trailersapi = False
    else:
        check_trailersapi = True

    movie = get_movie_info(movie_name, check_trailersapi)

    if movie is None:
        return None
    else:
        if manual_movie_trailer_link:
            trailer = manual_movie_trailer_link
        elif 'Trailer' in movie:
            trailer = movie['Trailer']
        else:
            trailer = ''

        return media.Movie(
            movie['Title'],
            movie['Plot'],
            movie['Poster'],
            trailer)

def check_which_movies_to_load():
    try:
        with open('movies_to_load.json') as json_file:
            data = json.load(json_file)
            movies_to_load = data['movies_to_load']
            print(str(movies_to_load))

        return movies_to_load
    except:
        error = '''
        Please populate movies_to_load.json! i.e:
        {
            "movies_to_load":[
                {"title":"Deadpool", "hardcoded_trailer_youtube_url":"https://www.youtube.com/watch?v=ONHBaC-pfsk"},
                {"title":"<<<Your movie>>>", "hardcoded_trailer_youtube_url":"<<<some youtube link here>>>"}
            ]
        }
        '''
        print(error)
        exit()

def load_movie_cache():
    cache = dict()

    try:
        with open('movie_cache.json') as json_file:
            movie_cache = json.load(json_file)

            for movie in movie_cache:
                cache[movie['title'].lower()] = media.Movie(movie['title'], movie['storyline'], movie['poster_image_url'], movie['trailer_youtube_url'])
    except:
        print('No cache detected.')

    return cache

def save_movie_cache(movies_dict):
    with open('movie_cache.json', 'w') as json_file:
        json.dump([m.__dict__ for m in movies_dict.values()], json_file, indent = 4)

###############################################################################

movies_cache = load_movie_cache()

###############################################################################
# Load all the movies from the list, but skip over previously loaded movies.
movies_to_load = check_which_movies_to_load()

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
        m = populate_media_movie(key, hardcoded_trailer_youtube_url)
        if m is None:
            print('NON-CACHE HIT: Cannot find data for \'' + key + '\'!')
        else:
            movies_dict[key] = m
            print('NON-CACHE HIT: ' + key)
###############################################################################

save_movie_cache(movies_dict)

###############################################################################
# Give the front-end UI the data it wants and launch it.
movies = movies_dict.values()
fresh_tomatoes.open_movies_page(movies)
###############################################################################
