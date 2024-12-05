import requests


# # Request made to API
# response = requests.get("https://www.random.org/integers/?num=4&min=0&max=7&col=1&base=10&format=plain&rnd=new")

# # Format response and store in list
# codemaker = response.text.replace("\n", " ").split()
codemaker = ["0", "1", "3", "5"]

# Grid
print(f"\n ==== {codemaker} ==== \n")

row_count = 10
pin = "\u26AB"
grid = row_count * f"\n| {pin} {pin} {pin} {pin} |"
print(grid)



# Game initializes
def game():
  user_input = input("\n\nPlease guess 4 random numbers: ")
  codebreaker = user_input.split()


  print(len(codebreaker))
  print(codemaker, codebreaker)


  data = f'''
  Example Run:
  Game initializes and selects “0 1 3 5”
  Player guesses 2 2 4 6 game responds “all incorrect”
  Player guesses 0 2 4 6 game responds “1 correct number and 1 correct location”
  Player guesses 2 2 1 1 game responds “1 correct number and 0 correct location”
  Player guesses 0 1 5 6 game responds “3 correct numbers and 2 correct location”
  '''

  game_attempts = []

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

    if codebreaker[i] == codemaker[i]:
      correct_number_and_location += codebreaker[i]
      correct_number_and_location_list = list(correct_number_and_location)

      if len(correct_number_and_location) > 1:
        correct_number_and_location_list = list(correct_number_and_location)

    elif codebreaker[i] in codemaker and codebreaker[i] != codemaker[i]:
      correct_number += codebreaker[i]
      correct_number_list = list(correct_number)


  print("a", all_incorrect)
  print("b", correct_number)
  print("c", correct_location)
  print("d", correct_number_and_location)

  print("e", all_incorrect_list)
  print("f", correct_number_list)
  print("g", correct_location_list)
  print("h", correct_number_and_location_list)

  if all_incorrect_list:
    print("all incorrect")

  elif correct_number_list and correct_number_and_location_list:
    print(f"LLL {len( correct_number_list) + len( correct_number_and_location_list)} correct numbers and {len(correct_number_and_location_list)} correct location")

  elif correct_number_list:
    # correct_number_list[0] should all have the same number so I only need the first one
    print(f"LL {len(correct_number_list[0])} correct number and {len(correct_number_and_location_list)} correct location")

  elif correct_number_and_location_list:
    print(f"L {len(correct_number_and_location_list)} correct number and {len(correct_number_and_location_list)} correct location")


  # return f"{codebreaker} all incorrect"
  # return f"{codebreaker} 1 correct number and 1 correct location"
  # return f"{codebreaker} 1 correct number and 0 correct location"
  # return f"{codebreaker} 3 correct number and 2 correct location"
  



for i in range(1):
  print(game())