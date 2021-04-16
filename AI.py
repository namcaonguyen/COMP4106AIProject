# AI.py
# This Python class contains code for the AI.
# TJ Mendicino	101044387
# NamCao Nguyen	101046157

# Import libraries.
import decimal
import random
import CardClasses
import GameFunctions

# Class for a State node.
class StateNode:
	# Constructor
	# Param: bIsRootNode		Boolean for if this state is a root node, meaning it has no parent node.
	# Param: nTerminalStateType	Integer which denotes what type of terminal state this is, if it is one (0 - NULL, 1 - WINNER, 2 - DRAW_CARD).
	# Param: bIsAINode			Boolean for if this is an AI node. If it isn't, then it is a player node (adversary ply).
	# Param: nDepth				Integer for the node's depth in the tree.
	# Param: nProbability		The probability that we'll reach this node.
	# Param: topCard			The top card of the pile.
	# Param: parentNode			The parent node for this node.
	# Param: currentHand		The current hand of cards.
	# Param: compatibilityList	List of binary values to denote which cards in the hand are compatible.
	def __init__(self, bIsRootNode, nTerminalStateType, bIsAINode, nDepth, nProbability, parentNode, topCard, currentHand, compatibilityList):
		# Initialize member variables.
		self.bIsRootNode = bIsRootNode																# Boolean for if this state is a root node, meaning it has no parent node.
		self.nTerminalStateType = nTerminalStateType												# Integer which denotes what type of terminal state this is, if it is one (0 - NULL, 1 - WINNER, 2 - DRAW_CARD).
		self.bIsAINode = bIsAINode																	# Boolean for if this is an AI node. If it isn't, then it is a player node (adversary ply).
		self.nDepth = nDepth																		# Integer for the node's depth in the tree.
		self.nProbability = nProbability															# Probability that the previous action was taken to reach this state.
		self.parentNode = parentNode																# The parent node for this node.
		self.topCard = topCard																		# The top card of the pile.
		self.currentHand = currentHand																# The current hand of cards.
		self.compatibilityList = compatibilityList													# List of binary values to denote which cards in the hand are compatible.
		self.nNumCompatibleCards = len(GameFunctions.getCompatibleCardsList(topCard, currentHand))	# The number of cards in the current hand that are compatible with the top card.

		self.childNodeList = []
	
	def __str__(self):
		sReturnString = ""
		if self.bIsRootNode == True:
			sReturnString += "ROOT "
		if self.bIsAINode == True:
			sReturnString += "AI "
		else:
			sReturnString += "Player "
		sReturnString += "node at depth " + str(self.nDepth) + ". "
		sReturnString += "Here are the cards in the hand: " + str(self.currentHand)
		sReturnString += "And here is the compatibility list: " + str(self.compatibilityList)
		sReturnString += " The probability of reaching this state from the parent state is " + str(self.nProbability) + "."
		if self.nTerminalStateType == 1:
			sReturnString += "This is a WINNER Terminal State!"
		elif self.nTerminalStateType == 2:
			sReturnString += "This is a DRAW_CARD Terminal State!"
		return sReturnString

# Function to get a binary list, with each element being a list.
# Param: nNumParam		The number to convert to a binary list.
# Param: nNumBitsParam	The desired length of the binary list.
def getBinaryList(nNumParam, nNumBitsParam):
	bitList = []
	# Go through the number of desired bits.
	for bit in range(nNumBitsParam -1, -1, -1):
		bitList.append((nNumParam >> bit) & 1)
	return bitList

