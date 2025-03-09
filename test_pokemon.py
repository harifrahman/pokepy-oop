import unittest
from pokemon import Pokemon

class TestPokemon(unittest.TestCase):
  
  def setUp(self):
    self.magikarp = Pokemon("Magikarp", 20, 60)
    self.charmander = Pokemon("Charmander", 30, 50)

  def test_fight(self):
        Pokemon.fight(self.charmander, self.magikarp)
        self.assertEqual(self.charmander.get_HP(), 30)

  def test_is_defeated(self):
      self.magikarp.set_HP(0)
      self.assertTrue(Pokemon.is_defeated(self.magikarp))

if __name__ == '__main__':
    unittest.main()


# how to run > python -m unittest test_pokemon.py