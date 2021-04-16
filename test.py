# NamCao Nguyen
# Class for testing stuff...
# test.py

# Import libraries.
import CardClasses
import GameFunctions
import AI

print("Here's the binary for 1: " + str(AI.getBinaryList(1, 6)))
print("Here's the binary for 2: " + str(AI.getBinaryList(2, 6)))
print("Here's the binary for 3: " + str(AI.getBinaryList(3, 6)))
print("Here's the binary for 4: " + str(AI.getBinaryList(4, 6)))
print("Here's the binary for 5: " + str(AI.getBinaryList(5, 6)))
print("Here's the binary for 6: " + str(AI.getBinaryList(6, 6)))
print("Here's the binary for 7: " + str(AI.getBinaryList(7, 6)))
print("Here's the binary for 8: " + str(AI.getBinaryList(8, 6)))
print("Here's the binary for 16: " + str(AI.getBinaryList(15, 6)))

fiveOfHeartsCard = CardClasses.PlayingCard("5", "HEARTS")
fiveOfHeartsCard2 = CardClasses.PlayingCard("5", "HEARTS")
fiveOfClubsCard = CardClasses.PlayingCard("5", "CLUBS")
threeOfHeartsCard = CardClasses.PlayingCard("3", "HEARTS")
eightOfDiamondsCard = CardClasses.PlayingCard("8", "DIAMONDS")

print("This should return true: " + str(fiveOfHeartsCard == fiveOfHeartsCard2))
print("This should return false: " + str(fiveOfHeartsCard == fiveOfClubsCard))

fullDeck = CardClasses.Deck()

subset1 = []
subset1.append(fiveOfHeartsCard)
subset1.append(fiveOfClubsCard)

print("Here are all cards in a full deck that are compatible with 5 of HEARTS and 5 of CLUBS:")
compatibleList1 = GameFunctions.getListOfCompatibleCardsForSubsetOfCards(fullDeck.deck, subset1, fiveOfHeartsCard)
for card in compatibleList1:
	print(card)
print("Here's the probability that one of those cards will be played from a full deck: " + str(GameFunctions.calculateProbabilityThatCompatibleCardWillBePlayed(fullDeck.deck, subset1, fiveOfHeartsCard)))

subset2 = []
subset2.append(fiveOfHeartsCard)
subset2.append(threeOfHeartsCard)
print("Here are all cards in a full deck that are compatible with 5 of HEARTS and 3 of HEARTS:")
compatibleList2 = GameFunctions.getListOfCompatibleCardsForSubsetOfCards(fullDeck.deck, subset2, fiveOfHeartsCard)
for card in compatibleList2:
	print(card)
print("Here's the probability that one of those cards will be played from a full deck: " + str(GameFunctions.calculateProbabilityThatCompatibleCardWillBePlayed(fullDeck.deck, subset2, fiveOfHeartsCard)))

subset3 = []
subset3.append(eightOfDiamondsCard)
subset3.append(threeOfHeartsCard)
print("Here are all cards in a full deck that are compatible with 8 of DIAMONDS and 3 of HEARTS:")
compatibleList3 = GameFunctions.getListOfCompatibleCardsForSubsetOfCards(fullDeck.deck, subset3, eightOfDiamondsCard)
for card in compatibleList3:
	print(card)
print("Here's the probability that one of those cards will be played from a full deck: " + str(GameFunctions.calculateProbabilityThatCompatibleCardWillBePlayed(fullDeck.deck, subset3, eightOfDiamondsCard)))

