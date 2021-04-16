# main.py
# Python file for the main function.
# TJ Mendicino	101044387
# NamCao Nguyen	101046157

# Import libraries.
import CardClasses
import GameFunctions
import AI

# Main function
def main():
	# Declaration of boolean variable for DEBUG mode. If it is on, then the system will print information about the AI's decision.
	bDebugModeOn = False
	
	# Declaration of variable for the AI's name.
	sAIName = ""

	print("Welcome to this Crazy Eights game!!!")
	# Get the player's name through input.
	sPlayerName = input("What's your name? ")
	
	# If the player's name is "DEBUG"...
	if sPlayerName == "HACKER":
		# Turn on DEBUG mode.
		bDebugModeOn = True
		print("You've entered DEBUG mode. Information about the AI's decision will be displayed.")
	
	if sPlayerName != "JOHNSON":
		sAIName = "JOHNSON"
	else:
		sAIName = "JOHNSON-2.0"
	
	print("Okay! Your opponent will be " + sAIName + ".")
	
	# Declaration of variable for the deck of 52 cards.
	gameDeck = CardClasses.Deck()
	
	# Declaration of variables for the Player's and AI's hand.
	playerHand = CardClasses.Hand([])
	aiHand = CardClasses.Hand([])
	
	# Give both players 5 cards to start.
	for i in range(0,5):
		playerHand.pickUpCard(gameDeck.drawCard())
		aiHand.pickUpCard(gameDeck.drawCard())
	
	# Declaration of variable for the top card.
	topCard = gameDeck.drawCard()
	
	# Declaration of variable for who goes first.
	bPlayerGoesFirst = False
	
	while True:
		# Get who goes first through user input.
		sGoFirst = input("Do you want to go first? (y/n) ")
		
		# If the user said yes...
		if sGoFirst == "y":
			print("Okay, " + sPlayerName + " will go first.")
			bPlayerGoesFirst = True
			break
		# If the user said no...
		elif sGoFirst == "n":
			print("Okay, " + sAIName + " will go first.")
			bPlayerGoesFirst = False
			break
		# If the user said something else...
		else:
			print("Please answer either 'y' or 'n'!")
	
	# Declaration of string variable for the winner.
	sWinner = ""
	
	# Declaration of variable for the AI's model of observed cards.
	aiObservedCardsModel = []
	# Initialize the AI's observed cards model.
	aiObservedCardsModel = GameFunctions.initializeAIObservedCardsModel(topCard, aiHand)
	
	# If the Player goes first...
	if bPlayerGoesFirst == True:
		while True:
			print("\n**********It's " + sPlayerName + "'s turn!**********")
			# Do the player's turn.
			topCard, playerHand, gameDeck = GameFunctions.doPlayerTurn(topCard, playerHand, gameDeck)
			
			# Display the number of cards left in the player's hand.
			GameFunctions.displayNumberOfCardsInHand(sPlayerName, playerHand)
			
			# Check if the player has emptied their hand.
			if playerHand.isHandEmpty() == True:
				# Set the player as the winner and exit the loop.
				sWinner = sPlayerName
				break
			
			# Add the top card to the AI's model of observed cards.
			aiObservedCardsModel.append(topCard)
			
			# Check if the deck is empty.
			if gameDeck.isDeckEmpty() == True:
				# Restock the deck.
				gameDeck.restockDeck(topCard, playerHand, aiHand)
				# When the deck is restocked, the AI's model of observed cards needs to be reset as well.
				aiObservedCardsModel = GameFunctions.initializeAIObservedCardsModel(topCard, aiHand)
				
			
			print("\n**********It's " + sAIName + "'s turn!**********")
			print("Here is the top card: " + str(topCard))

			# Do the AI's turn.
			topCard, aiHand, gameDeck, aiObservedCardsModel = AI.doAITurn(sAIName, topCard, aiHand, gameDeck, aiObservedCardsModel, bDebugModeOn)
			
			# Display the number of cards left in the AI's hand.
			GameFunctions.displayNumberOfCardsInHand(sAIName, aiHand)
			
			# Check if the AI has emptied their hand.
			if aiHand.isHandEmpty() == True:
				# Set the AI as the winner and exit the loop.
				sWinner = sAIName
				break
			
			# Check if the deck is empty.
			if gameDeck.isDeckEmpty() == True:
				# Restock the deck.
				gameDeck.restockDeck(topCard, playerHand, aiHand)
				# When the deck is restocked, the AI's model of observed cards needs to be reset as well.
				aiObservedCardsModel = GameFunctions.initializeAIObservedCardsModel(topCard, aiHand)
	# Else, the AI goes first...
	else:
		while True:
			print("\n**********It's " + sAIName + "'s turn!**********")
			print("Here is the top card: " + str(topCard))
			# Do the AI's turn.
			topCard, aiHand, gameDeck, aiObservedCardsModel = AI.doAITurn(sAIName, topCard, aiHand, gameDeck, aiObservedCardsModel, bDebugModeOn)
			
			# Display the number of cards left in the AI's hand.
			GameFunctions.displayNumberOfCardsInHand(sAIName, aiHand)
			
			# Check if the AI has emptied their hand.
			if aiHand.isHandEmpty() == True:
				# Set the AI as the winner and exit the loop.
				sWinner = sAIName
				break
				
			# Check if the deck is empty.
			if gameDeck.isDeckEmpty() == True:
				# Restock the deck.
				gameDeck.restockDeck(topCard, playerHand, aiHand)
				# When the deck is restocked, the AI's model of observed cards needs to be reset as well.
				aiObservedCardsModel = GameFunctions.initializeAIObservedCardsModel(topCard, aiHand)
			
			print("\n**********It's " + sPlayerName + "'s turn!**********")
			# Do the player's turn.
			topCard, playerHand, gameDeck = GameFunctions.doPlayerTurn(topCard, playerHand, gameDeck)
			
			# Display the number of cards left in the player's hand.
			GameFunctions.displayNumberOfCardsInHand(sPlayerName, playerHand)
			
			# Check if the player has emptied their hand.
			if playerHand.isHandEmpty() == True:
				# Set the player as the winner and exit the loop.
				sWinner = sPlayerName
				break
			
			# Add the top card to the AI's model of observed cards.
			aiObservedCardsModel.append(topCard)
			
			# Check if the deck is empty.
			if gameDeck.isDeckEmpty() == True:
				# Restock the deck.
				gameDeck.restockDeck(topCard, playerHand, aiHand)
				# When the deck is restocked, the AI's model of observed cards needs to be reset as well.
				aiObservedCardsModel = GameFunctions.initializeAIObservedCardsModel(topCard, aiHand)
	
	# Display the winner of the Crazy Eights game.
	print(sWinner + " is the winner of this Crazy Eights game!!!")

# Call the main function.
main()
