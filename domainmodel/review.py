from datetime import datetime

from domainmodel.movie import Movie


class Review:

    def __init__(self, movie: Movie, review_text: str, rating: int):
        self._movie: Movie = movie
        self._review_text: str = review_text
        if rating < 1 or rating > 10 or type(rating) is not int:
            self._rating = None
        else:
            self._rating: int = rating
        self._timestamp = datetime.today()

    def __repr__(self):
        return f"<Review: {self._review_text}>"

    def __eq__(self, other):
        if type(other) is not Review:
            return False
        else:
            return self._movie == other.movie and self._review_text == other.review_text and self._rating == other.rating and self._timestamp == other.timestamp


    @property
    def movie(self) -> Movie:
        return self._movie

    @property
    def review_text(self) -> str:
        return self._review_text

    @property
    def rating(self) -> int:
        return self._rating

    @property
    def timestamp(self):
        return self._timestamp


