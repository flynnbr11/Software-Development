import itertools, random
from cardClass import *
from printFunctions import *
from gameSetupAndPlayFunctions import *

def userTurn(playerOne, playerComputer, centralDeck):
  """
  Tells user the current values, and asks for their choice for this move. 
  Each input has distinct action given by later functions. 
  Asks for their choice in a while loop which is only broken when the choice is
  E (or e), meaning to End the user's move.
  """
  money = 0
  attack = 0
  while True: 

      printStateOfPlay(playerOne, playerComputer, money, attack) 
      act = getPlayerInput()
      if act == 'P' or act == 'p':
          money, attack = playAll(playerOne, money, attack)

      if act.isdigit():
          money, attack = digitInput(playerOne, money, attack, act)

      if act == 'B' or act == 'b':
          playerOne, money, attack, centralDeck = buyCards(playerOne, money, attack, centralDeck)

      if act == 'A' or act == 'a':
          playerComputer, attack = attackFunction(playerComputer, attack)
      if act == 'E' or act == 'e':
          endMove(playerOne)
          break
  
  printAvailCards(centralDeck)
  printHealths(playerOne, playerComputer)
  return (playerOne, playerComputer, centralDeck)


def getPlayerInput(): 
  """
  During the users turn, asks them to input a choice. 
  """
  print "\nChoose Action: (P = play all, [0-n] = play that card, B = Buy Card, A = Attack, E = end turn)"
  invalidInput = 1
  while invalidInput == 1:
    act = raw_input("Enter Action: ")
    if ( act == 'P' or act == 'p' or act == 'B' or act == 'b' or act == 'A' or act == 'a' or act == 'E' or act == 'e' or act.isdigit() ):
        invalidInput = 0 
    else:
        print "Please input a valid option \n"  
  print "input = %s \n" %act
  return act


def playAll(playerOne, money, attack):
  print "\n Inside play All loop \n"
  if(len(playerOne['hand'])>0):
      for x in range(0, len(playerOne['hand'])):
          card = playerOne['hand'].pop()
          playerOne['active'].append(card)
          money = money + card.get_money()
          attack = attack + card.get_attack()
  
  print "\nYour Hand"
  index = 0
  for card in playerOne['hand']:
      print "[%s] %s" % (index, card)
      index = index + 1

  print "\nYour Active Cards"
  for card in playerOne['active']:
      print card
  print "\nYour Values"
  print "inside fnc: Money %s, Attack %s " % (money, attack)

  return (money, attack)

def digitInput(playerOne, money, attack, act):
	if( int(act) < len(playerOne['hand'])):
		  playerOne['active'].append(playerOne['hand'].pop(int(act)))
		  for card in playerOne['active']:
		      money = money + card.get_money()
		      attack = attack + card.get_attack()
	print "\nYour Hand"
	index = 0
	for card in playerOne['hand']:
		  print "[%s] %s" % (index, card)
		  index = index + 1

	print "\nYour Active Cards"
	for card in playerOne['active']:
		  print card
	print "\nYour Values"
	print "Money %s, Attack %s" % (money, attack)

	return (money, attack)

def  buyCards(playerOne, money, attack, centralDeck):

	notending = True
	while money > 0:
		  print "Available Cards"
		  ind = 0
		  for card in centralDeck['active']:
		      print "[%s] %s" % (ind,card)
		      ind = ind + 1
		  print "Choose a card to buy [0-n], S for supplement, E to end buying"
		  buyValue = raw_input("Choose option: ")
		  if buyValue == 'S' or buyValue == 's':
		      if len(centralDeck['supplement']) > 0:
		          if money >= centralDeck['supplement'][0].cost:
		              money = money - centralDeck['supplement'][0].cost
		              playerOne['discard'].append(centralDeck['supplement'].pop())
		              print "Supplement Bought"
		          else:
		              print "insufficient money to buy"
		      else:
		          print "no supplements left"
		  elif buyValue == 'E' or buyValue == 'e':
		      notending = False
		      break;
		  elif buyValue.isdigit():
		      if int(buyValue) < len(centralDeck['active']):
		           if money >= centralDeck['active'][int(buyValue)].cost:
		              money = money - centralDeck['active'][int(buyValue)].cost
		              playerOne['discard'].append(centralDeck['active'].pop(int(buyValue)))
		              if( len(centralDeck['deck']) > 0):
		                  card = centralDeck['deck'].pop()
		                  centralDeck['active'].append(card)
		              else:
		                  centralDeck['activeSize'] = centralDeck['activeSize'] - 1
		              print "Card bought"
		           else:
		              print "insufficient money to buy"
		      else:
		           print "enter a valid index number"
		  else:
		      print "Enter a valid option"

	return(playerOne, money, attack, centralDeck)

def attackFunction(playerComputer, attack):
	playerComputer['health'] = playerComputer['health'] - attack
	attack = 0
	return (playerComputer, attack) ##should this not return playerComputer so health is updated? seems to work without returning health
	

def endMove(playerOne):
  if (len(playerOne['hand']) >0 ):
      for x in range(0, len(playerOne['hand'])):
          playerOne['discard'].append(playerOne['hand'].pop())


  if (len(playerOne['active']) >0 ):
      for x in range(0, len(playerOne['active'])):
          playerOne['discard'].append(playerOne['active'].pop())
  for x in range(0, playerOne['handsize']):
      if len(playerOne['deck']) == 0:
          random.shuffle(playerOne['discard'])
          playerOne['deck'] = playerOne['discard']
          playerOne['discard'] = []
      card = playerOne['deck'].pop()
      playerOne['hand'].append(card)
