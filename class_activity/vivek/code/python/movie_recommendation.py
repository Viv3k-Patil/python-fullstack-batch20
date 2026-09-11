

# ["movie1", "movie2", "movie3"]

class MovieRecIter:
    def __init__(self, movies):
        self.movies = movies
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.movies):
            raise StopIteration

        movie = self.movies[self.index]
        self.index += 1

        return movie

movies_list = ["movie1", "movie2", "movie3"]
a = MovieRecIter(movies_list)
for i in a:
    print(i)