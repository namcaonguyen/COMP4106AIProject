# NamCao Nguyen
# Class for testing stuff...
# test2.py

# Import libraries.
import CardClasses
import GameFunctions
import AI

incompleteDeck2 = []
incompleteDeck2.append(CardClasses.PlayingCard("2", "DIAMONDS"))
incompleteDeck2.append(CardClasses.PlayingCard("Q", "SPADES"))
incompleteDeck2.append(CardClasses.PlayingCard("K", "DIAMONDS"))
incompleteDeck2.append(CardClasses.PlayingCard("4", "CLUBS"))
incompleteDeck2.append(CardClasses.PlayingCard("10", "DIAMONDS"))
incompleteDeck2.append(CardClasses.PlayingCard("6", "CLUBS"))
incompleteDeck2.append(CardClasses.PlayingCard("7", "SPADES"))
incompleteDeck2.append(CardClasses.PlayingCard("10", "SPADES"))
incompleteDeck2.append(CardClasses.PlayingCard("2", "CLUBS"))
incompleteDeck2.append(CardClasses.PlayingCard("J", "SPADES"))
incompleteDeck2.append(CardClasses.PlayingCard("A", "CLUBS"))
incompleteDeck2.append(CardClasses.PlayingCard("7", "CLUBS"))
incompleteDeck2.append(CardClasses.PlayingCard("3", "CLUBS"))
incompleteDeck2.append(CardClasses.PlayingCard("Q", "CLUBS"))
incompleteDeck2.append(CardClasses.PlayingCard("K", "SPADES"))
incompleteDeck2.append(CardClasses.PlayingCard("7", "DIAMONDS"))
incompleteDeck2.append(CardClasses.PlayingCard("4", "SPADES"))
incompleteDeck2.append(CardClasses.PlayingCard("6", "SPADES"))
incompleteDeck2.append(CardClasses.PlayingCard("4", "DIAMONDS"))
incompleteDeck2.append(CardClasses.PlayingCard("5", "SPADES"))
incompleteDeck2.append(CardClasses.PlayingCard("10", "CLUBS"))
incompleteDeck2.append(CardClasses.PlayingCard("6", "DIAMONDS"))
incompleteDeck2.append(CardClasses.PlayingCard("K", "CLUBS"))

incompleteDeck2.append(CardClasses.PlayingCard("8", "SPADES"))
incompleteDeck2.append(CardClasses.PlayingCard("9", "CLUBS"))
incompleteDeck2.append(CardClasses.PlayingCard("8", "HEARTS"))
incompleteDeck2.append(CardClasses.PlayingCard("7", "HEARTS"))
incompleteDeck2.append(CardClasses.PlayingCard("10", "HEARTS"))
incompleteDeck2.append(CardClasses.PlayingCard("9", "DIAMONDS"))
incompleteDeck2.append(CardClasses.PlayingCard("9", "SPADES"))
incompleteDeck2.append(CardClasses.PlayingCard("J", "HEARTS"))
incompleteDeck2.append(CardClasses.PlayingCard("8", "DIAMONDS"))
incompleteDeck2.append(CardClasses.PlayingCard("8", "CLUBS"))
incompleteDeck2.append(CardClasses.PlayingCard("5", "HEARTS"))
incompleteDeck2.append(CardClasses.PlayingCard("3", "HEARTS"))
incompleteDeck2.append(CardClasses.PlayingCard("4", "HEARTS"))
incompleteDeck2.append(CardClasses.PlayingCard("6", "HEARTS"))
incompleteDeck2.append(CardClasses.PlayingCard("A", "HEARTS"))
incompleteDeck2.append(CardClasses.PlayingCard("Q", "HEARTS"))
incompleteDeck2.append(CardClasses.PlayingCard("2", "HEARTS"))
incompleteDeck2.append(CardClasses.PlayingCard("K", "HEARTS"))

incompleteDeck2.append(CardClasses.PlayingCard("5", "DIAMONDS"))
incompleteDeck2.append(CardClasses.PlayingCard("2", "SPADES"))
incompleteDeck2.append(CardClasses.PlayingCard("5", "CLUBS"))
incompleteDeck2.append(CardClasses.PlayingCard("A", "SPADES"))
incompleteDeck2.append(CardClasses.PlayingCard("J", "DIAMONDS"))
incompleteDeck2.append(CardClasses.PlayingCard("3", "SPADES"))
incompleteDeck2.append(CardClasses.PlayingCard("Q", "DIAMONDS"))
incompleteDeck2.append(CardClasses.PlayingCard("A", "DIAMONDS"))
incompleteDeck2.append(CardClasses.PlayingCard("J", "CLUBS"))
incompleteDeck2.append(CardClasses.PlayingCard("3", "DIAMONDS"))
incompleteDeck2.append(CardClasses.PlayingCard("9", "HEARTS"))

aiHand2 = CardClasses.Hand([])
playerHand2 = CardClasses.Hand([])
for i in range(0,5):
	aiHand2.pickUpCard(incompleteDeck2.pop())
	playerHand2.pickUpCard(incompleteDeck2.pop())
topCard2 = incompleteDeck2.pop()

aiObservedCardsModelList2 = []
aiObservedCardsModelList2 = GameFunctions.initializeAIObservedCardsModel(topCard2, aiHand2)
# Remove cards from the deck and add it to the AI's observed model.
for i in range(0, 18):
	aiObservedCardsModelList2.append(incompleteDeck2.pop())

print("Here is the top card: " + str(topCard2))

AI.beginAdversarySearch(aiObservedCardsModelList2, topCard2, aiHand2, True)