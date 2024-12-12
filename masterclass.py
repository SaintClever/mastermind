import os
import requests
from rich.console import Console

class Mastermind():
  # set up
  def __init__(self, game_loop = 10):
    self.console = Console()
    self.pin = "\u2686"
    self.attempts = game_loop

  def request(self):
    # response = request.get("https://www.random.org/integers/?num=4&min=0&max=7&col=1&base=10&format=plain&rnd=new")
    # cipher = response.text.replace("\n", " ").split()
    # return cipher
    
    cipher = ["0", "1", "3", "5"]
    return cipher


  def game_dislplay(self):
    self.console.print(f"\n Attempst left: {self.attempts}", style="bold red")
    grid = self.attempts * f"\n|  {self.pin}  {self.pin}  {self.pin}  {self.pin}  |"
    print(grid)
    self.attempts -= 1

  def clear_terminal(self):
     os.system('cls' if os.name == 'nt' else 'clear')


  def start_game(self):
    remaining_attempts = self.attempts
    self.clear_terminal()

    while remaining_attempts != 0:
      self.game_dislplay()
      player_guess = input("input: ").strip()
      
      if player_guess.casefold() == "exit":
        break
      elif len(player_guess) != 7 \
        or " " not in player_guess \
        or int != type(int(player_guess.replace(" ", ""))):
        self.console.print(f"{player_guess} is incorrect. Please try again. Ex: 8 6 7 5", style="bold red")
        continue
      else:
        self.cipher_logic(player_guess.split())

  def cipher_logic(self, player_guess):
    cipher = self.request()

    for i in range(len(cipher)):
      if player_guess[i] != cipher[i] and player_guess[i] not in cipher:
        print(player_guess)
      
    guesses += f"| {" ".join(player_guess)} |\n"
    print(gueesed)

if __name__ == "__main__":
  game = Mastermind()
  game.start_game()