# Function to create a Player State Child Node. It will also create any child AI nodes for that node if needed.
def createPlayerStateChildNode(stateNodeListParam, bPlayCardPossible, nDepthParam, aiObservedCardsModelParam, chosenCardParam, parentNodeParam, aiHandParam):
	# If the AI played their last card to reach this state...
	if (bPlayCardPossible == True) and (len(aiHandParam.cards) == 0):
		# Create a "WINNER" Terminal State Node.
		stateNodeListParam.append(StateNode(False, 1, False, nDepthParam, 1, parentNodeParam, chosenCardParam, aiHandParam, None))
	# Else if the AI was able to play a card to reach this state...
	elif bPlayCardPossible == True:
		
		# Declaration of variable for a list of cards unobserved by the AI's model.
		unobservedCards = CardClasses.Deck()
		# Go through all the AI's observed cards.
		for card in aiObservedCardsModelParam:
			# If the card is in the unobserved cards model.
			if card in unobservedCards.deck:
				# Remove the observed card from the unobserved deck.
				unobservedCards.removeCard(card)
		
		# Create a Player State Child Node and add it to the list.
		newChildNode = StateNode(False, 0, False, nDepthParam, 1, parentNodeParam, chosenCardParam, aiHandParam, None)
		stateNodeListParam.append(newChildNode)
		
		# Declaration of variable for the number of potential actions that can be taken from this state.
		# Set this equal to 2 to the power of the number of cards in the AI's hand. This will include all permutations of cards being compatible or not.
		nNumPotentialActions = 2**len(aiHandParam.cards)
		nNumActualActions = 0
		
		# Go through every potential action. Each potential action is a different combination of compatible cards.
		# For example, if the AI has two cards left, one action the player can take is to play a card that is compatible with the left card,
		# another is to play a card that is compatible with the right card, and another is to play a card that is compatible with both cards.
		# We won't consider the case where the player plays a card that is not compatible with ANY of the AI's cards here. We'll do that later.
		for i in range(1, nNumPotentialActions):
			potentialCompatibilityList = getBinaryList(i, len(aiHandParam.cards))
			###cardSubset = GameFunctions.createCardSubsetFromCompatibilityList(potentialCompatibilityList, aiHandParam)
			
			# Calculate the probability that a card that is compatible with the card subset will be played on top of the chosen card.
			nProbability = GameFunctions.calculateProbabilityThatCardAccordingToCompatibilityListWillBePlayed(unobservedCards.deck, aiHandParam, potentialCompatibilityList, chosenCardParam)
			
			# If the probability that this action can be taken is greater than 0...
			if nProbability > 0:
				nNumActualActions += 1
				# Pick a random card to play.
				listOfCardsThatCouldBePlayed = GameFunctions.getListOfCompatibleCardsAccordingToCompatibilityList(unobservedCards.deck, aiHandParam, potentialCompatibilityList, chosenCardParam)
				newChosenCard = random.choice(listOfCardsThatCouldBePlayed)
				# Add that card to the aiObservedCardsModel.
				newAIObservedCardsModel = aiObservedCardsModelParam.copy()
				newAIObservedCardsModel.append(newChosenCard)
				
				# Call the function to create an AI State Child Node and add it to the list.
				createAIStateChildNode(stateNodeListParam, nDepthParam + 1, nProbability, newAIObservedCardsModel, newChosenCard, newChildNode, aiHandParam, potentialCompatibilityList)
		
		# If there were no cards that the player could play that would be compatible with the ones in the AI's hand...
		if nNumActualActions == 0:
			# Call the function to create an AI State Child where all cards are incompatible.
			# Note that we only do this if there are no other child nodes created.
			createAIStateChildNode(stateNodeListParam, nDepthParam + 1, 1, aiObservedCardsModelParam, chosenCardParam, newChildNode, aiHandParam, getBinaryList(0, len(aiHandParam.cards)))
			
		
	# Else, the AI had no compatible cards to play...
	else:
		# Create a "DRAW_CARD" Terminal State Node and add it to the list.
		stateNodeListParam.append(StateNode(False, 2, False, nDepthParam, 1, parentNodeParam, chosenCardParam, aiHandParam, None))
	
	return stateNodeListParam

