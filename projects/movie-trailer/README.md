This is my movie trailer project for the  **Programming Foundations with Python** course at [Udacity](https://www.udacity.com).

*Note: I chose to use python3 instead of python2*

# Features
* Serves movie trailers of some of my favourite movies
* Embedded trailer viewing
* Movie data obtained via the public imdbapi
* Caches previously loaded movies

 ### Python3 Modules
 * json
 * re
 * urllib.request
 * webbrowser

 ### Web APIs Used
 * [omdapi](http://www.omdbapi.com)
 * [trailersapi](http://trailersapi.com)

# Source Code
This project is located in my udacity github repo, in the projects/movie-trailer folder.
```
git clone https://github.com/elam03/udacity
```

# Requirements
* Python 3.4.3 (or above) [Download link](https://www.python.org/downloads/release/python-343)

# Known issues/bugs
* The use of the external api [trailersapi](http://trailersapi.com) is experimental so there may be inherited issues with the association
* Movies that cannot be found in either of the apis may not display correctly

# Quick Start
```
git clone https://github.com/elam03/udacity ~/elam_udacity_path
cd ~/elam_udacity_path/movies/movie-trailer
python3 entertainment_center.py
```
