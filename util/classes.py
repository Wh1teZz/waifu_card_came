import json
import random

class Card:
    def __init__(self, name, effect, rarity, totalNum, currentNum):
        self.name = name
        self.effect = effect
        self.rarity = rarity
        self.totalNum = totalNum
        self.currentNum = currentNum

class Deck:
    def __init__(self):
        self.cards = []
        self.cardsTotal = 0
        self.cardsInDeck = 0
        with open("data/current_game_data.json", "r") as f:
            data = json.load(f)
            for key in data:
                curr = Card(key, 
                    data[key]["effect"], 
                    data[key]["rarity"], 
                    data[key]["totalNum"], 
                    data[key]["currentNum"])
                self.cards.append(curr)
                self.cardsTotal += curr.totalNum
                self.cardsInDeck += curr.currentNum
            
            

    def draw(self):
        if self.cardsInDeck == 0:
            print("Tried to draw from an empty deck")
            return None

        randomCard = random.randint(0, self.cardsInDeck - 1)
        index = 0
        currCardNum = 0
        currCard = self.cards[currCardNum]
        while currCardNum < len(self.cards):
            if currCard.currentNum == 0:
                currCardNum += 1
                currCard = self.cards[currCardNum]
                continue
            
            index += currCard.currentNum
            if index > randomCard:
                break

            currCardNum += 1
            currCard = self.cards[currCardNum]
            
            
        
        if not currCard or currCard.currentNum <= 0:
            print ("I'm panicking something went wrong :( ... tried to draw card that doesn't exist")
            print ("Bailing out")
            print ("Tried to draw:", currCard.name)
            exit(1)
            
        currCard.currentNum -= 1
        self.cardsInDeck -= 1
        return currCard

    # will never be called probably unless game rules change
    def cardIsPlayed(self, cardPlayed):
        check = False
        for card in self.cards:
            if card.name == cardPlayed.name:
                if card.currentNum == card.totalNum:
                    print("Tried to play a card but deck and player hand have mismatched information")
                    exit(1)

                card.currentNum += 1
                self.cardsInDeck += 1
                check = True

        if not check:
            print("Umm, you tried to play a card not in the deck...?")
            exit(1)

    def displayDeck(self):
        print("\n")
        print("There are currently", self.cardsInDeck, "cards in the deck.")
        for card in self.cards:
            print(card.name,"|",card.rarity,"| In the deck, there are",card.currentNum,"out of",card.totalNum)
        print("\n")


class Hand:
    def __init__(self, playerName, cards, handCount, handMax):
        self.player = playerName
        self.cards = cards
        self.handCount = handCount
        self.handMax = handMax


    def play(self, index):
        if index <= 0 or index > len(self.cards):
            print("That is an invalid card number")
            return
        index -= 1
        print(self.player,"has played",self.cards[index].name)
        print("The effect is:", self.cards[index].effect)
        
        if self.cards[index].currentNum == 1:
            self.cards.pop(index)
        elif self.cards[index].currentNum > 1:
            self.cards[index].currentNum += 1
        else:
            print("Something is wrong with the data...")
            print("Tried to play a card that doesn't exist (currentNum < 1)")
            exit(1)
        
        self.handCount -= 1


    def cardIsDrawn(self, card):
        print("You have drawn: ", card.name)
        print("Effect: ", card.effect)
        print("Rarity: ", card.rarity)
        self.handCount += 1

        # if card is already in hand
        for cardInHand in self.cards:
            if card.name == cardInHand.name:
                cardInHand.currentNum += 1
                return

        # otherwise, populate a new card and append to hand
        newCard = Card(card.name, card.effect, card.rarity, card.totalNum, 1)
        self.cards.append(newCard)
        


    def displayCards(self):
        for i in range(len(self.cards)):
            copy = "copy" if self.cards[i].currentNum == 1 else "copies"
            print(i + 1, "| ", self.cards[i].name, "|", self.cards[i].currentNum, copy)
        print("\n")
    

    def inspectCard(self, index):
        if index <= 0 or index > len(self.cards):
            print("That is an invalid card number")
            return
        
        index -= 1
        print(index + 1, "| ", self.cards[index].name)
        print("Effect: ", self.cards[index].effect)
        print("Rarity: ", self.cards[index].rarity, "\n")

    
    def canDraw(self):
        if self.handCount < self.handMax:
            return True
        return False
        
# Testing


# test_deck = Deck()
# test_hand = Hand("Yukie")
# for i in range(5):
#     card = test_deck.draw()
#     test_hand.cardIsDrawn(card)

# for card in test_deck.cards:
#     print ("card name: ", card.name)
#     print ("amount in deck: ", card.currentNum)

# print("\n\n")
# print(test_hand.player)
# test_hand.displayCards()
# for i in range(1, 6):
#     test_hand.inspectCard(i)

# test_hand.play(3)
# test_hand.play(5)

# test_hand.displayCards()