#!/usr/bin/env python3
import sys
import os
import numpy as np
#import cython
import random
#from dataclasses import dataclass
#import arcade

#H STANDS FOR HEATHLANDS
#A STANDS FOR AN ABANDONED BUILDING
#U STANDS FOR RUINS

#SCREEN_WIDTH = 800
#SCREEN_HEIGHT = 600
#SCREEN_TITLE = "Close this window with the X button"
#RADIUS = 150
#SCALING = 1

print(random.__all__)

random.seed(63)

#poor_residential = arcade.load_texture("images/lower_class_residential.png")
#medium_residential = arcade.load_texture("images/middle_class_residential.png")
#rich_residential = arcade.load_texture("images/luxury_residential.png")

#poor_commercial = arcade.load_texture("images/diner_commercial.png")
#medium_commercial = arcade.load_texture("images/googie_restaurant_commercial.png")
#rich_commercial = arcade.load_texture("images/historic_office_commercial.png")

#public_seervices = arcade.load_texture("images/hostpital.png")
#generators = arcade.load_texture("images/generators.png")
#school = arcade.load_texture("images/school.png")

#abandoned_building = arcade.load_texture("images/abandoned_building.png")

#heathlands = arcade.load_texture("images/vegetation.png")
#hills = arcade.load_texture("images/hills.png")
#water = arcade.load_texture("images/water.png")
 
class Game:
 def __init__(self, money, date, population, true_population, industrial, commercial, seervices, residential_demand, industrial_demand, commercial_demand, residential_tax, industrial_tax, commercial_tax, electric_power, failed):
  self.money = 10000
  self.date = 1900.0
  self.population = 1
  self.true_population = 1
  self.industrial = 0
  self.commercial = 0
  self.seervices = 0
  self.residential_demand = 50
  self.industrial_demand = 50
  self.commercial_demand = 50
  self.residential_tax = 11
  self.industrial_tax = 11
  self.commercial_tax = 11
  self.electric_power = False
  self.failed = False
  
land_use = np.array([["h", "h", "h", "h", "h", "h", "h", "h"], ["h", "h", "h", "h", "h", "h", "h", "h"], ["h", "h", "h", "h", "h", "h", "h", "h"], ["h", "h", "h", "h", "h", "h", "h", "h"], ["h", "h", "h", "h", "h", "h", "h", "h"], ["h", "h", "h", "h", "h", "h", "h", "h"], ["h", "h", "h", "h", "h", "h", "h", "h"], ["h", "h", "h", "h", "h", "h", "h", "h"]])
pollution = np.array([[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]])
life_expectancy = np.array([[70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0], [70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0], [70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0], [70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0], [70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0], [70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0], [70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0], [70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0]])

def calculate_pollution(land_use):

 #### dummy function for testing

 #pollution[int(ironedoutuserinput[1]), int(ironedoutuserinput[2])] = "r"
 #pollution[0, 0] = "50%"
 #print("Dummy function for testing")
 
 #### the actual function
 
 x = len(land_use)
 y = len(land_use[0])
 for i in range(0, x):
  for j in range(0, y):
   if land_use[i, j] == "i" or land_use[i, j] == "g":
    print("Industrial land use found at the grid reference: {} {}".format(i, j))
    if pollution[i, j] < 1000:
     for k in range(i - 1, i + 2):
      for l in range(j - 1, j + 2):
       try:
        pollution[k, l] += 1
       except:
        print("We're polluting our neighbors!")
 
def calculate_life_expectancy(land_use, pollution, life_expectancy):
 x = len(pollution)
 y = len(pollution[0])
 for i in range(0, x):
  for j in range(0, y):
   life_expectancy[i, j] -= (pollution[i, j] / 1000)
   if land_use[i, j] == "p":
    for k in range(i - 1, i + 2):
     for l in range(j - 1, j + 2):
      try:
       life_expectancy[k, l] += 0.1
      except:
       print("Notice: public seervices use suboptimal since the public seervices building is close to the city limits")
   if life_expectancy[i, j] > 105:
    life_expectancy[i, j] = 105
   if life_expectancy[i, j] < 55:
    life_expectancy[i, j] = 55
   #if pollution[i, j] == "i":
   # print("Industrial land use found at the grid reference: {} {}".format(i, j))
   # if life_expectancy[i, j] < 105 and life_expectancy[i, j] > 55:
   #  life_expectancy[i, j] -= 2 

