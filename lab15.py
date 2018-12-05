#lab15 - Team 10
# M. Mariscal, C. Piwarski, W. Robleh

###############################################################################################################
# Problem 1
###############################################################################################################

import random

def problem1():
  welcomeMessage ='On this first roll, a 7 or an 11 automatically wins, and a 2, 3, or 12 automatically loses,\
and play is over. If a 4, 5, 6, 8, 9, or 10 are rolled on this first roll, that number becomes the "point.\
The player continues to roll the two dice again until one of two things happens: either they roll the "point" \
again, in which case they win; or they roll a 7, in which case they lose.'
  rollAgain = True
  
  # introduce game
  answer = requestString('Do you want to play a game of craps(y/n)?')
  if answer == 'y':
     showInformation(welcomeMessage)
  if answer == 'n':
     showInformation('Goodbye')
      
  # first roll
  
  # roll dice
  dice1 = random.randint(1, 6)
  dice2 = random.randint(1, 6)
  showInformation('Dice1: %d\nDice2: %d' % (dice1, dice2))
  total = dice1 + dice2
  
  # determine another roll
  if total == 7 or total == 11:
    rollAgain = False
    gameWon = True
  elif total == 2 or total == 3 or total == 12:
    rollAgain = False
    gameWon = False
  else:
    point = total
    
  # subsequent rolls
  while rollAgain == True:
    
    # roll dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    showInformation('Dice1: %d\nDice2: %d' % (dice1, dice2))
    total = dice1 + dice2
    
    # determine another roll
    if total == point:
        rollAgain = False
        gameWon = True
    elif total == 7:
        rollAgain = False
        gameWon = False
    
  # declare win or lose
  if gameWon == True:
    showInformation('Congratulations, you won the game!')
  else:
    showInformation('I am sorry, you lose this round.')
  

if __name__ == '__main__':
  problem1()