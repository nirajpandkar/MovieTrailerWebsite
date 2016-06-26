import webbrowser
import requests
from bs4 import BeautifulSoup

class Movie:
    """
    Methods:
            movie_info(movie_name): obtains information(title,
            poster_image_url, storyline, imdb_rating, directors and stars)

            trailer_url(movie_name): used to get the youtube movie trailer

            show_trailer(): opens the browser and shows the movie trailer
    """
    def __init__(self, movie_name):
        # initialized the object variables
        self.trailer_youtube_url = ""
        self.title = ""
        self.poster_image_url = ""
        self.storyline = ""
        self.imdb_rating = ""
        self.directors = ""
        self.stars = ""
        self.movie_info(movie_name)  # get all the movie information
        self.trailer_youtube_url = self.trailer_url(movie_name)
        # get the movie trailer url

    def movie_info(self, title):
        # make a get request which then returns a response in JSON
        resp = requests.get('http://www.omdbapi.com/', params={
            't': title,
            'type': 'movie',
            'plot': 'short'
        })
        # handle the JSON response and obtain required information
        self.title = str(resp.json()['Title'])
        self.poster_image_url = str(resp.json()['Poster'])
        self.storyline = str(resp.json()['Plot'])
        self.imdb_rating = str(resp.json()['imdbRating'])
        self.directors = str(resp.json()['Director'])
        self.stars = str(resp.json()['Actors'])

    def trailer_url(self, title):
        # perform a youtube search with the movie title for movie trailer
        response = requests.get("https://youtube.com/results", params={
            'search_query': title + " trailer"
        })

        soup = BeautifulSoup(response.content, "html.parser")   # returns a
        # prettified version of the html

        # search for the div element with the provided class to return
        # the youtube trailer link
        for video in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
            return "https://youtube.com" + video["href"]

    def show_trailer(self):
        # function to fireup the trailer after clicking
        webbrowser.open(self.trailer_youtube_url)
print Movie.__doc__
