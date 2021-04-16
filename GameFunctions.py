# GameFunctions.py
# This Python class contains game functions.
# TJ Mendicino	101044387
# NamCao Nguyen	101046157

# Import libraries.
import CardClasses

# Function to check if the given card to be played is compatible with the top card.
# Param: topCardParam	The top card of the pile.
# Param: givenCardParam	The given card to be checked.
def isCardCompatible(topCardParam, givenCardParam):
	# If the cards have the same face value or suit, or the given card matches the chosen suit, or the given card is an 8, then it is compatible.
	if (topCardParam.sFaceValue == givenCardParam.sFaceValue) or (topCardParam.sSuit == givenCardParam.sSuit) or (givenCardParam.sFaceValue == "8"):
		return True
	else:
		return False

# Function to check if the hand has any cards compatible with the top card.
# Param: topCardParam	The top card of the pile.
# Param: handParam		The hand of cards to check.
def doesHandHaveCompatibleCard(topCardParam, handParam):
	# Go through each card in the hand.
	for card in handParam.cards:
		# If the current card is compatible with the top card, then return true.
		if isCardCompatible(topCardParam, card):
			return True
	return False

# Function to get a list of cards in the hand that are compatible with the top card.
# Param: topCardParam	The top card of the pile.
# Param: handParam		The hand of cards to check.
def getCompatibleCardsList(topCardParam, handParam):
	# Declaration of list.
	compatibleCardsList = []
	# Go through each card in the hand.
	for card in handParam.cards:
		# If the current card is compatible with the top card...
		if isCardCompatible(topCardParam, card):
			# Append it to the list.
			compatibleCardsList.append(card)
	return compatibleCardsList

# Function to get the changed suit for a Crazy Eight play.
def getSuitForCrazyEight():
	print("You played a Crazy Eight!")
	while True:
		# Get the user's input on which suit to change the top card to.
		sNewSuit = input("Select a suit to change the top card to (1 - HEARTS, 2 - SPADES, 3 - CLUBS, 4 - DIAMONDS): ")
		# If the Player chooses "HEARTS"...
		if sNewSuit == "1":
			return CardClasses.PlayingCard("8", "HEARTS")
		# If the Player chooses "SPADES"...
		elif sNewSuit == "2":
			return CardClasses.PlayingCard("8", "SPADES")
		# If the Player chooses "CLUBS"...
		elif sNewSuit == "3":
			return CardClasses.PlayingCard("8", "CLUBS")
		# If the Player chooses "DIAMONDS"...
		elif sNewSuit == "4":
			return CardClasses.PlayingCard("8", "DIAMONDS")
		# Else, the player chose something else...
		else:
			print("Please choose one of the suits!!!")

# Function to display the number of cards in the given hand.
# Param: sNameParam	The name of the hand owner.
# Param: handParam	The hand of cards.
def displayNumberOfCardsInHand(sNameParam, handParam):
	print(sNameParam + " now has " + str(len(handParam.cards)) + " cards left.")

# Function to initialize the AI's observed cards model. This function will need to be called every time the deck is restocked.
# Param: topCardParam	The top card of the pile.
# Param: aiHandParam	The AI's hand of cards.
def initializeAIObservedCardsModel(topCardParam, aiHandParam):
	# Declaration of variable for the AI's model of observed cards.
	aiObservedCardsModel = []
	# Add the top card and the AI's hand to its model of observed cards.
	aiObservedCardsModel.append(topCardParam)
	for card in aiHandParam.cards:
		aiObservedCardsModel.append(card)
	return aiObservedCardsModel

# Function to create a card subset of a hand based on a list of binary values.
# Param: potentialCompatibilityListParam	List of binary values to create the card subset. Each 1 corresponds to a card to add to the subset.
# Param: currentHandParam					The current hand of cards. Its length should match the length of the potentialCompatibilityListParam.
def createCardSubsetFromCompatibilityList(potentialCompatibilityListParam, currentHandParam):
	# Declaration of variable for the card subset to return.
	cardSubset = []
	# Go through every card in the hand.
	for i in range(0, len(potentialCompatibilityListParam)):
		# If the current value is a 1...
		if potentialCompatibilityListParam[i] == 1:
			# Add the corresponding card of the hand to the card subset.
			cardSubset.append(currentHandParam.cards[i])
	return cardSubset

