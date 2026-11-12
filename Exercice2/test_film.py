
import unittest
from film import Film


class TestFilm(unittest.TestCase):

    def setUp(self):
        self.film = Film("Titanic", "James Cameron", 1997, 9.5)

    def test_creation(self):
        self.assertEqual(self.film.titre, "Titanic")

    def test_est_classique(self):
        self.assertTrue(self.film.est_classique())

    def test_non_classique(self):
        film = Film("Inception", "Christopher Nolan", 2010, 9.0)
        self.assertFalse(film.est_classique())

    def test_note_invalide(self):
        with self.assertRaises(ValueError):
            Film("Film", "Realisateur", 2020, 12)

    def test_titre_vide(self):
        with self.assertRaises(ValueError):
            Film("", "Realisateur", 2020, 8.0)

    def test_type_note_invalide(self):
        with self.assertRaises(TypeError):
            Film("Film", "Realisateur", 2020, "8")

    def test_immutabilite(self):
        with self.assertRaises(AttributeError):
            self.film.note = 7.0

    def test_json(self):
        data = self.film.to_json()
        film_recree = Film.from_json(data)
        self.assertEqual(self.film, film_recree)


if __name__ == "__main__":
    unittest.main()
