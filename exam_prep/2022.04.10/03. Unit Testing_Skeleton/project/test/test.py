from project.movie import Movie
from unittest import TestCase, main

class TestMovie(TestCase):

    def setUp(self):
        self.movie = Movie("some name", 1987, 5.5)

    def test_initialization(self):
        self.assertIsInstance(self.movie.name, str)
        self.assertEqual(self.movie.name, "some name")
        self.assertIsInstance(self.movie.year, int)
        self.assertEqual(self.movie.name, 1987)
        self.assertIsInstance(self.movie.rating, float)
        self.assertEqual(self.movie.name, 5.5)


if __name__ == '__main__':
    main()