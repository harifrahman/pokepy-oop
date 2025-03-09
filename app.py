from game_engine import GameEngine
from log_battle import LogBattle as Log
from pokemon import Pokemon

def main():
    game_engine = GameEngine(Log(), Pokemon)
    game_engine.start_game_engine()

if __name__ == "__main__":
    main()