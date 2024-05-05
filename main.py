from random import randint
from settings import Settings

class Main:
  def __init__(self, teams):
    self.teams = teams
    self.classified = []
    Settings.check_os()

  def random_value(self, max):
    return randint(0, max)
  
  def goals(self, max):
    return self.random_value(max), self.random_value(max)
  
  def print_game(self, t1, t2, st1, st2):
    print(f"{t1} | {st1} - {st2} | {t2}")
  
  def game(self, t1, t2):
    score_t1, score_t2 = self.goals(5)

    if score_t1 == score_t2:
      while True:
        score_t1, score_t2 = self.goals(5)
        if score_t1 != score_t2:
          break
    
    if score_t1 > score_t2:
      self.print_game(t1, t2, score_t1, score_t2)
      return t1
    else:
      self.print_game(t1, t2, score_t1, score_t2)
      return t2
    
  def championship_round(self):
    if len(self.teams) > 2:
      while True:
        self.classified.append(self.game(self.teams[0], self.teams[1]))
        
        self.teams.pop(0)
        self.teams.pop(0)
        if len(self.teams) == 0:
          break
    else:
      print("\n--- Final ---")
      self.classified.append(self.game(self.teams[0], self.teams[1]))
      print(f'{self.classified[0]} wins the tournament!')

    self.teams = self.classified
    self.classified = []


  def check_tournament_size(self):

  
    if len(self.teams) == 2:
      self.championship_round()
    elif len(self.teams) == 4:
      print("\n--- Semifinals ---")
      self.championship_round()
      self.championship_round()
    elif len(self.teams) == 8:
      print("\n--- Quarterfinals ---")
      self.championship_round()
      print("\n--- Semifinals ---")
      self.championship_round()
      self.championship_round()
    elif len(self.teams) == 16:
      print("\n--- Round of 16 ---")
      self.championship_round()
      print("\n--- Quarterfinals ---")
      self.championship_round()
      print("\n--- Semifinals ---")
      self.championship_round()
      self.championship_round()
    else:
      print("Tournament is over!")

if __name__ == "__main__":
  teams = ["Man City", "Man Utd", "Liverpool", "Chelsea", "Arsenal", "Spurs", "Wolves", "Aston Villa"]
  play = Main(teams)
  play.check_tournament_size()