# Function to get a list of compatible cards from a list of potential cards for a subset of cards.
# All cards in the returned list must be compatible with the given card subset.
# Param: potentialCardsParam	Potential cards to make the list of compatible cards with.
# Param: cardSubsetParam		Subset of cards that the returned list must be compatible with.
# Param: topCardParam			The top card of the pile.
def getListOfCompatibleCardsForSubsetOfCards(potentialCardsParam, cardSubsetParam, topCardParam):
	# Declaration of variable for the list.
	listOfCompatibleCards = []
	# Go through all the cards in the potential cards parameter.
	for cardIterator in potentialCardsParam:
		# Declaration of boolean variable for if the current card is compatible with all cards in the subset.
		bIsCurrentCardCompatible = True
		# Go through all the cards in the subset parameter.
		for cardIterator2 in cardSubsetParam:
			# If the current card is NOT compatible with a card in the subset parameter...
			if isCardCompatible(cardIterator, cardIterator2) == False:	# Note: The 'cardIterator2' varible MUST be the second argument in this function because of how Crazy Eights are handled.
				# Set the variable to false and break out of the loop.
				bIsCurrentCardCompatible = False
				break
		# If the current card is NOT compatible with the top card...
		if isCardCompatible(topCardParam, cardIterator):
			# Set the variable to false.
			bIsCurrentCardCompatible = False
		# If the current card is compatible with all cards in the subset...
		if bIsCurrentCardCompatible == True:
			# Append the current card to the list.
			listOfCompatibleCards.append(cardIterator)
	return listOfCompatibleCards

# Function to get a list of compatible cards according to a compatibility list (list of binary values).
# All cards in the returned list must be compatible/incompatible with the ones in the hand in correspondence with the compatibility list.
# For example, if the compatibility list is [0,1,0,1], then all cards in the returned list must be [incompatible,compatible,incompatible,compatible] with the hand.
def getListOfCompatibleCardsAccordingToCompatibilityList(potentialCardsParam, handParam, compatibilityListParam, topCardParam):
	# Declaration of variable for the list.
	listOfCompatibleCards = []
	# Go through all the cards in the potential cards parameter.
	for cardIterator in potentialCardsParam:
		# Declaration of boolean variable for if the current card satisfies the compatibility list.
		bIsCurrentCardValid = True
		# Go through the compatibility list.
		for i in range(0, len(compatibilityListParam)):
			# If the current element is 0, then the current card should be incompatible with the i-th card in the hand.
			if compatibilityListParam[i] == 0:
				# If the current card IS compatible with the i-th card in the hand...
				if isCardCompatible(cardIterator, handParam.cards[i]) == True: # Note: The 'handParam.cards[i]' varible MUST be the second argument in this function because of how Crazy Eights are handled.
					# Set the variable to false and break out of the loop.
					bIsCurrentCardValid = False
					break
			# Else, the current element is 1, then the current card should be compatible with the i-th card in the hand.
			else:
				# If the current card is NOT compatible with the i-th card in the hand...
				if isCardCompatible(cardIterator, handParam.cards[i]) == False: # Note: The 'handParam.cards[i]' varible MUST be the second argument in this function because of how Crazy Eights are handled.
					# Set the variable to false and break out of the loop.
					bIsCurrentCardValid = False
					break
		# If the current card is NOT compatible with the top card...
		if isCardCompatible(topCardParam, cardIterator) == False:
			# Set the variable to false.
			bIsCurrentCardValid = False
		# If the current card satisfies the compatibility list and is compatible with the top card...
		if bIsCurrentCardValid == True:
			# Append the current card to the list.
			listOfCompatibleCards.append(cardIterator)
	return listOfCompatibleCards

# Function to get a list of compatible cards from a list of potential cards for one singular top card.
# Param: potentialCardsParam	Potential cards to make the list of compatible cards with.
# Param: topCardParam			The top card of the pile.
def getListOfCompatibleCardsForTopCard(potentialCardsParam, topCardParam):
	# Declaration of variable for the list.
	listOfCompatibleCards = []
	# Go through all the cards in the potential cards parameter.
	for card in potentialCardsParam:
		# If the current card is compatible with the top card...
		if isCardCompatible(topCardParam, card) == True:
			# Append the current card to the list.
			listOfCompatibleCards.append(card)
	return listOfCompatibleCards

