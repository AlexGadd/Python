import urllib.request
import json
from random import randrange
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def hangman(data):
    HANGMAN = (
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | | 
|
--------
""")
    theJSON = json.loads(data)
    wordlist = theJSON["data"]
    choice = wordlist[randrange(0, (len(wordlist) - 1))]
    choices = []
    displayResult = ""
    response = ""
    guesses = ""
    finished = False
    clear()


    numberOfGuesses = len(HANGMAN)
    clear()
    while finished == False:
        if displayResult == "":
            for each in choice:
                displayResult = displayResult + "_ "
        clear()
        print(HANGMAN[len(HANGMAN) - numberOfGuesses])
        print(response)
        print(f"You have guessed these letters so far: {guesses}")
        currentLetter = str(input(f"You have {numberOfGuesses} lives left, the word so far is {displayResult}\n"))

        if len(currentLetter) > 1:
            response = "It must be a single letter"
        elif currentLetter in choices:
            response = "Youve already chosen that one"
        elif currentLetter in choice:
            response = "You got one right"
            choices.append(currentLetter)
        else:
            response = "Looks like you messed up"
            choices.append(currentLetter)
            numberOfGuesses = numberOfGuesses - 1
        
        guesses = ""
        for each in choices:
            guesses = guesses + str(each)
    
        if numberOfGuesses < 1:
            print(f"You lost! The word was '{choice}'")
            exit()

        count = int(len(choice)  - 1)
        length = 0

        while count > -1:
            if choice[count] in choices:
                length = length + 1
            count = count -1
    
        if length == len(choice):
            clear()
            finished = True
            print(f"You won! The word was '{choice}'")

        displayResult = ""
        for index, checker in enumerate(choice):
            if checker in choices:
                displayResult = displayResult + checker + " "
            else:
                displayResult = displayResult + "_ "






def main():
  # define a variable to hold the source URL
  urlData = "https://www.randomlists.com/data/nouns.json"
  
  # Open the URL and read the data
  webUrl = urllib.request.urlopen(urlData)
  print ("result code: " + str(webUrl.getcode()))
  if (webUrl.getcode() == 200):
    data = webUrl.read()
    # print out our customized results
    hangman(data)
  else:
      print("No internet connection!")

if __name__ == "__main__":
  main()
