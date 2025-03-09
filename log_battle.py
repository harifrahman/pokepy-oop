from pokemon import Pokemon

class LogBattle:

  @staticmethod
  def display_game_start():
    return """
    =======================================
    ==           POKEPY Battle           ==
    =======================================

    Please input pokemon data with this order (max 6 input):
    Pokemon A: 
    1. Name
    2. Attack point
    3. Health point

    Pokemon B:
    4. Name
    5. Attack point
    6. Health point

    """

  @staticmethod
  def display_stage(stage_counter):
    return "\n=============== STAGE " + str(stage_counter) + " =============="

  def display_info(self, defending_pokemon, attacking_pokemon):
    def_HP = defending_pokemon.get_HP()
    att_name = attacking_pokemon.get_name()
    display_info = f"{att_name} attacks! {defending_pokemon.get_name()} has {def_HP} HP left."
    return display_info
  
  @staticmethod
  def display_winner(winner_pokemon):
    display_winner = f"{winner_pokemon.get_name()} won! with {winner_pokemon.get_HP()} HP left"
    return display_winner
