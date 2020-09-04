from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director

class Movie:

    def __init__(self, title: str, release_year: int):
        if title == "" or type(title) is not str:
            self.__title = None
        else:
            self.__title = title.strip()
        if release_year < 1900 or release_year == "" or type(release_year) is not int:
            self.__release_year = None
        else:
            self.__release_year = release_year
        self.__description = ""
        self.__director = None
        self.__actors = []
        self.__genres = []
        self.__runtime_minutes = None

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        if title == "" or type(title) is not str:
            self.__title = None
        else:
            self.__title = title.strip()

    @property
    def release_year(self) -> int:
        return self.__release_year

    @release_year.setter
    def release_year(self, release_year: int):
        if release_year < 1900 or release_year == "" or type(release_year) is not int:
            self.__release_year = None
        else:
            self.__release_year = release_year

    def __repr__(self):
        return f"<Movie {self.__title}, {self.__release_year}>"

    def __eq__(self, other):
        self_title_and_release = self.__title + str(self.__release_year)
        other_title_and_release = other.__title + str(other.__release_year)
        return self_title_and_release == other_title_and_release

    def __lt__(self, other):
        self_title_and_release = self.__title + str(self.__release_year)
        other_title_and_release = other.__title + str(other.__release_year)
        return self_title_and_release < other_title_and_release

    def __hash__(self):
        return hash(self.__title + str(self.__release_year))

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        if description == "" or type(description) is not str:
            self.__description = None
        else:
            self.__description = description.strip()

    @property
    def director(self):
        return self.__director

    @director.setter
    def director(self, director: Director):
        if type(director) == Director:
            self.__director = director

    @property
    def actors(self):
        return self.__actors

    @actors.setter
    def actors(self, actors):
        if type(actors) == list:
            self.__actors = actors

    @property
    def genres(self):
        return self.__genres

    @genres.setter
    def genres(self, genres):
        if type(genres) == list:
            self.__genres = genres

    @property
    def runtime_minutes(self) -> int:
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, runtime_minutes):
        if type(runtime_minutes) is not int or runtime_minutes < 0:
            raise ValueError
        else:
            self.__runtime_minutes = runtime_minutes

    def add_actor(self, actor: Actor):
        self.__actors.append(actor)

    def remove_actor(self, actor: Actor):
        if actor in self.__actors:
            index = self.__actors.index(actor)
            self.__actors.pop(index)

    def add_genre(self, genre: Genre):
        self.__genres.append(genre)

    def remove_genre(self, genre: Genre):
        if genre in self.__genres:
            index = self.__genres.index(genre)
            self.__genres.pop(index)

