from project.movie import Movie
from unittest import TestCase, main

class TestMovie(TestCase):

    def setUp(self):
        self.movie = Movie("some name", 1987, 5.5)

    def test_initialization(self):
        self.assertIsInstance(self.movie.name, str)
        self.assertEqual(self.movie.name, "some name")
        self.assertIsInstance(self.movie.year, int)
        self.assertEqual(self.movie.year, 1987)
        self.assertIsInstance(self.movie.rating, float)
        self.assertEqual(self.movie.rating, 5.5)
        self.assertIsInstance(self.movie.actors, list)
        self.assertEqual(self.movie.actors, [])

    def test_set_name_with_empty_string_value_error_msg(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ""
        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_name_correctly(self):
        self.movie.name = "somename"
        self.assertEqual(self.movie.name, "somename")

    def test_set_year_with_year_before_1887_value_error_msg(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1886
        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_set_year_correctly(self):
        self.movie.year = 2000
        self.assertEqual(self.movie.year, 2000)

    def test_add_actor_with_new_actor(self):
        self.movie.add_actor("actor")
        self.assertEqual(self.movie.actors[0], "actor")

    def test_add_actor_with_already_added_actor(self):
        self.movie.add_actor("actor")
        result = self.movie.add_actor("actor")
        self.assertEqual(result, f"actor is already added in the list of actors!")

    def test_actors_rating_bigger_or_smaller(self):
        self.movie2 = Movie("second movie", 2000, 8.3)
        self.movie3 = Movie("third movie", 2000, 9.5)
        result = self.movie > self.movie2
        result2 = self.movie3 > self.movie
        self.assertEqual(result, '"second movie" is better than "some name"')
        self.assertEqual(result2, '"third movie" is better than "some name"')

    def test_pepr_dunder_method(self):
        self.movie.add_actor("AZ")
        self.movie.add_actor("TI")
        self.assertEqual(self.movie.__repr__(), "Name: some name\n"
                                                "Year of Release: 1987\n"
                                                "Rating: 5.50\n"
                                                "Cast: AZ, TI")


if __name__ == '__main__':
    main()