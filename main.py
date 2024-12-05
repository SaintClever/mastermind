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


  tracked_attempts = []

  for i in range(len(codemaker)):
    if codebreaker[i] != codemaker[i] and codebreaker[i] not in codemaker:
      return f"{codebreaker} all incorrect"
    
    if codebreaker[i] == codemaker[i] and codebreaker[i] in codemaker:
      return f"{codebreaker} 1 correct number and 1 correct location"

    if codebreaker[i] == codemaker[i] and codebreaker[i] not in codemaker:
      return f""






for i in range(1):
  print(game())