import unittest
from unittest.mock import patch
from game_engine import GameEngine
from log_battle import LogBattle as Log
from pokemon import Pokemon

class TestGameEngine(unittest.TestCase):

  def setUp(self):
    self.game_engine = GameEngine(Log(), Pokemon)

  @patch('builtins.input', side_effect=['Pikachu', '50', '20', 'Charmander', '60', '30'])
  @patch('builtins.print')
  def test_start_game_engine(self, mock_print, mock_input):
      winner = self.game_engine.start_game_engine()

      # Check if the game start message was printed
      mock_print.assert_any_call(self.game_engine.log.display_game_start())

      # Check if the initial Pokémon info was printed
      expected_pokemon1_info = "\n  Pokemon 1 info:\n  Name: Pikachu\n  HP: 50\n  AP: 20\n  "
      expected_pokemon2_info = "\n  Pokemon 2 info:\n  Name: Charmander\n  HP: 60\n  AP: 30\n  "
      mock_print.assert_any_call(expected_pokemon1_info)
      mock_print.assert_any_call(expected_pokemon2_info)
      
      # # Check if the stage info was printed
      mock_print.assert_any_call(self.game_engine.log.display_stage(1))

      # # Check if the fight info was printed
      mock_print.assert_any_call(self.game_engine.log.display_info(self.game_engine.pokemon2, self.game_engine.pokemon1))
      mock_print.assert_any_call(self.game_engine.log.display_info(self.game_engine.pokemon1, self.game_engine.pokemon2))

      # # Check if the winner was printed
      expected_display_winner = "Charmander won! with 20 HP left"
      mock_print.assert_any_call(expected_display_winner)

      self.assertEqual(self.game_engine.pokemon2, winner)
      self.assertEqual("Charmander", winner.get_name())

if __name__ == '__main__':
    unittest.main()