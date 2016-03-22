import itertools, random
from cardClass import *
from playerFunctions import * 
from computerFunctions import *
from printFunctions import *
from gameSetupAndPlayFunctions import *

if __name__ == '__main__':
  """
  Initialise player, computer and shared decks
  """
  playerOne, playerComputer, centralDeck = setUpPlayers() #initialise players and decks ??? - is this the same as is done when replay?
  
  continueGame, aggressive = askToPlay()

  """ 
  Main Gameplay
  """
  while continueGame: 
      playerOne, playerComputer, centralDeck = userTurn(playerOne, 
          playerComputer, centralDeck)

      playerOne, playerComputer, centralDeck = computerTurn(playerOne, 
          playerComputer, centralDeck, aggressive)

      """
      Show player current values
      """
      printAvailCards(centralDeck)
      printHealths(playerOne, playerComputer)

      """
      Test whether this round of moves has caused the end of the game.
      If so, continueGame = 0. 
      """
      continueGame = endGameCheck(playerOne, playerComputer, 
          centralDeck, continueGame)

      """
      If game is over, ask to play again. If so, reset values. 
      If not, while loop terminates and program exits. 
      """
      if not continueGame: 
          continueGame, aggressive, playerOne, playerComputer, centralDeck = rematch(playerOne,
              playerComputer, centralDeck)
  exit()
