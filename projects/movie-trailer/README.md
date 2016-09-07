This is my movie trailer project for the  **Programming Foundations with Python** course at [Udacity](https://www.udacity.com).

*Note: I chose to use python3 instead of python2*

# Features
* Serves movie trailers of some of my favourite movies
* Dynamically displays movie, plot, and trailer
* Embedded trailer viewing
* Movie data obtained via the public imdbapi
* Caches previously loaded movies

## Usage (and modification)
You can add extra content by modifying 'movies_to_load.json'. This is the list which is used to determine what movies to load. It will load movies from the cache if they exist, otherwise the app will attempt to retrieve data from [omdbapi](http://www.omdbapi.com) and [trailersapi](http://trailersapi.com).

 ### Python3 Modules
 * json
 * re
 * urllib.request
 * webbrowser

 ### Web APIs Used
 * [omdbapi](http://www.omdbapi.com)
 * [trailersapi](http://trailersapi.com)

# Source Code
This project is located in my udacity github repo, in the projects/movie-trailer folder.
```
git clone https://github.com/elam03/udacity
```

# Requirements
* Python 3.4.3 (or above) [Download link](https://www.python.org/downloads/release/python-343)

# Known issues/bugs/limitations
* The use of the external api [trailersapi](http://trailersapi.com) is experimental so there may be inherited issues with the association
* Movies that cannot be found in either of the apis may not display correctly; a fair amount of time the trailersapi finds similarly named movies...

# Quick Start
```
git clone https://github.com/elam03/udacity ~/elam_udacity_path
cd ~/elam_udacity_path/movies/movie-trailer
python3 entertainment_center.py
```
