import unittest
from pokemon import Pokemon

class TestPokemon(unittest.TestCase):
  
  def setUp(self):
    self.magikarp = Pokemon("Magikarp", 20, 60)
    self.charmander = Pokemon("Charmander", 30, 50)

  def test_fight(self):
        self.magikarp.fight(self.charmander)
        self.assertEqual(30, self.charmander.get_HP())

  def test_is_defeated(self):
      self.magikarp.set_HP(0)
      self.assertTrue(self.magikarp.is_defeated())

if __name__ == '__main__':
    unittest.main()


# how to run > python -m unittest test_pokemon.py