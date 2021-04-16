# PlayingCard.py
# This Python class contains classes related to card objects.
# TJ Mendicino	101044387
# NamCao Nguyen	101046157

# Import libraries.
import random

# Class for a playing card.
class PlayingCard:
	# Constructor
	# Param: sFaceValue	Number value of the card
	# Param: sSuit		Suit of the card
	def __init__(self, sFaceValue, sSuit):
		self.sFaceValue = sFaceValue
		self.sSuit = sSuit
	
	# toString function to print the value of the card.
	def __str__(self):
		return self.sFaceValue + " of " + self.sSuit
	
	# Equality function to compare two playing cards.
	# Param: otherCard	The other playing card to compare with this one.
	def __eq__(self, otherCard):
		if (self.sFaceValue == otherCard.sFaceValue) and (self.sSuit == otherCard.sSuit):
			return True
		else:
			return False

# Class for a deck of cards.
class Deck:
	# Constructor
	def __init__(self):
		self.deck = []
		# Populate the deck with a full 52 card deck.
		self.deck.append(PlayingCard("A", "HEARTS"))
		self.deck.append(PlayingCard("2", "HEARTS"))
		self.deck.append(PlayingCard("3", "HEARTS"))
		self.deck.append(PlayingCard("4", "HEARTS"))
		self.deck.append(PlayingCard("5", "HEARTS"))
		self.deck.append(PlayingCard("6", "HEARTS"))
		self.deck.append(PlayingCard("7", "HEARTS"))
		self.deck.append(PlayingCard("8", "HEARTS"))
		self.deck.append(PlayingCard("9", "HEARTS"))
		self.deck.append(PlayingCard("10", "HEARTS"))
		self.deck.append(PlayingCard("J", "HEARTS"))
		self.deck.append(PlayingCard("Q", "HEARTS"))
		self.deck.append(PlayingCard("K", "HEARTS"))
		self.deck.append(PlayingCard("A", "SPADES"))
		self.deck.append(PlayingCard("2", "SPADES"))
		self.deck.append(PlayingCard("3", "SPADES"))
		self.deck.append(PlayingCard("4", "SPADES"))
		self.deck.append(PlayingCard("5", "SPADES"))
		self.deck.append(PlayingCard("6", "SPADES"))
		self.deck.append(PlayingCard("7", "SPADES"))
		self.deck.append(PlayingCard("8", "SPADES"))
		self.deck.append(PlayingCard("9", "SPADES"))
		self.deck.append(PlayingCard("10", "SPADES"))
		self.deck.append(PlayingCard("J", "SPADES"))
		self.deck.append(PlayingCard("Q", "SPADES"))
		self.deck.append(PlayingCard("K", "SPADES"))
		self.deck.append(PlayingCard("A", "CLUBS"))
		self.deck.append(PlayingCard("2", "CLUBS"))
		self.deck.append(PlayingCard("3", "CLUBS"))
		self.deck.append(PlayingCard("4", "CLUBS"))
		self.deck.append(PlayingCard("5", "CLUBS"))
		self.deck.append(PlayingCard("6", "CLUBS"))
		self.deck.append(PlayingCard("7", "CLUBS"))
		self.deck.append(PlayingCard("8", "CLUBS"))
		self.deck.append(PlayingCard("9", "CLUBS"))
		self.deck.append(PlayingCard("10", "CLUBS"))
		self.deck.append(PlayingCard("J", "CLUBS"))
		self.deck.append(PlayingCard("Q", "CLUBS"))
		self.deck.append(PlayingCard("K", "CLUBS"))
		self.deck.append(PlayingCard("A", "DIAMONDS"))
		self.deck.append(PlayingCard("2", "DIAMONDS"))
		self.deck.append(PlayingCard("3", "DIAMONDS"))
		self.deck.append(PlayingCard("4", "DIAMONDS"))
		self.deck.append(PlayingCard("5", "DIAMONDS"))
		self.deck.append(PlayingCard("6", "DIAMONDS"))
		self.deck.append(PlayingCard("7", "DIAMONDS"))
		self.deck.append(PlayingCard("8", "DIAMONDS"))
		self.deck.append(PlayingCard("9", "DIAMONDS"))
		self.deck.append(PlayingCard("10", "DIAMONDS"))
		self.deck.append(PlayingCard("J", "DIAMONDS"))
		self.deck.append(PlayingCard("Q", "DIAMONDS"))
		self.deck.append(PlayingCard("K", "DIAMONDS"))
		
		# Shuffle the deck.
		random.shuffle(self.deck)
	
	# toString function to print out all the cards in the deck.
	def __str__(self):
		# Initialize a return string.
		returnString = "Deck: "
		# Go through all the cards in the deck.
		for card in self.deck:
			returnString += str(card) + " \n"
		return returnString
	
	# Function to draw a card from the top of the deck.
	def drawCard(self):
		return self.deck.pop()
	
	# Function to check if the deck is out of cards.
	def isDeckEmpty(self):
		if len(self.deck) == 0:
			return True
		else:
			return False
	
	# Function to restock the deck if it has run out. The top card and the cards in the player's and AI's hand will not be restocked.
	# Param: topCard	The top card of the pile.
	# Param: playerHand	The player's hand of cards.
	# Param: aiHand		The AI's hand of cards.
	def restockDeck(self, topCard, playerHand, aiHand):
		# Populate the deck with a full 52 card deck.
		self.deck.append(PlayingCard("A", "HEARTS"))
		self.deck.append(PlayingCard("2", "HEARTS"))
		self.deck.append(PlayingCard("3", "HEARTS"))
		self.deck.append(PlayingCard("4", "HEARTS"))
		self.deck.append(PlayingCard("5", "HEARTS"))
		self.deck.append(PlayingCard("6", "HEARTS"))
		self.deck.append(PlayingCard("7", "HEARTS"))
		self.deck.append(PlayingCard("8", "HEARTS"))
		self.deck.append(PlayingCard("9", "HEARTS"))
		self.deck.append(PlayingCard("10", "HEARTS"))
		self.deck.append(PlayingCard("J", "HEARTS"))
		self.deck.append(PlayingCard("Q", "HEARTS"))
		self.deck.append(PlayingCard("K", "HEARTS"))
		self.deck.append(PlayingCard("A", "SPADES"))
		self.deck.append(PlayingCard("2", "SPADES"))
		self.deck.append(PlayingCard("3", "SPADES"))
		self.deck.append(PlayingCard("4", "SPADES"))
		self.deck.append(PlayingCard("5", "SPADES"))
		self.deck.append(PlayingCard("6", "SPADES"))
		self.deck.append(PlayingCard("7", "SPADES"))
		self.deck.append(PlayingCard("8", "SPADES"))
		self.deck.append(PlayingCard("9", "SPADES"))
		self.deck.append(PlayingCard("10", "SPADES"))
		self.deck.append(PlayingCard("J", "SPADES"))
		self.deck.append(PlayingCard("Q", "SPADES"))
		self.deck.append(PlayingCard("K", "SPADES"))
		self.deck.append(PlayingCard("A", "CLUBS"))
		self.deck.append(PlayingCard("2", "CLUBS"))
		self.deck.append(PlayingCard("3", "CLUBS"))
		self.deck.append(PlayingCard("4", "CLUBS"))
		self.deck.append(PlayingCard("5", "CLUBS"))
		self.deck.append(PlayingCard("6", "CLUBS"))
		self.deck.append(PlayingCard("7", "CLUBS"))
		self.deck.append(PlayingCard("8", "CLUBS"))
		self.deck.append(PlayingCard("9", "CLUBS"))
		self.deck.append(PlayingCard("10", "CLUBS"))
		self.deck.append(PlayingCard("J", "CLUBS"))
		self.deck.append(PlayingCard("Q", "CLUBS"))
		self.deck.append(PlayingCard("K", "CLUBS"))
		self.deck.append(PlayingCard("A", "DIAMONDS"))
		self.deck.append(PlayingCard("2", "DIAMONDS"))
		self.deck.append(PlayingCard("3", "DIAMONDS"))
		self.deck.append(PlayingCard("4", "DIAMONDS"))
		self.deck.append(PlayingCard("5", "DIAMONDS"))
		self.deck.append(PlayingCard("6", "DIAMONDS"))
		self.deck.append(PlayingCard("7", "DIAMONDS"))
		self.deck.append(PlayingCard("8", "DIAMONDS"))
		self.deck.append(PlayingCard("9", "DIAMONDS"))
		self.deck.append(PlayingCard("10", "DIAMONDS"))
		self.deck.append(PlayingCard("J", "DIAMONDS"))
		self.deck.append(PlayingCard("Q", "DIAMONDS"))
		self.deck.append(PlayingCard("K", "DIAMONDS"))
		
		# Remove the top card from the deck.
		self.deck.remove(topCard)
		# Go through all the cards in the player's hand.
		for card in playerHand.cards:
			# Remove the current card from the deck.
			self.deck.remove(card)
		# Go through all the cards in the AI's hand.
		for card in aiHand.cards:
			# Remove the current card from the deck.
			self.deck.remove(card)
			
		# Shuffle the deck.
		random.shuffle(self.deck)
	
	# Function to remove a card from the deck.
	def removeCard(self, cardToRemove):
		self.deck.remove(cardToRemove)

# Class for a hand of cards.
class Hand:
	# Constructor
	def __init__(self, cards):
		self.cards = cards
	
	# toString function to print out all the cards in the Hand.
	def __str__(self):
		# Initialize a return string.
		returnString = "Hand: \n"
		# Go through all the cards in the Hand.
		for i in range(0, len(self.cards)):
			returnString += str(i + 1) + " : " + str(self.cards[i]) + "\n"
		return returnString
	
	# Function to add a card to the player's hand.
	def pickUpCard(self, card):
		self.cards.append(card)
	
	# Function to remove a card from the player's hand.
	def removeCard(self, cardToRemove):
		self.cards.remove(cardToRemove)
	
	# Function to remove a card from the player's hand.
	# Param: nIndex	Index of the card to remove.
	def removeCardByIndex(self, nIndex):
		del self.cards[nIndex]
	
	# Function to check if the hand is empty (no cards left).
	def isHandEmpty(self):
		# If there are no cards left in the hand...
		if len(self.cards) == 0:
			return True
		else:
			return False