from log_battle import LogBattle as log
from pokemon import Pokemon

class GameEngine:

  def __init__(self, log, pokemon):
    self.log = log
    self.pokemon = pokemon

  def _accept_input(self):
    self.pk_name_1 = input("Pokemon 1 Name: ")
    self.pk_hp_1 = int(input("Pokemon 1 Health Point: "))
    self.pk_ap_1 = int(input("Pokemon 1 Attack Point: "))

    self.pk_name_2 = input("Pokemon 2 Name: ")
    self.pk_hp_2 = int(input("Pokemon 2 Health Point: "))
    self.pk_ap_2 = int(input("Pokemon 2 Attack Point: "))

  def _init_pokemons(self):
    self.pokemon1 = Pokemon(self.pk_name_1, self.pk_ap_1, self.pk_hp_1)
    self.pokemon2 = Pokemon(self.pk_name_2, self.pk_ap_2, self.pk_hp_2)

  def start_game_engine(self):
    stage_counter = 1
    print(log.display_game_start())
    
    self._accept_input()
    self._init_pokemons()

    print(log.display_pokemon_info(self.pokemon1, 1))
    print(log.display_pokemon_info(self.pokemon2, 2))

    while True:
      print(log.display_stage(stage_counter))
      stage_counter += 1

      # pokemon 1 attack pokemon 2
      self.pokemon1.fight(self.pokemon2)
      print(self.log.display_info(self.pokemon2, self.pokemon1))
      if self.pokemon2.is_defeated():
        break

      # pokemon 2 attack pokemon 1
      self.pokemon2.fight(self.pokemon1)
      print(self.log.display_info(self.pokemon1, self.pokemon2))
      if self.pokemon1.is_defeated():
        break
    
    winner = self.pokemon2 if self.pokemon1.is_defeated() else self.pokemon1
    print(log.display_winner(winner))
    
    return winner
