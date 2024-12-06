## mastermind ##

Installation instructions:
  - Create a random folder named "mastermind"
  - Download the and main.py and requirements.txt into your mastermind folder
  - Within your code editor or terminal navigate to your mastermind folder and create a virtual env: <code>python -m venv venv</code> or <code>python3 -m venv venv</code>
  - Activate your virtual env:
    - mac: <code>source venv/bin/activate</code>
    - win: <code>source venv/scripts/activate</code>
  - Install package: <code>pip3 install requests</code>
  - After your installation is complete and currenlty located in your mastermind folder run <code>python3 main.py</code> in your terminal 
<br>
<br>

![mastermind](/assets/mastermind.gif "mastermind")

Game rules
- At the start of the game the computer will randomly select a pattern of four different
numbers from a total of 8 different numbers.
- A player will have 10 attempts to guess the number combinations
- At the end of each guess, computer will provide one of the following response as

feedback:
- The player had guess a correct number
- The player had guessed a correct number and its correct location
- The player’s guess was incorrect

Example Run:<br>
Game initializes and selects “0 1 3 5”<br>
Player guesses “2 2 4 6”, game responds “all incorrect”<br>
Player guesses “0 2 4 6”, game responds “1 correct number and 1 correct location”<br>
Player guesses “2 2 1 1”, game responds “1 correct number and 0 correct location”<br>
Player guesses “0 1 5 6”, game responds “3 correct numbers and 2 correct location”<br>

**Note that the computer’s feedback should not reveal which number the player guessed correctly

User Interface:<br>
Any type of user interface is acceptable (command line, mobile app, web page etc) but the
player must have a way of interacting with your game including:
- Ability to guess the combinations of 4 numbers
- Ability to view the history of guesses and their feedback
- The number of guesses remaining is displayed

