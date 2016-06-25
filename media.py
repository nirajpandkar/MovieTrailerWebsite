import webbrowser
import requests
from bs4 import BeautifulSoup

class Movie:
    def __init__(self, movie_name):
        self.trailer_youtube_url = ""
        self.title = ""
        self.poster_image_url = ""
        self.storyline = ""
        self.imdb_rating = ""
        self.directors = ""
        self.stars = ""
        self.writers = ""
        self.movie_info(movie_name)
        self.trailer_youtube_url = self.trailer_url(movie_name)

    def movie_info(self, title):
        resp = requests.get('http://www.omdbapi.com/', params={
            't': title,
            'type': 'movie',
            'plot': 'short'
        })
        self.title = str(resp.json()['Title'])
        self.poster_image_url = str(resp.json()['Poster'])
        self.storyline = str(resp.json()['Plot'])
        self.imdb_rating = str(resp.json()['imdbRating'])
        self.directors = str(resp.json()['Director'])
        self.writers = str(resp.json()['Writer'])
        self.stars = str(resp.json()['Actors'])

    def trailer_url(self, title):
        response = requests.get("https://youtube.com/results", params={
            'search_query': title + " trailer"
        })

        soup = BeautifulSoup(response.content, "html.parser")

        for video in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
            return "https://youtube.com" + video["href"]

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