def avg_pollution(pollution):
 avg_pollution = 0
 tiles = 0
 x = len(pollution)
 y = len(pollution[0])
 for i in range(0, x):
  for j in range(0, y):
   avg_pollution += pollution[i, j]
   tiles += 1
 avg_pollution /= tiles
 return avg_pollution

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
 
g1 = Game(10000, 1900.0, 1, 1, 0, 0, 0, 50, 50, 50, 11, 11, 11, False, False)

#### defines the main loop of the game

def main(money, date, population, true_population, failed):
 if True:#g1.resource1 > 0 and g1.resource2 > 0:
 
  #### calculate pollution
  
  calculate_pollution(land_use)
  
  #### calculate life expectancy
  
  calculate_life_expectancy(land_use, pollution, life_expectancy)
  
  #### calculate average pollution
  
  average_pollution = avg_pollution(pollution)
  print("Average pollution: {} ".format(average_pollution))
  
  #### rci demand influenced by taxes
  
  g1.residential_demand -= (int(g1.residential_tax) - 11)
  g1.commercial_demand -= (int(g1.commercial_tax) - 11)
  g1.industrial_demand -= (int(g1.industrial_tax) - 11)
  
  #### rci demand reduced by pollution
  
  g1.residential_demand -= (average_pollution * 4)
  g1.commercial_demand -= (average_pollution * 2)
  g1.industrial_demand -= (average_pollution * 1)
  
  #### rci demand increased by public seervices
  
  g1.residential_demand += (g1.seervices * 10)
  g1.commercial_demand += (g1.seervices * 1)
  
  #### rci demand influenced by rci demand
  
  g1.residential_demand += g1.commercial
  g1.residential_demand += g1.industrial
  g1.commercial_demand += (g1.population / 6)#(g1.true_population/10)#g1.industrial
  g1.industrial_demand += (g1.population / 24)
  g1.industrial_demand += (g1.commercial * 2)
  
  #### check if demand exceeds 100 or is below 0 and change the value to remain within 0-100
  
  if g1.residential_demand > 100:
   g1.residential_demand = 100
  if g1.residential_demand < 0:
   g1.residential_demand = 0
  if g1.commercial_demand > 100:
   g1.commercial_demand = 100
  if g1.commercial_demand < 0:
   g1.commercial_demand = 0
  if g1.industrial_demand > 100:
   g1.industrial_demand = 100
  if g1.industrial_demand < 0:
   g1.industrial_demand = 0
 
  print("---------------------------")
  print('\x1b[0;37;40m', "Date: {}, Money: {}, Population: {}, Demand: ".format(g1.date, g1.money,g1.population) + '\x1b[0;32;40m', "Residential {}, ".format(int(g1.residential_demand)) + '\x1b[0;34;40m', "Commercial {}, ".format(int(g1.commercial_demand)) + '\x1b[0;33;40m', "Industrial {} ".format(int(g1.industrial_demand)) + '\x1b[0m')
  #print('\034[40m', "Date: {}, Money: {}, Population: {}, Demand: Residential {}, Commercial {}, Industrial {} ".format(g1.date, g1.money,g1.population, int(g1.residential_demand), int(g1.commercial_demand), int(g1.industrial_demand)))
  #print("Money: {} ".format(g1.money))
  #print("Population: {} ".format(g1.population))
  #print("Demand: Residential {}, Commercial {}, Industrial {} ".format(int(g1.residential_demand), int(g1.commercial_demand), int(g1.industrial_demand)))
  #print("Resource 1: {}/{} Resource 2: {}/{}".format(g1.resource1, g1.maxresource1, g1.resource2, g1.resource2))
  print("Zone " + '\x1b[0;32;40m',  "residential (r), " + '\x1b[0;33;40m', "industrial (i), " + '\x1b[0;34;40m', "commercial (c), " + '\x1b[0;37;40m', "build a public seervices building (p), build a generator (g), do nothing (n)?" + '\x1b[0m')
  print("Specify coordinates, i.e. (r 0 0) (numbers increment from the top left corner towards the bottom right corner)")
  print('\x1b[0;37;40m', "Current taxes: " + '\x1b[0;32;40m',  "residential (r) {}, ".format(int(g1.residential_tax)) + '\x1b[0;33;40m', "industrial (i) {}, ".format(int(g1.industrial_tax)) + '\x1b[0;34;40m', "commercial (c) {}, ".format(int(g1.commercial_tax)) + '\x1b[0;37;40m', "change taxes? (i.e. t r 11)" + '\x1b[0m')
  print("Land use map:")
  print("H on the land use map stands for heathlands, A stands for an abandoned building, U stands for ruins")
  print(land_use)
  print("Pollution map:")
  print(pollution)
  print("Life expectancy map:")
  print(life_expectancy)
  print("Quit game (q)?")
  
  #### reads the user input
  
  try:
   userinput = input("What will you do this month, Mayor?")
  except:
   print("Invalid input provided")
  print(userinput)
  ironedoutuserinput = userinput.split()
  if len(ironedoutuserinput) != 3 and ironedoutuserinput[0] != 'n' and ironedoutuserinput[0] != 'q':
   ironedoutuserinput[0] = 'n'
   print("Invalid input provided. Doing nothing.")
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
  try:
   if ironedoutuserinput[0] == "g":
    land_use[int(ironedoutuserinput[1]), int(ironedoutuserinput[2])] = "g"
    g1.money -= 1500
    g1.electric_power = True
   if ironedoutuserinput[0] == "t":
    if ironedoutuserinput[1] == "r":
     g1.residential_tax = ironedoutuserinput[2]
    elif ironedoutuserinput[1] == "c":
     g1.commercial_tax = ironedoutuserinput[2]
    elif ironedoutuserinput[1] == "i":
     g1.industrial_tax = ironedoutuserinput[2]
  except:
   print("Invalid input")
   ironedoutuserinput = "n"
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
    g1.seervices += 1
    g1.money -= 1000
   if ironedoutuserinput[0] == "g":
    land_use[int(ironedoutuserinput[1]), int(ironedoutuserinput[2])] = "g"
    g1.money -= 1500
    g1.electric_power = True
  elif g1.electric_power == False:
   print("No citizen (excepting yourself) will move to this city without electric power! You need to build the generators first, Mayor.")
   
  #### legacy urban decay code
   
  #if avg_pollution(pollution) > 30.0:
   #x = len(land_use)
   #y = len(land_use[0])
   #for i in range(0, x):
    #for j in range(0, y):
     #if land_use[i, j] == "r" or land_use[i, j] == "c":
      #if random.getrandbits(1) == 1:
       #land_use[i, j] = "a"
       
  #### the actual urban decay code
  
  if g1.residential_demand < 20.0:
   x = len(land_use)
   y = len(land_use[0])
   for i in range(0, x):
    for j in range(0, y):
     if land_use[i, j] == "r":
      if random.getrandbits(1) == 1:
       land_use[i, j] = "a"
       population -= 10
       
  if g1.commercial_demand < 20.0:
   x = len(land_use)
   y = len(land_use[0])
   for i in range(0, x):
    for j in range(0, y):
     if land_use[i, j] == "c":
      if random.getrandbits(1) == 1:
       land_use[i, j] = "a"
       g1.commercial -= 10
   
  #### advance the date
  
  g1.date += 0.1
  
  #### public seervices spending
  
  g1.money -= (g1.seervices * 3)
  
  #### population calculations
  
  x = len(land_use)
  y = len(land_use[0])
  for i in range(0, x):
   for j in range(0, y):
    if land_use[i, j] == "r":# or land_use[i, j] == "g":
     true_population += 10
  print("True population: {} ".format(true_population))
  
  #### taxes
  
  if (true_population * 10) >= g1.industrial or (true_population * 10) >= g1.commercial:
   g1.money += int(population * (int(g1.residential_tax) / 11))
  if (true_population * 10) >= g1.industrial:
   g1.money += int(population * (int(g1.industrial_tax) / 5))
  if (true_population * 10) >= g1.commercial:
   g1.money += int(population * (int(g1.commercial_tax) / 3))
  
  #### news ticker
  
  if True:#population >= 10:
   #print("The Angoba newspaper says: {} ".format(random.randrange(0, 4, 1)))
   #print('\033[95m', "The Angoba newspaper says: {} ".format(headlines[int(random.randrange(0, 2))]))
   #print("The Angoba newspaper says: {} ".format(result[int(random.randrange(0, 4))]))
   print("The Angoba newspaper says: {} ".format(headlines[int(random.randrange(0, 2))]))
  # print("The Angoba newspaper says: {} ".format(random.choice(result)))
   
  #try:
   #arcade.draw_circle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, RADIUS, arcade.color.BLUE)
   #arcade.finish_render()
   #arcade.run()
  #finally:
   #print("Render finished")
  #### end main game loop definition


#### opens the arcade window

#arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

while True:
 #arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
 #arcade.set_background_color(arcade.color.WHITE)
 #arcade.start_render()
 #arcade.draw_texture_rectangle(150, 150, 300, 300, poor_residential)
 main(g1.money, g1.date, g1.population, g1.true_population, g1.failed)
