#from screen_search import *
import pyautogui
from os import name, system
import time

cards=["d2","d3","d4","d5","d6","d7","d8","d9","dt","dj","dq","dk","da",
       "c2","c3","c4","c5","c6","c7","c8","c9","ct","cj","cq","ck","ca",
       "h2","h3","h4","h5","h6","h7","h8","h9","ht","hj","hq","hk","ha",
       "s2","s3","s4","s5","s6","s7","s8","s9","st","sj","sq","sk","sa"]

found=[""]

################################
# MAKE SURE TO CONFIGURE THESE #
################################
imagePath = ""
imageExtension = ""

def clear(): 
  # for windows 
  if name == 'nt': 
    system('cls') 
  # for mac and linux(here, os.name is 'posix') 
  else: 
    system('clear') 

def drawTable():
  clear()
  
  for i in range(0,13):
    line = "| "
    for j in range(0,4):
      if(cards[13*j + i] not in found):
        line += cards[13*j +i]
      else:
        line += "  "
      line += " | "
    print(line)
  print("----------------------")
  

def searchCard(card, tableImg):
  # only try searching for the card if the card hasn't been found yet
  if(card not in found):
    try:
      # try searching for the card (throws an error if card not found)
      pyautogui.locate(card + ".png", tableImg)
      # if the card was found add the card to the found list
      found.append(card)
      # update the table
      drawTable()
    except:
      # do nothing if the card wasn't found
      pass

def main():
  # find the top left corner of the table
  tcX = None
  tcY = None
  # loop until we find the table
  while(tcX == None):
    try:
      (tcX,tcY,_,_) = pyautogui.locateOnScreen("tableCorner.png")
    except:
      pass
      
  # define the range
  tableRegion = [tcX,tcY,260,240]  

  userInput = ""
  # loop until the user exits
  while(userInput != "quit"):
    # clear the found cards
    found.clear()
    
    # loop until the hand is complete
    while(len(found) < 52):
      # take a screenshot of the table
      tableImg = pyautogui.screenshot(region=tableRegion)
      
      # loop through the deck to see if the cards exist
      for card in real:
        searchCard(card, tableImg)
		
    # get the user input to see if they want to do another hand or exit
    userInput = input("Press enter key to continue or type 'quit' to exit: ")
      
main()