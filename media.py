import webbrowser
import requests
import urllib


class Movie:
    def __init__(self, movie_name, movie_trailer):
        self.trailer_youtube_url = movie_trailer
        self.title = ""
        self.poster_image_url = ""
        self.storyline = ""
        self.imdb_rating = ""
        self.movie_info(movie_name)

    def movie_info(self, title):
        parameter = {'t': title}
        req = requests.get(
            'http://www.omdbapi.com/?plot=short&type=movie&r=json&' +
            str(urllib.urlencode(parameter)))
        self.title = str(req.json()['Title'])
        self.poster_image_url = str(req.json()['Poster'])
        self.storyline = str(req.json()['Plot'])
        self.imdb_rating = str(req.json()['imdbRating'])

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
