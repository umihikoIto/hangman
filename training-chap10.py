class Hangman:
    def __init__(self, word):
        self.word = word
        self.wordList = list(word)
        self.stage = [
                      "--------",
                      "|   |   ",
                      "|   o   ",
                      "|  /|\  ",
                      "|  / \  ",
                      "|       "]
        self.wrong = 0
        self.hint = ["_"] * len(self.word)
        self.status = "continue"


    def debug(self):
        print("")
        print("======= Debug =======")
        print("self.word : ", self.word)
        print("self.wordList : ", self.wordList)
        print("self.worng : ", self.wrong)
        print("self.status : ", self.status)
        print("======= Debug =======")
        print("")


    def start(self):
        print("")
        print("Created by Umihiko Ito in 2018/11/3.")
        print("Refered self-taught programer.")
        print("\n".join(self.stage))
        print(" HANGMAN")
        print("")



    def getOneCharacter(self, inputCharacter):
        characterIndex = self.wordList.index(inputCharacter)
        self.hint[characterIndex] = self.wordList[characterIndex]
        self.wordList[characterIndex] = "$"



    def getOneWrong(self):
        self.wrong += 1


    def checkStatus(self):
        if self.wrong == len(self.stage) - 1:
            self.status = "lose"
            print("")
            print("You lose!")
            print("\n".join(self.stage))
        elif "_" not in self.hint:
            self.status = "win"
            print("")
            print("You win!")
        elif "_" in self.hint:
            self.status = "continue"
        else:
            print("Something I didn't expect is happening.")


    def game(self):
        stageDummy = self.stage[0: self.wrong]
        print("")
        print("=========")
        print("\n".join(stageDummy))
        print("=========")
        print("")
        print("Hint : ", self.hint)

        inputCharacter = input("Input a character. : ")
        if inputCharacter in self.wordList:
            self.getOneCharacter(inputCharacter)
        else:
            self.getOneWrong()
        self.checkStatus()



    def hangman(self):
        self.start()
      #  self.debug()
        while self.status == "continue":
            self.game()
          #  self.debug()
        print("The answer is " + self.word)
        print("Thank you for enjoying it!")
        print("")



if __name__ == "__main__":
    print("")
    word = input("Input keyword and start hangman! : ")
    h = Hangman(word)
    h.hangman()

