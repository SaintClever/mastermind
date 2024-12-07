import os
import requests
from rich.console import Console

class Mastermind():
  # set up
  def __init__(self, game_loop = 10):
    self.console = Console
    self.pin = "\u2686"
    self.attempts = []

  def request(self):
    # response = request.get("https://www.random.org/integers/?num=4&min=0&max=7&col=1&base=10&format=plain&rnd=new")
    # cipher = response.text.replace("\n", " ").split()
    # return cipher
    
    cipher = ["0", "1", "3", "5"]
    return cipher

  def clear_screen(self):
     os.system('cls' if os.name == 'nt' else 'clear')

  
if __name__ == "__main__":
  game = Mastermind()
  print(game)