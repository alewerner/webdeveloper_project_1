import media
import fresh_tomatoes


def run():
        """
        Generates a and opens a html page in a web browser
        containing my favorite movies via fresh_tomatoes.py file
        pass the arguments: get_movies_list -- contains a list of
        movies and their
        parameters: movie title, storyline, poster image and movie trailer
        pass the tittle of the web page
        """
        fresh_tomatoes.open_movies_page(
            get_movies_list(),
            "My Top Movies - Provided by Python + HTML + CSS"
        )


def get_movies_list():
    """

    :return: load a list of movies to be loaded in run() function
    """
    # to load a movie, please complete this parameters: movie tittle,
    # storyline, poster image and movie trailer
    return[media.Movie("Toy Story",
                       "a story of a boy and hist toys that come to life",
                       "http://www.animated247.com/wp-content/uploads/2014/05/Toy-Story.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc"),

           media.Movie("Goodfellas",
                       "The film narrates the rise and fall of mob "
                       "associate Henry Hill and his friends and family"
                       " from 1955 to 1980.",
                       "https://upload.wikimedia.org/wikipedia/pt/7/7c/GoodfellasPoster.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=2ilzidi_J8Q"),

           media.Movie("The Lord of the Rings: The Fellowship of the Ring",
                       "Set in Middle-earth, the story tells of the Dark Lord"
                       " Sauron, who is seeking the One Ring. The Ring has "
                       "found its way to the young hobbit Frodo Baggins."
                       " The fate of Middle-earth hangs in the balance as"
                       " Frodo and eight companions who form the Fellowship"
                       " of the Ring begin their journey to Mount Doom "
                       "in the land of Mordor, the only place where "
                       "the Ring can be destroyed.",
                       "https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=V75dMMIW2B4"),

           media.Movie("Harry Potter and the Sorcere's Stone",
                       " Its story follows Harry Potter's first year at "
                       "Hogwarts School of Witchcraft and Wizardry as he "
                       "discovers that he is a famous wizard and "
                       "begins his education.",
                       "https://upload.wikimedia.org/wikipedia/en/7/7a/Harry_Potter_and_the_Philosopher%27s_Stone_banner.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=VyHV0BRtdxo"),

           media.Movie("Pirates of Silicon Valley",
                       "it explores the impact of the rivalry between "
                       "Jobs (Apple Computer) and Gates (Microsoft) on "
                       "the development of the personal computer.",
                       "https://upload.wikimedia.org/wikipedia/en/3/30/Movieposterposv.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=lEyrivrjAuU"),

           media.Movie("The Patriot",
                       "The film takes place during the events of the "
                       "Southern theater of the American Revolutionary War",
                       "https://upload.wikimedia.org/wikipedia/en/6/68/Patriot_promo_poster.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=_comGBmnYew")]


run()
