
#made by evelyn, kai, michael
import words
import random

wordarray = [["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"],["_","_","_","_","_"]]


def get_word():
  randint = random.randint(0,len(words.wordlist))
  return words.wordlist[randint]

word = get_word()

def wordle(guess1):
  
  letters = ["_","_","_","_","_"]
  coloredStr = ["_","_","_","_","_"]
  
  #green letters
  for a in range(5):
    if guess1[a:a+1]==word[a:a+1]:
      letters[a] = guess1[a:a+1].upper()
      coloredStr[a] = '\033[0;37;42m' + guess1[a:a+1].upper() + '\033[0;0m'
  
  #yellow letters
  index = 0
  for y in guess1:
    if y in word and letters[index]== "_":
      letters[index] = y.upper()
      coloredStr[index] = '\033[0;37;43m' + y.upper() + '\033[0;0m'
    index+=1
  
  #gray letters
  for b in range(5):
    if letters[b] == "_":
      letters[b] = guess1[b].upper()
      coloredStr[b] = guess1[b].upper()
  
  return coloredStr

def displayBoard(arr):
  for row in arr:
    strtoprint = ""
    for col in row:
      strtoprint += col
    print(strtoprint)
  return

def replaceWord(arr, guess):
  print("")
  countOfRow = 0
  for row in arr:
    if(row[0]!="_"):
      countOfRow +=1
    else:
      break

  for x in range(0,5):
    wordledguess = wordle(guess)
    arr[countOfRow][x] = wordledguess[x]


guess_count = 0
gameRunning = True

print("Hello! This is BHS CS Club's Wordle game!")
print("Made by Evelyn, Kai, Michael")
while gameRunning == True:
  validGuess = False
  guess = input()
  while validGuess == False:
    if guess not in words.validwords and guess not in words.wordlist:
      print('not a valid word')
      guess = input()
    else:
      validGuess = True

  #clear the console
  print("Hello! This is BHS CS Club's Wordle game!")
  print("Made by Evelyn, Kai, Michael")

  replaceWord(wordarray, guess)

  displayBoard(wordarray)

  guess_count+=1
  if guess == word:
    print("Congrats! You win :))")
    gameRunning = False
  elif guess_count > 5:
    print("Sorry, you lose. The word was " + word + ".")
    gameRunning = False
