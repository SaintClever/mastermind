import os
import requests
from rich.console import Console

console = Console()


# Request made to API
# response = requests.get("https://www.random.org/integers/?num=4&min=0&max=7&col=1&base=10&format=plain&rnd=new")

# Format response and store in list
# cipher = response.text.replace("\n", " ").split()

# Game test array
cipher = ["0", "1", "3", "5"]
loop_count = 10

# Game initializes
def game(game_loop):
  # The previously gueesed numbers
  game_attempts = ""

  # Grid
  while game_loop != 0:
    pin = "\u2686"
    grid = game_loop * f"\n|  {pin}   {pin}   {pin}   {pin}  |"
    console.print(f"\nAttempts left: {game_loop}", style="bold red")
    print(grid)
    print(game_attempts)
    game_loop -= 1

    # User Input
    try:
      # print(f"\n{cipher}\n")
      print("To quit or restart the game type: exit")
      user_input = input("Please guess 4 random numbers: ")
      os.system('cls' if os.name == 'nt' else 'clear')

      if user_input == "exit":
        break

      # Check lenght of input, spaces provided, if input is converted is it an int
      if len(user_input) != 7 or " " not in user_input or int != type(int(user_input.replace(" ", ""))):
        console.print(f"{user_input} is incorrect. Please try again. Ex: 8 6 7 5", style="bold red")
        continue
    except:
      print("Game starting over")

    player_guess = user_input.split()

    all_incorrect = []
    correct_number = []
    correct_location = []

    for i in range(len(cipher)):
      # Logic corresponsed to having all entered numbers incorrect
      if player_guess[i] != cipher[i] and player_guess[i] not in cipher:
        all_incorrect.append(player_guess[i])
      # Logic for having a correct number in the cipher but in the incorrect location
      elif player_guess[i] != cipher[i] and  player_guess[i] in cipher:
        correct_number.append(player_guess[i])
      # logic for matching the correct number location
      else:
        correct_location.append(player_guess[i])


    # If a this list exit that means all numbers are correct. WON THE GAME HERE
    if len(all_incorrect) == 4:
      console.print("all incorrect", style="bold red")
    # Else if a correct number exist and a correct location exist we add the items within the list by getting list len for both
    elif correct_number and correct_location:
      if correct_number[0] not in correct_location:
        numbers = len(correct_number) + len(correct_location)
      else:
        numbers = len(correct_location)
      console.print(f"{numbers} correct numbers and {len(correct_location)} correct location", style="bold magenta")
    # If only a correct location exist we just get the lens for both correct numbers and location
    elif correct_number:
      # remove the set of duplicates if the correct number appears multiple times
      numbers = len(list(set(correct_number)))
      console.print(f"{numbers} correct number and {len(correct_location)} correct location", style="bold magenta")
    # For all correct numbers in the right place
    elif correct_location:
      console.print(f"{len(correct_location)} correct number and {len(correct_location)} correct location", style="bold green")
      # Print winner if all numbers and locations match up
      if len(correct_location) == 4 and len(correct_location) == 4:
        console.print(":tada::partying_face: Winner!!! :tada::partying_face:")

    # Add game attempts and attempt count
    game_attempts += f"|  {" ".join(user_input)}  |\n"

  # After breaking out of the loop with quit
  user_input = input("Quit or Restart game [q / r]: ")
  os.system('cls' if os.name == 'nt' else 'clear')

  if user_input.casefold() == "q":
    print("Thanks for playing Mastermind!!!\n")
    print(grid)
    print(game_attempts)
    print(f"\nAnswer: {cipher}\n")
  elif user_input.casefold() == "r":
    game(game_loop = loop_count)
  else:
    exit()

# Game function with count being the length of game
game(loop_count)