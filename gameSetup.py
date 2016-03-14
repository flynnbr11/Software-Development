import itertools, random
from new_dbc import *

class Card(object):
    def __init__(self, name, values=(0, 0), cost=1, clan=None):
        self.name = name
        self.cost = cost
        self.values = values
        self.clan = clan
    def __str__(self):
                return 'Name %s costing %s with attack %s and money %s' % (self.name, self.cost, self.values[0], self.values[1])
    def get_attack(self):
        return self.values[0]
    def get_money(self):
            return self.values[1]

def setUpPlayers():
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
  
 
def newGame(continueGame, oT, playerOne, playerComputer, centralDeck):
  
  playGame = raw_input("\nDo you want to play another game?:")
  continueGame = (playGame=='Y')
  if continueGame:
      oT = raw_input("Do you want an aggressive (A) opponent or an acquisative (Q) opponent")
      aggressive = (oT=='A')
      
      playerOne, playerComputer, centralDeck = setUpPlayers()

      printAvailCards(centralDeck)
        
  return (continueGame, oT, playerOne, playerComputer, centralDeck)
    

