import webbrowser


class Movie():
    """
    Documentation: This class provides a way to store movie related
    information and execute a youtube trailer, if the movie had it
    """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """
        This are the parameters of the constructor
        :param movie_title: string
        :param movie_storyline: string
        :param poster_image: string
        :param trailer_youtube: string
        """

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailler(self):
        """
        this function calls the trailer_youtube from the movie
        and reproduces it on the web browser
        :return: a youtube video
        """
        webbrowser.open(self.trailer_youtube_url)
