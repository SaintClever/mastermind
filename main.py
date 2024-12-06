import os
import requests


# Request made to API
# response = requests.get("https://www.random.org/integers/?num=4&min=0&max=7&col=1&base=10&format=plain&rnd=new")

# Format response and store in list
# cipher = response.text.replace("\n", " ").split()

# Game test array
cipher = ["0", "1", "3", "5"]


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
    print(f"\nAttempts left: {game_loop}")
    print(grid)
    print(game_attempts)
    game_loop -= 1

    print(f"\n{cipher}\n")
    print("To end game type: exit")

    # User Input
    try:
      user_input = input("Please guess 4 random numbers: ")
      os.system('cls' if os.name == 'nt' else 'clear')

      if user_input == "exit":
        break

      # Check lenght of input, spaces provided, if input is converted is it an int
      if len(user_input) != 7 or " " not in user_input or int != type(int(user_input.replace(" ", ""))):
        print(f"{user_input} is incorrect. Please try again. Ex: 8 6 7 5")
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
        correct_number += player_guess[i]
        correct_number_list = list(correct_number)

      # logic for matching the the correction number location
      elif player_guess[i] == cipher[i]:
        correct_number_and_location += player_guess[i]
        correct_number_and_location_list = list(correct_number_and_location)

        # however if the locations or greater than one that eventually means the number matches as well?
        if len(correct_number_and_location) > 1:
          correct_number_and_location_list = list(correct_number_and_location)

    # # For testing output
    # print("a", all_incorrect)
    # print("b", correct_number)
    # print("c", correct_location)
    # print("d", correct_number_and_location)

    print("e", all_incorrect_list)
    print("f", correct_number_list)
    print("g", correct_location_list)
    print("h", correct_number_and_location_list)

    # Clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    if all_incorrect_list:
      print("all incorrect")

    elif correct_number_list and correct_number_and_location_list:
      print(f"a {len(correct_number_list) + len(correct_number_and_location_list)} correct numbers and {len(correct_number_and_location_list)} correct location")

    elif correct_number_list:
      # correct_number_list[0] should all have the same number so I only need the first one
      print(f"b {len(correct_number_list)} correct number and {len(correct_number_and_location_list)} correct location")

    elif correct_number_and_location_list:
      print(f"c {len(correct_number_and_location_list)} correct number and {len(correct_number_and_location_list)} correct location")
    
    # Add game attempts and attempt count
    game_attempts += f"|  {" ".join(user_input)}  |\n"
    attempt_count += 1


  print("Thanks for playing Mastermind!!!\n")
  # print("The player had guess a correct number")
  # print("The player had guessed a correct number and its correct location")
  # print("The player’s guess was incorrect")

# Game function with count being the length of game
count = 10
game(count)