#!/usr/bin/env python3
import sys
import os
import numpy as np
#import cython
import random
#from dataclasses import dataclass
#H STANDS FOR HEATHLANDS

print(random.__all__)

class Game:
 def __init__(self, money, date, population, industrial, commercial, electric_power, failed):
  self.money = 10000
  self.date = 1900.0
  self.population = 1
  self.industrial = 0
  self.commercial = 0
  self.electric_power = False
  self.failed = False
  
land_use = np.array([["h", "h", "h", "h"], ["h", "h", "h", "h"], ["h", "h", "h", "h"], ["h", "h", "h", "h"]])
pollution = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
life_expectancy = np.array([["EXPUNGED", "EXPUNGED", "EXPUNGED", "EXPUNGED"], ["EXPUNGED", "EXPUNGED", "EXPUNGED", "EXPUNGED"], ["EXPUNGED", "EXPUNGED", "EXPUNGED", "EXPUNGED"], ["EXPUNGED", "EXPUNGED", "EXPUNGED", "EXPUNGED"]])

def calculate_pollution(land_use):

 #### dummy function for testing

 #pollution[int(ironedoutuserinput[1]), int(ironedoutuserinput[2])] = "r"
 #pollution[0, 0] = "50%"
 #print("Dummy function for testing")
 
 #### the actual function
 
 x = len(land_use)
 y = len(land_use[0])
 for i in range(0, x):
  print(i)
  for j in range(0, y):
   print(j)
   if land_use[i, j] == "i":
    print("Industrial land use found at the grid reference: {} {}".format(i, j))
    pollution[i, j] += 10 
 
def calculate_life_expectancy(pollution):
 print("The other dummy function for testing")

#### try to read newspaper headlines from a file

result = []
newspaper = open('./ticker.txt', 'r')
try:
 ticker = newspaper.read()
finally:
 newspaper.close()
headlines = ticker.splitlines()
print(headlines)
print(result)

#### initializes a class instance of the game walkthrough
 
g1 = Game(10000, 1900.0, 1, 0, 0, False, False)

#### defines the main loop of the game

def main(money, date, population, failed):
 if True:#g1.resource1 > 0 and g1.resource2 > 0:
  print("---------------------------")
  print("Date: {} ".format(g1.date))
  print("Money: {} ".format(g1.money))
  print("Population: {} ".format(g1.population))
  #print("Resource 1: {}/{} Resource 2: {}/{}".format(g1.resource1, g1.maxresource1, g1.resource2, g1.resource2))
  print("Zone residential (r), industrial (i), commercial (c), build a public seervices building (p), build a generator (g), do nothing (n)?")
  print("Specify coordinates, i.e. (r 0 0)")
  print("Land use map:")
  print("H on the land use map stands for heathlands")
  print(land_use)
  print("Pollution map:")
  print(pollution)
  print("Life expectancy map:")
  print(life_expectancy)
  print("Quit game (q)?")
  
  #### reads the user input
  
  userinput = input("What will you do this month, Mayor?")
  print(userinput)
  ironedoutuserinput = userinput.split()
  print(ironedoutuserinput)
  try:
   print(ironedoutuserinput[1])
  except:
   print("No coordinates specified this month")
  print("===========================")
 #elif g1.resource1 <= 0:
 # print("Game over due to lack of resource 1")
 # g1.failed = True
 #elif g1.resource2 <= 0:
 # print("Game over due to lack of resource 2")
 # g1.failed = True
 #if g1.failed == True:
 # print("Restart game (r), quit game (q)?")
 # userinput = input("What do you do?")
 # print(userinput)
 # if userinput == "r":
   #g1.resource1 = 5
   #g1.maxresource1 = 10
 #  g1.resource2 = 5
 #  g1.maxresource2 = 10
 #  g1.failed = False
  if ironedoutuserinput[0] == "g":
   land_use[int(ironedoutuserinput[1]), int(ironedoutuserinput[2])] = "g"
   g1.money -= 1500
   g1.electric_power = True
  if ironedoutuserinput[0] == "n":
   print("")
  elif ironedoutuserinput[0] == "q":
   sys.exit()
  
  if g1.electric_power == True:
   if ironedoutuserinput[0] == "r":
    land_use[int(ironedoutuserinput[1]), int(ironedoutuserinput[2])] = "r"
    g1.population += 10
    g1.money -= 100
   if ironedoutuserinput[0] == "i":
    land_use[int(ironedoutuserinput[1]), int(ironedoutuserinput[2])] = "i"
    g1.industrial += 1
    g1.money -= 150
   if ironedoutuserinput[0] == "c":
    land_use[int(ironedoutuserinput[1]), int(ironedoutuserinput[2])] = "c"
    g1.commercial += 1
    g1.money -= 200
   if ironedoutuserinput[0] == "p":
    land_use[int(ironedoutuserinput[1]), int(ironedoutuserinput[2])] = "p"
    print("The emergency seervices pledge to protect the citizens. We'll see about that.")
    g1.money -= 1000
   if ironedoutuserinput[0] == "g":
    land_use[int(ironedoutuserinput[1]), int(ironedoutuserinput[2])] = "g"
    g1.money -= 1500
    g1.electric_power = True
  elif g1.electric_power == False:
   print("No citizen (excepting yourself) will move to this city without electric power! You need to build the generators first, Mayor.")
   
  #### calculate pollution
  
  calculate_pollution(land_use)
   
  #### advance the date
  
  g1.date += 0.1
  
  #### taxes
  
  if (population*10) >= g1.industrial or (population*10) >= g1.commercial:
   g1.money += population
   print("The citizens had enough money to pay personal income tax this month, thank goodness.")
  else:
   print("Something went against protocol. It seems like the citizens did not file the personal income tax this month.")
  if (population*10) >= g1.industrial:
   g1.money += (g1.industrial*2)
   print("The dirty industry (if any is present) had enough money to pay tax this month.")
  else:
   print("Something went against protocol. It seems like the dirty industry did not file tax this month.")
  if (population*10) >= g1.commercial:
   g1.money += (g1.commercial*3)
   print("The commerce (if any is present) had enough money to pay tax this month.")
  else:
   print("Something went against protocol. It seems like the commerce did not file tax this month.")
  
  #### news ticker
  
  if True:#population >= 10:
   #print("The Angoba newspaper says: {} ".format(random.randrange(0, 4, 1)))
   print("The Angoba newspaper says: {} ".format(headlines[int(random.randrange(0, 2))]))
   #print("The Angoba newspaper says: {} ".format(result[int(random.randrange(0, 4))]))
  # print("The Angoba newspaper says: {} ".format(random.choice(result)))
   
  #### end main game loop definition
      
while True:
 main(g1.money, g1.date, g1.population, g1.failed)
