import requests


# Request made to API
response = requests.get("https://www.random.org/integers/?num=4&min=0&max=7&col=1&base=10&format=plain&rnd=new")

# Format response and store in list
codemaker = response.text.replace("\n", " ").split()


# Grid
row_count = 10
pin = "\u26AB"
grid = row_count * f"\n| {pin} {pin} {pin} {pin}|"
print(grid)



print(f"\n === Game initialized: {codemaker} === \n")



# Initialize game
def game():
  user_input = input("Please insert 4 random numbers: ")
  codebreaker = user_input.split()


  print(len(codebreaker))
  print(codemaker, codebreaker)


  codebreaker_attempts = []

  for i in range(len(codemaker)):
    if codemaker[i] == codebreaker[i]:
      codebreaker.append("BLACK")






for i in range(2):
  game()