# Function to create an AI State Child Node. It will also create any child Player nodes for that node if needed.
def createAIStateChildNode(stateNodeListParam, nDepthParam, nProbabilityParam, aiObservedCardsModelParam, chosenCardParam, parentNodeParam, aiHandParam, compatibilityListParam):
	# Create the AI State Child Node and add it to the list.
	newChildNode = StateNode(False, 0, True, nDepthParam, nProbabilityParam, parentNodeParam, chosenCardParam, aiHandParam, compatibilityListParam)
	stateNodeListParam.append(newChildNode)
	
	# Declaration of boolean variable.
	bAllCardsIncompatible = True
	# Go through the compatibility list.
	for i in range(0, len(compatibilityListParam)):
		# If the current element is a 1...
		if compatibilityListParam[i] == 1:
			# Then there is at least one compatible card in the AI's hand.
			bAllCardsIncompatible = False
	
	# If there are no compatible cards in the hand...
	if bAllCardsIncompatible == True:
		# Call the function to create a Player State Child Node and add it to the list.
		# This will be a "DRAW_CARD" Terminal State Node.
		createPlayerStateChildNode(stateNodeListParam, False, nDepthParam + 1, aiObservedCardsModelParam, chosenCardParam, newChildNode, aiHandParam)
	# Else, there is at least one compatible card in the hand...
	else:
		# Go through the compatibility list. This is how we'll create the child nodes for this current node.
		for i in range(0, len(compatibilityListParam)):
			# If the current element is a 1, then we will create a new Player State Child Node.
			if compatibilityListParam[i] == 1:
				# Declaration of variables for a new hand, which will have the chosen card removed.
				tempCards = aiHandParam.cards.copy()
				newAIHand = CardClasses.Hand(tempCards)
				# Remove the chosen card.
				newAIHand.removeCard(aiHandParam.cards[i])
				
				# Call the function to create a Player State Child Node and add it to the list.
				createPlayerStateChildNode(stateNodeListParam, True, nDepthParam + 1, aiObservedCardsModelParam, aiHandParam.cards[i], newChildNode, newAIHand)
	
	return stateNodeListParam

# Function to get which card needs to be played first to reach the terminal state. This can be found in the child of the root node.
# Param: bestTerminalStateParam	The best terminal state.
def getBestCardToPlayForTerminalState(bestTerminalStateParam):
	# Declaration of variable to traverse through the nodes.
	currentNode = bestTerminalStateParam
	# While loop to traverse through the node's parent nodes.
	while True:
		# If the current node's parent node is NOT the root node...
		if currentNode.parentNode.bIsRootNode == False:
			# Update the current node.
			currentNode = currentNode.parentNode
		# Else, the current node's parent node IS the root node...
		else:
			# Get the top card of the child of the root.
			return currentNode.topCard