incompleteDeck = []
incompleteDeck.append(CardClasses.PlayingCard("2", "DIAMONDS"))
incompleteDeck.append(CardClasses.PlayingCard("Q", "SPADES"))
incompleteDeck.append(CardClasses.PlayingCard("K", "DIAMONDS"))
incompleteDeck.append(CardClasses.PlayingCard("4", "CLUBS"))
incompleteDeck.append(CardClasses.PlayingCard("10", "DIAMONDS"))
incompleteDeck.append(CardClasses.PlayingCard("6", "CLUBS"))
incompleteDeck.append(CardClasses.PlayingCard("7", "SPADES"))
incompleteDeck.append(CardClasses.PlayingCard("10", "SPADES"))
incompleteDeck.append(CardClasses.PlayingCard("2", "CLUBS"))
incompleteDeck.append(CardClasses.PlayingCard("J", "SPADES"))
incompleteDeck.append(CardClasses.PlayingCard("A", "HEARTS"))
incompleteDeck.append(CardClasses.PlayingCard("Q", "HEARTS"))
incompleteDeck.append(CardClasses.PlayingCard("2", "HEARTS"))
incompleteDeck.append(CardClasses.PlayingCard("K", "HEARTS"))
incompleteDeck.append(CardClasses.PlayingCard("A", "CLUBS"))
incompleteDeck.append(CardClasses.PlayingCard("7", "CLUBS"))
incompleteDeck.append(CardClasses.PlayingCard("8", "DIAMONDS"))
incompleteDeck.append(CardClasses.PlayingCard("9", "SPADES"))
incompleteDeck.append(CardClasses.PlayingCard("J", "HEARTS"))
incompleteDeck.append(CardClasses.PlayingCard("3", "CLUBS"))
incompleteDeck.append(CardClasses.PlayingCard("6", "HEARTS"))
incompleteDeck.append(CardClasses.PlayingCard("Q", "CLUBS"))
incompleteDeck.append(CardClasses.PlayingCard("4", "HEARTS"))
incompleteDeck.append(CardClasses.PlayingCard("8", "CLUBS"))
incompleteDeck.append(CardClasses.PlayingCard("K", "SPADES"))
incompleteDeck.append(CardClasses.PlayingCard("7", "DIAMONDS"))
incompleteDeck.append(CardClasses.PlayingCard("5", "HEARTS"))
incompleteDeck.append(CardClasses.PlayingCard("3", "HEARTS"))
incompleteDeck.append(CardClasses.PlayingCard("4", "SPADES"))
incompleteDeck.append(CardClasses.PlayingCard("6", "SPADES"))
incompleteDeck.append(CardClasses.PlayingCard("4", "DIAMONDS"))
incompleteDeck.append(CardClasses.PlayingCard("5", "SPADES"))
incompleteDeck.append(CardClasses.PlayingCard("9", "DIAMONDS"))
incompleteDeck.append(CardClasses.PlayingCard("10", "HEARTS"))
incompleteDeck.append(CardClasses.PlayingCard("10", "CLUBS"))
incompleteDeck.append(CardClasses.PlayingCard("7", "HEARTS"))
incompleteDeck.append(CardClasses.PlayingCard("6", "DIAMONDS"))
incompleteDeck.append(CardClasses.PlayingCard("8", "HEARTS"))
incompleteDeck.append(CardClasses.PlayingCard("9", "CLUBS"))
incompleteDeck.append(CardClasses.PlayingCard("K", "CLUBS"))
incompleteDeck.append(CardClasses.PlayingCard("3", "SPADES"))
incompleteDeck.append(CardClasses.PlayingCard("5", "DIAMONDS"))
incompleteDeck.append(CardClasses.PlayingCard("2", "SPADES"))
incompleteDeck.append(CardClasses.PlayingCard("5", "CLUBS"))
incompleteDeck.append(CardClasses.PlayingCard("A", "SPADES"))
incompleteDeck.append(CardClasses.PlayingCard("J", "DIAMONDS"))
incompleteDeck.append(CardClasses.PlayingCard("8", "SPADES"))
incompleteDeck.append(CardClasses.PlayingCard("Q", "DIAMONDS"))
incompleteDeck.append(CardClasses.PlayingCard("A", "DIAMONDS"))
incompleteDeck.append(CardClasses.PlayingCard("J", "CLUBS"))
incompleteDeck.append(CardClasses.PlayingCard("3", "DIAMONDS"))
incompleteDeck.append(CardClasses.PlayingCard("9", "HEARTS"))

aiHand = CardClasses.Hand([])
playerHand = CardClasses.Hand([])
for i in range(0,5):
	aiHand.pickUpCard(incompleteDeck.pop())
	playerHand.pickUpCard(incompleteDeck.pop())
topCard = incompleteDeck.pop()

aiObservedCardsModelList = []
aiObservedCardsModelList = GameFunctions.initializeAIObservedCardsModel(topCard, aiHand)

print("Here is the top card: " + str(topCard))

# Test the beginAdversarySearch() function.
AI.beginAdversarySearch(aiObservedCardsModelList, topCard, aiHand, True)



print("\n\n")
def testRecursionStart():
	list = []
	list.append(1)
	list = testRecursion(2, list)
	list = testRecursion(2.5, list)
	list = testRecursion(2.7, list)
	print(list)
	
def testRecursion(nNumParam, listParam):
	listParam.append(nNumParam)
	if nNumParam < 10:
		testRecursion(nNumParam + 1, listParam)
	return listParam

print("Gonna test a recursion thing:")
testRecursionStart()


