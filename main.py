import requests

response = requests.get("https://www.random.org/integers/?num=4&min=1&max=6&col=1&base=10&format=plain&rnd=new")

code = response.text.replace("\n", " ").split()

print(code)