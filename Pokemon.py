class Pokemon:

  def __init__(self, name, attack_point, health_point):
    self.__name = name
    self.__attack_point = attack_point
    self.__health_point = health_point

  def get_name(self):
    return self.__name

  def get_AP(self):
    return self.__attack_point
  
  def get_HP(self):
    return self.__health_point
  
  def set_HP(self, new_health_point):
    self.__health_point = new_health_point

  def fight(defending_pokemon, attacking_pokemon):
    # attacking_pokemon attacking defending_pokemon
    def_pokemon_new_HP = defending_pokemon.get_HP() - attacking_pokemon.get_AP()
    defending_pokemon.set_HP(def_pokemon_new_HP)

  def is_defeated(pokemon):
    if pokemon.get_HP() <= 0 :
      print(f"{pokemon.get_name()} HP touch 0..")
      return True
    return False 
