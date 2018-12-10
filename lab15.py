# Lab15 - Team 10
# M. Mariscal, C. Piwarski, W. Robleh
# Developed with Python2 and JES

################################################################################
# Problem 1
################################################################################

import random
import datetime

def problem1():
  welcomeMessage ='On this first roll, a 7 or an 11 automatically wins, and a 2,\
3, or 12 automatically loses, and play is over. If a 4, 5, 6, 8, 9, or 10 are\
 rolled on this first roll, that number becomes the "point. The player\
  continues to roll the two dice again until one of two things happens: \
either they roll the "point" again, in which case they win; or they roll a 7,\
 in which case they lose.'
  rollAgain = True
  
  # introduce game
  answer = requestString('Do you want to play a game of craps(y/n)?')
  if answer == 'y':
     showInformation(welcomeMessage)
  if answer == 'n':
     showInformation('Goodbye')
      
  # first roll
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
  
################################################################################
# Problem 2
################################################################################

import calendar
from datetime import date

#prints the calendar month of when you are born.
def printDateMonth(year, month):
  c = calendar.prmonth(year, month)
  print c

#prints the days until next birthday.
def days_until_next(month, day):
  today = date.today()
  birthday = date(today.year, month, day)
  days_until_birth = (birthday - today).days
  if days_until_birth > 0:
    print('It is ' + str(days_until_birth) + ' day(s) until your birthday!')
  elif days_until_birth == 0:
    print('Happy Birthday!')
  else:
    new = 365 - abs(days_until_birth) # make sure that it returns new year
    print('Your birthday is in the next ' + str(new) + ' days')

#prints day of week when the declaratio nof independence occurs
def dayOfWeek(year, month, day):
  weekOf = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
  day = date(year, month, day).isoweekday()
  print 'The Declaration of Independence was signed on: '
  print weekOf[day - 1] + ' ' + calendar.month_name[month] + ' ' + str(day) + ', ' + str(year)
  


#problem 2 takes 3 inputs to put everything together.
#Those three inputs are the users birthday.    
def problem2():

  year = int(input('What year were born? [YY] '))
  month = int(input('When is your birthday? [MM] '))
  day = int(input('When is your birthday? [DD] '))
  
  
  printDateMonth(year, month)
  days_until_next(month, day)
  dayOfWeek(1776, 7 , 4) #declaration of independence part
  return

if __name__ == '__main__':
  problem1()
  problem2()