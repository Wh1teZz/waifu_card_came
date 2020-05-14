from util.classes import Deck, Hand, Card
import json

class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = {}
        with open("data/current_player_data.json") as f:
            players = json.load(f)
            for playerName in players:
                # for ease of use
                currPlayer = players[playerName]
                # create instance of the hand of a new player
                currHand = Hand(playerName, 
                    [], 
                    currPlayer["handCount"],
                    currPlayer["handMax"])
                # iterate thru cards
                for card in currPlayer["cards"]:
                    # create card instance
                    currCard = Card(card, 
                        currPlayer["cards"][card]["effect"], 
                        currPlayer["cards"][card]["rarity"], 
                        currPlayer["cards"][card]["totalNum"], 
                        currPlayer["cards"][card]["currentNum"])
                    # add card to hand
                    currHand.cards.append(currCard)
                # add hand to players
                self.players[playerName] = currHand


    def _checkPlayer(self, player):
        if player in self.players:
            return True
        else:
            print("Sorry,", player, "doesn't exist")
            return False


    def saveGame(self):
        # convert players into dictionary format
        playerJson = {}
        for player in self.players:
            cardJson = {}
            for card in self.players[player].cards:
                cardJson[card.name] = {
                    "effect":card.effect,
                    "rarity":card.rarity,
                    "totalNum":card.totalNum,
                    "currentNum":card.currentNum
                }

            playerJson[player] = {
                "cards":cardJson,
                "handCount":self.players[player].handCount,
                "handMax":self.players[player].handMax
            }

        # rewrite player json file
        with open("data/current_player_data.json", "w") as f1:
            json.dump(playerJson, f1)

        # convert deck into dictionary format
        deckJson = {}
        for card in self.deck.cards:
            deckJson[card.name] = {
                "effect":card.effect,
                "rarity":card.rarity,
                "totalNum":card.totalNum,
                "currentNum":card.currentNum
            }

        # rewrite deck json file
        with open("data/current_game_data.json", "w") as f2:
            json.dump(deckJson, f2)

        print("Session has successfully saved!")


    def drawCard(self, player):
        if self._checkPlayer(player):
            card = self.deck.draw()
            if not card:
                return
            self.players[player].cardIsDrawn(card)


    def playCard(self, player, index):
        if self._checkPlayer(player):
            self.players[player].play(index)


    def inspectCard(self, player, index):
        if self._checkPlayer(player):
            self.players[player].inspectCard(index)


    def displayCards(self, player):
        if self._checkPlayer(player):
            self.players[player].displayCards()

    def displayDeck(self):
        self.deck.displayDeck()

    def showPlayers(self):
        players = ""
        for player in self.players:
            players += player
            players += "\n"
        print(players)



# driver code for testing the functions

# game = Game()
# game.displayDeck()
# game.drawCard("Yookles")
# game.drawCard("Yookles")
# game.drawCard("Yookles")
# game.displayDeck()
# game.drawCard("Hooman")
# game.drawCard("Hooman")
# game.drawCard("Hooman")
# game.displayDeck()
# game.displayCards("Yookles")
# game.displayCards("Hooman")
# game.saveGame()