# Function to display debug information about the AI's decisions.
def displayDebugInformation(nLargestProbabilityParam, aiHandParam, topCardParam, bFoundWinningState, terminalStateListParam, bestPlayingCardParam, bestTerminalStateParam):
	# Convert the best probability to a percentage.
	nBestPercentage = nLargestProbabilityParam * 100
	# Print out some information about the AI's decision.
	print("\n")
	print("DEBUG: Here was the AI's hand of cards: ")
	print(aiHandParam)
	print("DEBUG: The top card was " + str(topCardParam) + ".\n")
	# If a winning state was found...
	if bFoundWinningState == True:
		print("DEBUG: The AI found " + str(len(terminalStateListParam)) + " ways to win the game.")
		print("DEBUG: The most likely way to win has a probability of approximately " + str(decimal.Decimal(nBestPercentage)) + " %.")
	# Else, there was no winning state found, and the AI is just trying to get rid of as many of its cards as it can.
	else:
		print("DEBUG: The AI couldn't find any ways to win the game with the current deck. But it found " + str(len(terminalStateListParam)) + " ways to get rid of as many of its cards as possible.")
		print("DEBUG: The most likely way to get rid of " + str(bestTerminalStateParam.nDepth // 2) + " of its cards has a probability of approximately " + str(decimal.Decimal(nBestPercentage)) + " %.")
	print("DEBUG: Here is how:\n")
	print("DEBUG: It starts by playing " + str(bestPlayingCardParam) + ".")
	# Go through all the Player parent nodes leading to this terminal state.
	for stopAtDepth in range(1, bestTerminalStateParam.nDepth):
		currentNode = bestTerminalStateParam
		# While loop to traverse through the node's parent nodes.
		while True:
			# If the current node is not at the desired depth...
			if currentNode.nDepth != stopAtDepth:
				# Update the current node.
				currentNode = currentNode.parentNode
			# Else, the current node has reached the desired depth.
			else:
				# If the stopping point is odd...
				if stopAtDepth % 2 != 0:
					print("DEBUG: If the AI plays " + str(currentNode.topCard) + "...")
				# Else, the stopping point is even...
				else:
					sAllCardsString = ""
					for card in currentNode.currentHand.cards:
						sAllCardsString += str(card) + ", "
					# Remove the last two characters of the string (because it's ", ")
					sAllCardsString = sAllCardsString[:-2]
					print("DEBUG: Then they will be left with: [" + sAllCardsString + "]")
					sCompatibleCardsString = ""
					for i in range(0, len(currentNode.compatibilityList)):
						# If the current element is a 1, then that means that the corresponding card is compatible.
						if currentNode.compatibilityList[i] == 1:
							sCompatibleCardsString += str(currentNode.currentHand.cards[i]) + ", "
					# Remove the last two characters of the string (because it's ", ")
					sCompatibleCardsString = sCompatibleCardsString[:-2]
					print("DEBUG: There is an approximately " + str(currentNode.nProbability * 100) + " % chance that a card will be played that is compatible with: [" + sCompatibleCardsString + "]")
					print("DEBUG: For example, let's say that a " + str(currentNode.topCard) + " was played...")
				break
	# If a winning state was found...
	if bFoundWinningState == True:
		print("DEBUG: That is the last card. If they play it, they win!")
	# Else, there was no winning state found, and the AI is just trying to get rid of as many of its cards as it can.
	else:
		print("DEBUG: That is the last card that the AI can play. They will be left with " + str(len(aiHandParam.cards) - (bestTerminalStateParam.nDepth // 2)) + " card(s).")
	print("\n")
	

# Function for the AI to begin the adversary search.
# Param: aiObservedCardsModelParam	The AI's model of observed cards.
# Param: topCardParam				The top card of the pile.
# Param: aiHandParam				The AI's hand of cards.
# Param: bDebugModeOnParam			Boolean for if DEBUG mode is on.
def beginAdversarySearch(aiObservedCardsModelParam, topCardParam, aiHandParam, bDebugModeOnParam):
	# Declaration of variable for the compatibility list.
	compatibilityList = []
	# Go through all the cards in the AI's hand.
	for card in aiHandParam.cards:
		# If the current card is compatible with the top card...
		if GameFunctions.isCardCompatible(topCardParam, card):
			compatibilityList.append(1)
		# Else, it is NOT compatible with the top card...
		else:
			compatibilityList.append(0)
	
	# Declaration of variable for the list of state nodes.
	stateNodeList = []
	# Create the root node and add it to the list.
	rootAIStateNode = StateNode(True, 0, True, 0, 1, None, topCardParam, aiHandParam, compatibilityList)
	stateNodeList.append(rootAIStateNode)
	
	# Go through the compatibility list. This is how we'll create the child nodes for our root node.
	for i in range(0, len(compatibilityList)):
		# If the current element is a 1, then we will create a new Player State Child Node.
		if compatibilityList[i] == 1:
			# Declaration of variables for a new hand, which will have the chosen card removed.
			tempCards = aiHandParam.cards.copy()
			newAIHand = CardClasses.Hand(tempCards)
			# Remove the chosen card.
			newAIHand.removeCard(aiHandParam.cards[i])
			
			# Call the function to create a Player State Child Node and add it to the list.
			createPlayerStateChildNode(stateNodeList, True, 1, aiObservedCardsModelParam, aiHandParam.cards[i], rootAIStateNode, newAIHand)
	
	
	# Once we are done, we'll go through all of our nodes and find the best value.
	
	# First, we'll have to get all of the winner states.
	winnerStateList = []
	# Go through each state node.
	for node in stateNodeList:
		# If the current node is a WINNER Terminal State...
		if node.nTerminalStateType == 1:
			# Add it to the winner state list.
			winnerStateList.append(node)
	
	# If there is at least one WINNER Terminal State...
	if len(winnerStateList) > 0:
		# Inside each AI node is a probability value of how likely it is to reach that state directly from the parent node.
		# We want to calculate the actual probability it takes to reach the terminal state from the top.
		# We will do this by multiplying all the probabilities on the path to the winner state.
		# Declare a list variable for it.
		winnerActualProbabilities = []
		
		# Go through all the winner state nodes.
		for node in winnerStateList:
			nActualProbability = 1
			currentNode = node
			# While loop to traverse through the node's parent nodes.
			while True:
				# If the current node's parent node is NOT the root node...
				if currentNode.parentNode.bIsRootNode == False:
					# Multiply the probability by the parent's probability.
					nActualProbability = nActualProbability * currentNode.parentNode.nProbability
					# Update the current node.
					currentNode = currentNode.parentNode
				# Else, the current node's parent node IS the root node...
				else:
					# The probability has been calculated, so append it to the list.
					winnerActualProbabilities.append(nActualProbability)
					# Break out of the loop.
					break
		# Now that all the probabilities have been calculated, let's pick the biggest one!
		nTempLargest = 0
		nLargestProbabilityIndex = 0
		# Go through all the winner actual probabilities.
		for i in range(0, len(winnerActualProbabilities)):
			# If the current probability is larger than the temporary one...
			if winnerActualProbabilities[i] > nTempLargest:
				# Set the largest probability and its index.
				nTempLargest = winnerActualProbabilities[i]
				nLargestProbabilityIndex = i
		
		# Save the best winning state in a variable.
		bestWinningState = winnerStateList[nLargestProbabilityIndex]
		
		# We have the best state. Now, let's find out which card needs to be played first to reach this state!
		bestPlayingCard = getBestCardToPlayForTerminalState(bestWinningState)
		
		# If DEBUG mode is on, then we'll print some information on what the AI is doing.
		if bDebugModeOnParam == True:
			# Display DEBUG information about the AI's decision.
			displayDebugInformation(nTempLargest, aiHandParam, topCardParam, True, winnerStateList, bestPlayingCard, bestWinningState)
		
		return bestPlayingCard
	# Else, there is no probability of a winner state.
	else:
		# The next best thing is the deepest "DRAW_CARD" state.
		# First, we'll get the depth of the tree.
		nDeepestDepth = 0
		for node in stateNodeList:
			# If the current node's depth is greater than our depth variable...
			if node.nDepth > nDeepestDepth:
				nDeepestDepth = node.nDepth
		
		# Next, we'll have to get all of the DRAW_CARD states at that depth.
		deepestDrawCardStateList = []
		# Go through each state node.
		for node in stateNodeList:
			# If the current node is a DRAW_CARD Terminal State at the deepest depth...
			if node.nTerminalStateType == 2 and node.nDepth == nDeepestDepth:
				# Add it to the DRAW_CARD state list.
				deepestDrawCardStateList.append(node)
		
		# Inside each AI node is a probability value of how likely it is to reach that state directly from the parent node.
		# We want to calculate the actual probability it takes to reach the terminal state from the top.
		# We will do this by multiplying all the probabilities on the path to the DRAW_CARD state.
		# Declare a list variable for it.
		drawCardActualProbabilities = []
		
		# Go through all the DRAW_CARD nodes at the deepest depth.
		for node in deepestDrawCardStateList:
			nActualProbability = 1
			currentNode = node
			# While loop to traverse through the node's parent nodes.
			while True:
				# If the current node's parent node is NOT the root node...
				if currentNode.parentNode.bIsRootNode == False:
					# Multiply the probability by the parent's probability.
					nActualProbability = nActualProbability * currentNode.parentNode.nProbability
					# Update the current node.
					currentNode = currentNode.parentNode
				# Else, the current node's parent node IS the root node...
				else:
					# The probability has been calculated, so append it to the list.
					drawCardActualProbabilities.append(nActualProbability)
					# Break out of the loop.
					break
		# Now that all the probabilities have been calculated, let's pick the biggest one!
		# We want the biggest one because that means it is the highest chance that the AI will get rid of as many of its cards as possible.
		nTempLargest = 0
		nLargestProbabilityIndex = 0
		# Go through all the DRAW_CARD actual probabilities.
		for i in range(0, len(drawCardActualProbabilities)):
			# If the current probability is larger than the temporary one...
			if drawCardActualProbabilities[i] > nTempLargest:
				# Set the largest probability and its index.
				nTempLargest = drawCardActualProbabilities[i]
				nLargestProbabilityIndex = i
		
		# Save the best DRAW_CARD state in a variable.
		bestDrawCardState = deepestDrawCardStateList[nLargestProbabilityIndex]
		
		# We have the best state. Now let's find out which card needs to be played first to reach this state!
		bestPlayingCard = getBestCardToPlayForTerminalState(bestDrawCardState)
		
		# If DEBUG mode is on, then we'll print some information on what the AI is doing.
		if bDebugModeOnParam == True:
			# Display DEBUG information about the AI's decision.
			displayDebugInformation(nTempLargest, aiHandParam, topCardParam, False, deepestDrawCardStateList, bestPlayingCard, bestDrawCardState)
		
		return bestPlayingCard

# Function to do the AI's turn.
# Param: aiNameParam				The AI's name.
# Param: topCardParam				The top card of the pile.
# Param: aiHandParam				The AI's hand of cards.
# Param: gameDeckParam				The game deck.
# Param: aiObservedCardsModelParam	The AI's model of observed cards.
# Param: bDebugModeOnParam			Boolean for if DEBUG mode is on.
def doAITurn(aiNameParam, topCardParam, aiHandParam, gameDeckParam, aiObservedCardsModelParam, bDebugModeOnParam):
	while True:
		# If the AI can't play any of the cards in their hand...
		if GameFunctions.doesHandHaveCompatibleCard(topCardParam, aiHandParam) == False:
			# If there are no cards left in the deck...
			if gameDeckParam.isDeckEmpty() == True:
				print(aiNameParam + " cannot make a move. Skipping " + aiNameParam + "'s turn.")
				# The AI's turn is over. Return the top card, the AI's hand, and the game deck, which have all been affected.
				return (topCardParam, aiHandParam, gameDeckParam, aiObservedCardsModelParam)
			# Else, the deck isn't empty...
			else:
				# Draw one card from the deck and add it to the AI's hand.
				drewCard = gameDeckParam.drawCard()
				aiHandParam.pickUpCard(drewCard)
				# Add the drawn card to the AI's observed card model.
				aiObservedCardsModelParam.append(drewCard)
				# Display on screen that a card was drawn.
				print(aiNameParam + " drew a card.")
		# Else, there is a compatible card in the hand...
		else:
			# Declaration of variable for the compatible cards in the hand.
			compatibleCardsList = GameFunctions.getCompatibleCardsList(topCardParam, aiHandParam)
			# If there is only one compatible card in the hand...
			if len(compatibleCardsList) == 1 or len(aiHandParam.cards) >= 7:
				# Set the new top card.
				topCardParam = compatibleCardsList[0]
				# Remove the played card from the AI's hand.
				aiHandParam.removeCard(compatibleCardsList[0])
				# Display the new top card.
				print("The top card is now " + str(topCardParam) + ".\n")
				
				# If DEBUG mode is on, then we'll print some information about what the AI is doing.
				if bDebugModeOnParam == True and len(aiHandParam.cards) < 6:
					print("DEBUG: The AI only had one compatible card. No adversary search here!\n")
				elif bDebugModeOnParam == True and len(aiHandParam.cards) >= 6:
					print("DEBUG: The AI has too many cards to perform adversary search.")
				
				# The AI's turn is over. Return the top card, the AI's hand, and the game deck, which have all been affected.
				return (topCardParam, aiHandParam, gameDeckParam, aiObservedCardsModelParam)
			elif len(compatibleCardsList) > 1:
				# Call function to begin the adversary search! This also sets the new top card.
				topCardParam = beginAdversarySearch(aiObservedCardsModelParam, topCardParam, aiHandParam, bDebugModeOnParam)
				
				# Remove the played card from the AI's hand.
				aiHandParam.removeCard(topCardParam)
				# Display the new top card.
				print("The top card is now " + str(topCardParam) + ".\n")
				# The AI's turn is over. Return the top card, the AI's hand, and the game deck, which have all been affected.
				return (topCardParam, aiHandParam, gameDeckParam, aiObservedCardsModelParam)