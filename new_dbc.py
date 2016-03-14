import itertools, random
from cardClass import *
from playerFunctions import * 
from computerFunctions import *
from printFunctions import *
from gameSetupAndPlayFunctions import *

if __name__ == '__main__':

    playerOne, playerComputer, centralDeck = setUpPlayers() #initialise players and decks ??? - is this the same as is done when replay?
    
    playGame = raw_input('Do you want to play a game?: \n')
    continueGame = (playGame=='Y')
    oT = raw_input("Do you want an aggressive (A) opponent or an acquisative (Q) opponent \n")
    aggressive = (oT=='A')

    while continueGame: #Gameplay
        playerOne, playerComputer, centralDeck = userTurn(playerOne, playerComputer, centralDeck)

        playerOne, playerComputer, centralDeck = computerTurn(playerOne, playerComputer, centralDeck, aggressive)

        printAvailCards(centralDeck)
        printHealths(playerOne, playerComputer)

        # test if game is over
        continueGame = endGameCheck(playerOne, playerComputer, centralDeck, continueGame)

        if not continueGame: #game has ended, ask whether to play again
            continueGame, oT, playerOne, playerComputer, centralDeck = newGame(continueGame, oT, playerOne, playerComputer, centralDeck)
    exit()
