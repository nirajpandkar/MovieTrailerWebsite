import media
import movies_view

penguins_of_madagascar = media.Movie('Penguins of madagascar')
epic = media.Movie('Epic')
big_hero_6 = media.Movie('Big Hero 6')
kingsman = media.Movie('Kingsman')
home = media.Movie('Home')
the_lego_movie = media.Movie('The lego movie')
the_social_network = media.Movie('The Social Network')
the_theory_of_everything = media.Movie('The Theory of Everything')

movies = [penguins_of_madagascar, epic, big_hero_6, home, kingsman,
          the_lego_movie, the_social_network, the_theory_of_everything]

movies_view.open_movies_page(movies)