# Function to calculate the probability that a card from the unseen cards will be played that is compatible with a subset of cards.
# Param: unobservedCardsParam	Cards that have not been observed by the AI yet.
# Param: cardSubsetParam		Subset of cards that the played card must be compatible with.
# Param: topCardParam			The top card of the pile.
def calculateProbabilityThatCompatibleCardWillBePlayed(unobservedCardsParam, cardSubsetParam, topCardParam):
	return len(getListOfCompatibleCardsForSubsetOfCards(unobservedCardsParam, cardSubsetParam, topCardParam)) / len(getListOfCompatibleCardsForTopCard(unobservedCardsParam, topCardParam))

def calculateProbabilityThatCardAccordingToCompatibilityListWillBePlayed(unobservedCardsParam, handParam, compatibilityListParam, topCardParam):
	if len(getListOfCompatibleCardsForTopCard(unobservedCardsParam, topCardParam)) == 0:
		return 0
	return len(getListOfCompatibleCardsAccordingToCompatibilityList(unobservedCardsParam, handParam, compatibilityListParam, topCardParam)) / len(getListOfCompatibleCardsForTopCard(unobservedCardsParam, topCardParam))

# Function to do the player's turn.
# Param: topCardParam		The top card of the pile.
# Param: playerHandParam	The player's hand of cards.
# Param: gameDeckParam		The game deck.
def doPlayerTurn(topCardParam, playerHandParam, gameDeckParam):
	while True:
		# Display the top card.
		print("Here is the top card: " + str(topCardParam))
		# Display the player's hand.
		print(str(playerHandParam))
		# Display the user's options.
		print("Here are your options:")
		print("0 - Draw a card.")
		print("1 - Play a card.")
		# Get the user's input on what they want to do.
		sUserChoice = input("What do you want to do? ")
		
		# If the user wants to draw a card...
		if sUserChoice == "0":
			# If the deck isn't empty...
			if gameDeckParam.isDeckEmpty() == False:
				# Draw one card from the deck and add it to the player's hand.
				drewCard = gameDeckParam.drawCard()
				playerHandParam.pickUpCard(drewCard)
				# Display the drawn card on screen.
				print("You drew a " + str(drewCard) + ".\n")
			# Else, there are no cards left in the deck...
			else:
				# If there is a compatible card in the hand...
				if doesHandHaveCompatibleCard(topCardParam, playerHandParam) == True:
					print("There are no cards left in the deck! Please play a card.\n")
				# Else, the player can't play any of the cards in their hand...
				else:
					print("There are no cards left in the deck, and you don't have any compatible cards! Skipping your turn...\n")
					# The player's turn is over. Return the top card, the player's hand, and the game deck, which have all been affected.
					return (topCardParam, playerHandParam, gameDeckParam)
		# If the user wants to play a card...
		elif sUserChoice == "1":
			# Get the user's input on which card they want to play.
			nCardToPlay = int(input("Pick a card to play: "))
			
			# If the card index is in range of the player's hand...
			if nCardToPlay in range(1, len(playerHandParam.cards) + 1):
				# If the chosen card is valid to play on the top card...
				if isCardCompatible(topCardParam, playerHandParam.cards[nCardToPlay - 1]) == True:
					# Set the new top card.
					topCardParam = playerHandParam.cards[nCardToPlay - 1]
					# If the card played was a Crazy Eight...
					if topCardParam.sFaceValue == "8":
						# Ask the user to set a suit for the top card.
						topCardParam = getSuitForCrazyEight()
					# Remove the played card from the player's hand.
					playerHandParam.removeCardByIndex(nCardToPlay - 1)
					# Display the new top card.
					print("This card is compatible! The top card is now " + str(topCardParam) + ".\n")
					# The player's turn is over. Return the top card, the player's hand, and the game deck, which have all been affected.
					return (topCardParam, playerHandParam, gameDeckParam)
				else:
					print(str(playerHandParam.cards[nCardToPlay - 1]) + " is NOT compatible with " + str(topCardParam) + "!\n")
			# Else, the player chose an index that they don't have...
			else:
				print("That's not a card you have!\n")
		# Else, the user said something else...
		else:
			print("That's not an option!\n")

