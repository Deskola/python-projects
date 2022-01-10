#HigherOrLower

from math import inf
import random

#Card constants
SUIT_TUPLE = ('Spades', 'Heart', 'Clubs', 'Diamond')
RANK_TUPLE = ('ACE','2','3','4','5','6','7','8','9','10','Jack','Queen','King')

NCARD = 8

# Pass in a deck and this function returns a random card from the deck
def getCard(deckListIn):
    thisCard = deckListIn.pop() #pop one off the top of deck and return
    return thisCard

# Pass in a deck and this function returns a shuffled copy of the deck 
def shuffle(deckListIn):
    deckListOut = deckListIn.copy() #make a copy of the starting deck
    random.shuffle(deckListOut)
    return deckListOut

#Main code
print('Welcome to Higher or Lower.')
print('You have to choose wheter the next card to be shown will be higher or lower than the current card.')
print('Getting it right adds 20 points ;); get it wron and you lose 15 points:(')
print('You have 50 points to start:)')
print()

startingDeckList = []
for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank': rank, 'suit': suit, 'value': thisValue+1}
        startingDeckList.append(cardDict)

score = 50

while True:
    print()
    gameDeckList = shuffle(startingDeckList)

    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']

    print('Starting card is: '+ currentCardRank +' of '+currentCardSuit)
    print()

    for cardNumber in range(0, NCARD): #play one game of many cards
        answer = input('Will the next card be higher or lower than the '+ currentCardRank + ' of '+ currentCardSuit + '? (enter h or l):')
        answer = answer.casefold() #force lowercase

        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']

        print('Next card is:', nextCardRank + ' of '+ nextCardSuit)

        if answer == 'h':
            if nextCardValue > currentCardValue:
                print('You got it right, it was higher')
                score = score + 20
            else:
                print('Sorry, it was not higher')
                score = score - 15
        elif answer == 'l':
            if nextCardValue < currentCardValue:
                score = score + 20
                print('You got it right, it was lower')
                score = score + 20
            else:
                score = score - 15
                print('Sorry, it was not lower')

        print('Your score is:', score)
        print()
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue # don't need current suit

    goAgain = input('To play again, Please ENTER, or "q" to quit: ')
    if goAgain == 'q':
        break
print('OK bye')
                






