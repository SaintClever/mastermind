import os
import requests


# Request made to API
# response = requests.get("https://www.random.org/integers/?num=4&min=0&max=7&col=1&base=10&format=plain&rnd=new")

# Format response and store in list
# codemaker = response.text.replace("\n", " ").split()

# Game test array
codemaker = ["0", "1", "3", "5"]


# Game initializes
def game(game_loop):
  attempt_count = 1
  game_attempts = ""

  # Grid
  while game_loop != 0:
    pin = "\u2686"
    grid = game_loop * f"\n|  {pin}   {pin}   {pin}   {pin}  |"
    print(f"\nAttempts left: {game_loop}")
    print(grid)
    print(game_attempts)
    game_loop -= 1

    print(f"\n{codemaker}\n")
    print("To end game type: exit")

    # User Input
    try:
      user_input = input("Please guess 4 random numbers: ")
      os.system('cls' if os.name == 'nt' else 'clear')

      if user_input == "exit":
        break

      if len(user_input) != 7 or " " not in user_input or int not in user_input:
        print(f"{user_input} is incorrect. Please try again. Ex: 8 6 7 5")
        game(game_loop)
    except:
      print("Game starting over")

    codebreaker = user_input.split()

    all_incorrect = ""
    correct_number = ""
    correct_location = ""
    correct_number_and_location = ""

    all_incorrect_list = []
    correct_number_list = []
    correct_location_list = []
    correct_number_and_location_list = []

    for i in range(len(codemaker)):
      if codebreaker[i] != codemaker[i] and codebreaker[i] not in codemaker:
        all_incorrect += codebreaker[i]
        
        if len(all_incorrect) == len(codemaker):
          all_incorrect_list = list(all_incorrect)

      elif codebreaker[i] in codemaker and codebreaker[i] != codemaker[i]:
        correct_number += codebreaker[i]
        correct_number_list = list(correct_number)

      elif codebreaker[i] == codemaker[i]:
        correct_number_and_location += codebreaker[i]
        correct_number_and_location_list = list(correct_number_and_location)

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