import itertools, random
from cardClass import *
from playerFunctions import * 
from printFunctions import *
from gameSetupAndPlayFunctions import *

  

def computerTurn(playerOne, playerComputer, centralDeck, aggressive):
  """
  Simulate opponent's moves. 
  Update values/hands of both user and computer based on computer's moves. 
  """  
  money = 0
  attack = 0
  
  playerComputer, money, attack = fillComputersHand(playerComputer, money, attack)

  print " Computer player values attack %s, money %s" % (attack, money)
  print " Computer attacking with strength %s" % attack
  playerOne['health'] = playerOne['health'] - attack
  attack = 0

  printHealths(playerOne, playerComputer)
  
  print "Computer player values attack %s, money %s" % (attack, money)
  print "Computer buying"
  if money > 0:
      playerComputer, money, centralDeck = computerPurchase(playerComputer, centralDeck, money, aggressive	)
  else:
      print "No Money to buy anything"

  playerComputer = updateComputerHand(playerComputer)

  print "Computer turn ending"

  return (playerOne, playerComputer, centralDeck)  
  
  
def fillComputersHand(playerComputer, money, attack):
  """
  Initiate computer's active hand from cards in their discard hand. 
  """
  for x in range(0, len(playerComputer['hand'])):
                  card = playerComputer['hand'].pop()
                  playerComputer['active'].append(card)
                  money = money + card.get_money()
                  attack = attack + card.get_attack()
  return (playerComputer, money, attack)	  
  
def computerPurchase(playerComputer, centralDeck, money, aggressive):
    """
    Computer purchases which cards it can afford based on the preference
    of aggressive or acquisative. 
    """
    computerBuy = True
    templist = []
    print "Starting Money %s and computerBuy %s " % (money, computerBuy)
    while computerBuy:

		  templist = []
		  if len(centralDeck['supplement']) > 0:
		      if centralDeck['supplement'][0].cost <= money:
		          templist.append(("S", centralDeck['supplement'][0]))
		  for intindex in range (0, centralDeck['activeSize']):
		      if centralDeck['active'][intindex].cost <= money:
		          templist.append((intindex, centralDeck['active'][intindex]))
		  if len(templist) >0:
		      highestIndex = 0
		      for intindex in range(0,len(templist)):
		          if templist[intindex][1].cost > templist[highestIndex][1].cost:
		              highestIndex = intindex
		          if templist[intindex][1].cost == templist[highestIndex][1].cost:
		              if aggressive:
		                  if templist[intindex][1].get_attack() >templist[highestIndex][1].get_attack():
		                      highestIndex = intindex
		              else:
		                  if templist[intindex][1].get_attack() >templist[highestIndex][1].get_money():
		                      highestIndex = intindex
		      source = templist[highestIndex][0]
		      if source in range(0,5):
		          if money >= centralDeck['active'][int(source)].cost:
		              money = money - centralDeck['active'][int(source)].cost
		              card = centralDeck['active'].pop(int(source))
		              print "Card bought %s" % card
		              playerComputer['discard'].append(card)
		              if( len(centralDeck['deck']) > 0):
		                  card = centralDeck['deck'].pop()
		                  centralDeck['active'].append(card)
		              else:
		                  centralDeck['activeSize'] = centralDeck['activeSize'] - 1
		          else:
		              print "Error Occurred"
		      else:
		          if money >= centralDeck['supplement'][0].cost:
		              money = money - centralDeck['supplement'][0].cost
		              card = centralDeck['supplement'].pop()
		              playerComputer['discard'].append(card)
		              print "Supplement Bought %s" % card
		          else:
		              print "Error Occurred"  
		  else:
		      computerBuy = False
		  if money == 0:
		      computerBuy = False

    return (playerComputer, money, centralDeck)
  
  
def updateComputerHand(playerComputer):
	"""
	Replaces the cards in the computers hand into discard deck
	and shuffles discard deck.
	"""
	if (len(playerComputer['hand']) >0 ):
		  for x in range(0, len(playerComputer['hand'])):
		      playerComputer['discard'].append(playerComputer['hand'].pop())
	if (len(playerComputer['active']) >0 ):
		  for x in range(0, len(playerComputer['active'])):
		      playerComputer['discard'].append(playerComputer['active'].pop())
	for x in range(0, playerComputer['handsize']):
		          if len(playerComputer['deck']) == 0:
		              random.shuffle(playerComputer['discard'])
		              playerComputer['deck'] = playerComputer['discard']
		              playerComputer['discard'] = []
		          card = playerComputer['deck'].pop()
		          playerComputer['hand'].append(card)
	return playerComputer
	



