from domainmodel.movie import Movie


class WatchList:
    def __init__(self):
        self.__watch_list = []

    def __repr__(self):
        return f"<WatchList {self.__watch_list}>"

    def __eq__(self, other):
        return self.__watch_list == other.watch_list

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.__watch_list):
            movie = self.__watch_list[self.n]
            self.n += 1
            return movie
        else:
            raise StopIteration

    def add_movie(self, movie: Movie):
        if movie not in self.__watch_list:
            self.__watch_list.append(movie)

    def remove_movie(self, movie: Movie):
        if movie in self.__watch_list:
            self.__watch_list.remove(movie)

    def select_movie_to_watch(self, index):
        if index < 0 or index >= len(self.__watch_list):
            return None
        else:
            return self.__watch_list[index]

    def size(self):
        return len(self.__watch_list)

    def first_movie_in_watchlist(self):
        if len(self.__watch_list) == 0:
            return None
        else:
            return self.__watch_list[0]






