
#made by evelyn, kai, michael
import words
import random

import pygame

WIDTH, HEIGHT = 900, 900
FPS = 30

WHITE = (255, 255, 255)
GREEN = "#6aaa64"
YELLOW = "#c9b458"
GREY = "#787c7e"

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("wordle")
clock = pygame.time.Clock()



board = [
    ["_","_","_","_","_"],
    ["_","_","_","_","_"],
    ["_","_","_","_","_"],
    ["_","_","_","_","_"],
    ["_","_","_","_","_"],
    ["_","_","_","_","_"]
]


def get_word():
  randint = random.randint(0,len(words.wordlist))
  return words.wordlist[randint]

word = get_word()

def wordle(guess1):
  
  letters = ["_","_","_","_","_"]
  
  #green letters
  for a in range(5):
    if guess1[a:a+1]==word[a:a+1]:
      letters[a] = guess1[a:a+1].upper()
  
  #yellow letters
  index = 0
  for y in guess1:
    if y in word and letters[index]== "_":
      letters[index] = y.upper()
    index+=1
  
  #gray letters
  for b in range(5):
    if letters[b] == "_":
      letters[b] = guess1[b].upper()
  
  return letters

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


def display_board():
  screen.fill(WHITE)
  for row in range(6):
    for col in range(5):
      pygame.draw.rect(screen,GREY, (col*WIDTH/5 + 10, row*HEIGHT/6+10, WIDTH/5-20, HEIGHT/5-20))
  

guess_count = 0
gameRunning = True

print("Hello! This is BHS CS Club's Wordle game!")
print("Made by Evelyn, Kai, Michael")
while gameRunning == True:
  validGuess = False

  clock.tick(FPS)  

  display_board()
  pygame.display.flip()


  # guess = input()
  # while validGuess == False:
  #   if guess not in words.validwords and guess not in words.wordlist:
  #     print('not a valid word')
  #     guess = input()
  #   else:
  #     validGuess = True

  # print("Hello! This is BHS CS Club's Wordle game!")
  # print("Made by Evelyn, Kai, Michael")

  # replaceWord(board, guess)

  # guess_count+=1
  # if guess == word:
  #   print("Congrats! You win :))")
  #   gameRunning = False
  # elif guess_count > 5:
  #   print("Sorry, you lose. The word was " + word + ".")
  #   gameRunning = False
