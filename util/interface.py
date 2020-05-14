from util.game import Game
import csv

class Interface:
    def __init__(self):
        self.game = Game()
        self.args = {}
        self.argsHelp = {}

        with open("data/args.csv") as f:
            reader = csv.reader(f)
            for line in reader:
                self.args[line[0]] = line

        with open("data/args_help.csv") as f:
            reader = csv.reader(f)
            for line in reader:
                self.argsHelp[line[0]] = line[1]


    def parseArgs(self, args=[]):
        if not args:
            print("I don't know how we got to this point, I'm bailing")
            exit(1)

        elif args[0] in self.args["quit"]:
            return

        elif args[0] in self.args["help"]:
            for arg in self.argsHelp:
                print(self.argsHelp[arg])

        elif args[0] in self.args["draw"]:
            try:
                playerName = args[1]
            except IndexError:
                print(self.argsHelp["draw"])
                return

            self.game.drawCard(playerName)

        elif args[0] in self.args["play"]:
            try:
                playerName = args[1]
                index = args[2]
            except IndexError:
                print(self.argsHelp["play"])
                return

            if playerName in self.game.players:
                self.game.playCard(playerName, index)
            else:
                print("Sorry, that player couldn't be found. Here's a list:")
                self.game.showPlayers()
    
        elif args[0] in self.args["inspecthand"]:
            try:
                playerName = args[1]
            except IndexError:
                print(self.argsHelp["inspecthand"])
                return

            if playerName in self.game.players:
                self.game.displayCards(playerName)
            else:
                print("Sorry, that player couldn't be found. Here's a list:")
                self.game.showPlayers()

        elif args[0] in self.args["inspectdeck"]:
            self.game.displayDeck()

        elif args[0] in self.args["inspectcard"]:
            try:
                playerName = args[1]
                index = args[2]
            except IndexError:
                print(self.argsHelp["inspectcard"])
                return

            if playerName in self.game.players:
                self.game.inspectCard(playerName, index)
            else:
                print("Sorry, that player couldn't be found. Here's a list:")
                self.game.showPlayers()

        else:
            print("Sorry, that wasn't an expected command.")
            print("If you would like to see a list of commands, please enter: help")

    def runProgram(self):
        try:
            userInput = [""]
            while userInput[0] not in self.args["quit"]:
                userInput = input("8==>>> ").split()
                if not userInput:
                    continue
                self.parseArgs(userInput)
        finally:
            self.game.saveGame()

    def debugProgram(self):
        print(self.args)
        print(self.argsHelp)



 



            
