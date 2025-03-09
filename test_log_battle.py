import unittest
from log_battle import LogBattle
from pokemon import Pokemon

class TestLogBattle(unittest.TestCase):
  def setUp(self):
    self.magikarp = Pokemon("Magikarp", 20, 60)
    self.charmander = Pokemon("Charmander", 30, 50)
    self.log_battle = LogBattle()
  
  def test_display_stage(self):
    actual = LogBattle.display_stage(1)
    self.assertEqual("\n=============== STAGE 1 ==============", actual)

  def test_display_info(self):
    expected = "Charmander attacks! Magikarp has 60 HP left."
    actual = self.log_battle.display_info(self.magikarp, self.charmander)
    self.assertEqual(expected, actual)

  def test_display_winner(self):
    expected = "Charmander won! with 50 HP left"
    actual = LogBattle.display_winner(self.charmander)
    self.assertEqual(expected, actual)

  def test_display_pokemon_info(self):
    expected = "\n  Pokemon 1 info:\n  Name: Magikarp\n  HP: 60\n  AP: 20\n  "
    actual = LogBattle.display_pokemon_info(self.magikarp, 1)
    self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()