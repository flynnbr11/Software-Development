import itertools, random
from cardClass import *
from printFunctions import *

def askToPlay():
  """
  Ask the user if they want to play the game. 
  If they respond Y (or y), ask them what opponent type they want. 
  Then set continueGame = 0, which gets passed to the main, and used in a 
  while loop for duration of game. 
  If they respond N (or n), we exit the program. 
  """
  invalidResponse1 = 1
  invalidResponse2 = 1
  aggressive = 0
  while invalidResponse1:
      playGame = raw_input('Do you want to play a game?: \n')
      if playGame=='Y' or playGame == 'y':
          continueGame = 1
          invalidResponse1 = 0    
      elif playGame == 'N' or playGame == 'n':
          continueGame = 0
          invalidResponse1 = 0
          invalidResponse2 =0
      else: 
          print "\t \t Please choose either Y or N \n"
  while invalidResponse2:
      opponentType = raw_input("Do you want an aggressive (A) opponent or an acquisative (Q) opponent \n")
      if opponentType == 'A' or opponentType == 'a':
          aggressive = 1
          invalidResponse2 = 0
      elif opponentType == 'Q' or opponentType == 'q':
          aggressive = 0
          invalidResponse2 = 0
      else: 
          print "\t \t Please choose either A or Q"                    
  return (continueGame, aggressive)


def setUpPlayers():
    """
    Initialise playerOne, playerComputer and centralDeck, and return them.
    """

    playerOne = {'name': 'player one', 'health': 30, 'deck': None, 'hand': None, 'active': None, 'handsize': 5,
                 'discard': None}
    playerComputer = {'name': 'player computer', 'health': 30, 'deck': None, 'hand': None, 'active': None, 'handsize': 5,
               'discard': None}
    centralDeck = {'name': 'centralDeck', 'active': None, 'activeSize': 5, 'supplement': None, 'deck': None}
    sharedDeck = [4 * [Card('Archer', (3, 0), 2)],
           4 * [Card('Baker', (0, 3), 2)],	
           3 * [Card('Swordsman', (4, 0), 3)],
           2 * [Card('Knight', (6, 0), 5)],
           3 * [Card('Tailor', (0, 4), 3)],
           3 * [Card('Crossbowman', (4, 0), 3)],
           3 * [Card('Merchant', (0, 5), 4)],
           4 * [Card('Thug', (2, 0), 1)],
           4 * [Card('Thief', (1, 1), 1)],
           2 * [Card('Catapault', (7, 0), 6)], 
           2 * [Card('Caravan', (1, 5), 5)],
           2 * [Card('Assassin', (5, 0), 4)]]

    playeronedeck = [8 * [Card('Serf', (0, 1), 0)],
                     2 * [Card('Squire', (1, 0), 0)]
                     ]
    pod = list(itertools.chain.from_iterable(playeronedeck))
    playerOne['deck'] = pod
    playerOne['hand'] = []
    playerOne['discard'] = []
    playerOne['active'] = []
    playertwodeck = [
            8 * [Card('Serf', (0, 1), 0)],
		        2 * [Card('Squire', (1, 0), 0)]
    ]
    ptd = list(itertools.chain.from_iterable(playertwodeck))
    playerComputer['deck'] = ptd
    playerComputer['hand'] = []
    playerComputer['discard'] = []
    playerComputer['active'] = []

    supplement = 10 * [Card('Levy', (1, 2), 2)]
    deck = list(itertools.chain.from_iterable(sharedDeck))
    random.shuffle(deck)
    centralDeck['deck'] = deck
    centralDeck['supplement'] = supplement
    centralDeck['active'] = []

    max = centralDeck['activeSize']
    count = 0
    while count < max:
        card = centralDeck['deck'].pop()
        centralDeck['active'].append(card)
        count = count + 1

    for x in range(0, playerOne['handsize']):
        if (len(playerOne['deck']) == 0):
            random.shuffle(playerOne['discard'])
            playerOne['deck'] = playerOne['discard']
            playerOne['discard'] = []
        card = playerOne['deck'].pop()
        playerOne['hand'].append(card)

    for x in range(0, playerOne['handsize']):
        if len(playerComputer['deck']) == 0:
            random.shuffle(playerOne['discard'])
            playerComputer['deck'] = playerComputer['discard']
            playerComputer['discard'] = []
        card = playerComputer['deck'].pop()
        playerComputer['hand'].append(card)

    printAvailCards(centralDeck)

    return (playerOne, playerComputer, centralDeck)
    
    
def endGameCheck(playerOne, playerComputer, centralDeck, continueGame):
  """
  Tests whether the game should end, based on the health of the players
  and the remaining cards in the central deck. 
  If the game should end, set continueGame = 0 and return it to the main.
  """
  if playerOne['health'] <= 0:
      continueGame = False
      print "Computer wins"
  elif playerComputer['health'] <= 0:
      continueGame = False
      print 'Player One Wins'
  elif centralDeck['activeSize'] == 0:
      print "No more cards available"
      if playerOne['health'] > playerComputer['health']:
          print "Player One Wins on Health"
      elif playerComputer['health'] > playerOne['health']:
          print "Computer Wins"
      else:
          pHT = 0
          pCT = 0 ##this doesn't make any sense
          if pHT > pCT:
              print "Player One Wins on Card Strength"
          elif pCT > pHT:
              print "Computer Wins on Card Strength"
          else:
              print "Draw"
      continueGame = False

  return continueGame
  
 
def rematch(playerOne, playerComputer, centralDeck):
  """
  Asks the user if they want a rematch. 
  If so, reset values of players and decks.
  """
  continueGame = 0
  aggressive = 0
  continueGame, aggressive = askToPlay()
  if continueGame == 1:
      playerOne, playerComputer, centralDeck = setUpPlayers()

  return (continueGame, aggressive, playerOne, playerComputer, centralDeck)




    

