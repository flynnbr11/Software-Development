import itertools, random
from cardClass import *

def printAvailCards(centralDeck):
  print "Available Cards"
  max = centralDeck['activeSize']
  count = 0
  while count < max:
      print centralDeck['active'][count]
      count = count + 1

  print "Supplement"
  if len(centralDeck['supplement']) > 0:
      print centralDeck['supplement'][0]

	
	
def printHealths(playerOne, playerComputer):

  print "\nPlayer Health %s" % playerOne['health']
  print "Computer Health %s" % playerComputer['health']

	
def printStateOfPlay(playerOne, playerComputer, money, attack):
  printHealths(playerOne, playerComputer)
  print "\nwhile loop: Your Hand"
  index = 0
  for card in playerOne['hand']:
          print "[%s] %s" % (index, card)
          index = index + 1
  print "\nYour Values"
  print " Money %s, Attack %s" % (money, attack)
