import media
import fresh_tomatoes

penguins_of_madagascar = media.Movie("Penguins Of Madagascar",
                                     "https://youtu.be/retX8Wj7JdM")

epic = media.Movie("Epic", "https://youtu.be/BJVkoq_wK80")

big_hero_6 = media.Movie("Big Hero 6", "https://youtu.be/z3biFxZIJOQ")

home = media.Movie('Home', "https://youtu.be/MyqZf8LiWvM")

kingsman = media.Movie('Kingsman', "https://youtu.be/kl8F-8tR8to")

movies = [penguins_of_madagascar, epic, big_hero_6, home, kingsman]

fresh_tomatoes.open_movies_page(movies)
