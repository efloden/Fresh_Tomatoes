import media
import fresh_tomatoes

# Populating Movie classes
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar",
                        "A marine on an alien planet",
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")
school_of_rock = media.Movie("School of Rock",
                        "Using rock music to learn",
                        "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                        "https://www.youtube.com/watch?v=XCwy6lW5Ixc")
ratatouille = media.Movie("Ratatouille",
                        "A rat is a chef in Paris",
                        "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                        "https://www.youtube.com/watch?v=c3sBBRxDAqk")
midnight_in_paris = media.Movie("Midnight in Paris",
                        "Going back in time to meet authors",
                        "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                        "https://www.youtube.com/watch?v=FAfR8omt-CY")
hunger_games = media.Movie("Hunger Games",
                        "A really real reality show",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/4/42/HungerGamesPoster.jpg/220px-HungerGamesPoster.jpg",
                        "https://www.youtube.com/watch?v=4S9a5V9ODuY")
suicide_squad = media.Movie("Suicide Squad",
                        "The worst heroes imaginable",
                        "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQIxQn3FcPf59csggeuklfLoLc5HwDP2PEENvh1C5RHh-7lWHfY",
                        "https://www.youtube.com/watch?v=CmRih_VtVAs")
# List of the movie data structures
movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games, suicide_squad]

# Takes the movies list and generates the web page through the open_movies_page method in fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)
