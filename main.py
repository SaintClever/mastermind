import os
import requests
from rich.console import Console

console = Console()


# Request made to API
response = requests.get("https://www.random.org/integers/?num=4&min=0&max=7&col=1&base=10&format=plain&rnd=new")

# Format response and store in list
cipher = response.text.replace("\n", " ").split()

# Game test array
# cipher = ["0", "1", "3", "5"]
loop_count = 10

# Game initializes
def game(game_loop):
  # Number of left attempts to win
  attempt_count = 1
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

    # print(f"\n{cipher}\n")
    print("To quit or restart the game type: exit")

    # User Input
    try:
      user_input = input("Please guess 4 random numbers: ")
      os.system('cls' if os.name == 'nt' else 'clear')

      if user_input == "exit":
        break

      # Check lenght of input, spaces provided, if input is converted is it an int
      if len(user_input) != 7 or " " not in user_input or int != type(int(user_input.replace(" ", ""))):
        console.print(f"{user_input} is incorrect. Please try again. Ex: 8 6 7 5", style="bold red")
        game(game_loop)
    except:
      print("Game starting over")

    player_guess = user_input.split()

    all_incorrect = ""
    correct_number = ""
    correct_location = ""
    correct_number_and_location = ""

    all_incorrect_list = []
    correct_number_list = []
    correct_location_list = []
    correct_number_and_location_list = []

    for i in range(len(cipher)):
      # Logic corresponsed to having all entered numbers incorrect
      if player_guess[i] != cipher[i] and player_guess[i] not in cipher:
        all_incorrect += player_guess[i]
        
        if len(all_incorrect) == len(cipher):
          all_incorrect_list = list(all_incorrect)

      # Logic for having a correct number in the cipher but in the incorrect location
      elif player_guess[i] in cipher and player_guess[i] != cipher[i]:
        # correct_number += player_guess[i]
        # correct_number_list = list(correct_number)
        correct_number_list.append(player_guess[i])

      # logic for matching the correct number location
      elif player_guess[i] == cipher[i]:
        # correct_number_and_location += player_guess[i]
        # correct_number_and_location_list = list(correct_number_and_location)
        correct_number_and_location_list.append(player_guess[i])

        # however if the locations or greater than one that eventually means the number matches as well?
        if len(correct_number_and_location) > 1:
          # correct_number_and_location_list = list(correct_number_and_location)
          correct_number_and_location_list.append(player_guess[i])

    # # For testing output
    # print("a", all_incorrect)
    # print("b", correct_number)
    # print("c", correct_location)
    # print("d", correct_number_and_location)

    # print("e", all_incorrect_list)
    # print("f", correct_number_list)
    # print("g", correct_location_list)
    # print("h", correct_number_and_location_list)

    # Clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    # If a this list exit that means all numbers are correct. WON THE GAME HERE
    if all_incorrect_list:
      console.print("all incorrect", style="bold red")

    # Else if a correct number exist and a correct location exist we add the items within the list by getting list len for both
    elif correct_number_list and correct_number_and_location_list:

      if correct_number_list[0] not in correct_number_and_location_list:
        numbers = len(correct_number_list) + len(correct_number_and_location_list)
      else:
        numbers = len(correct_number_and_location_list)

      console.print(f"{numbers} correct numbers and {len(correct_number_and_location_list)} correct location", style="bold magenta")

    # If only a correct location exist we just get the lens for both correct numbers and location
    elif correct_number_list:
      # remove the set of duplicates if the correct number appears multiple times
      numbers = len(list(set(correct_number_list)))
      console.print(f"{numbers} correct number and {len(correct_number_and_location_list)} correct location", style="bold magenta")

    # For all correct numbers in the right place
    elif correct_number_and_location_list:
      console.print(f"{len(correct_number_and_location_list)} correct number and {len(correct_number_and_location_list)} correct location", style="bold green")

      # Print winner if all numbers and locations match up
      if len(correct_number_and_location_list) == 4 and len(correct_number_and_location_list) == 4:
        console.print(":tada::partying_face: Winner!!! :tada::partying_face:")

    # Add game attempts and attempt count
    game_attempts += f"|  {" ".join(user_input)}  |\n"
    attempt_count += 1

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