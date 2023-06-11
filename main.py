import random

class cows_and_bulls:
    def __init__(self):
        self.secret = ""
        self.guess = ""
        self.guess_history = []
        self.result_history = []
        self.bull_count = 0
        self.cow_count = 0
        self.playGame
        self.makeGuess
        self.checkGuess

    def getSecret(self, j: int=4):
        """Generates a unique 4 digit secret for the game. No one digit can be the same as the other 3

        Args:
            j (int, optional): Length of the unique secret. Defaults to 4 (classic game).
        """

        # Check if the user is requesting a game with a length that is too long
        if j > 9:
            print("Can't play a game with that length. Clamping the length to 9")
            j = 9

        # Check that the length is valid
        if j <= 0:
            print("Invalid length. Defaulting back to a length of 4")
            j = 4
        
        # Generate the secret
        while len(self.secret) < j:
            secret_array = [self.secret[i] for i in range(len(self.secret))]
            random_digit = random.choices("0123456789", k=1)[0]

            if random_digit not in secret_array:
                self.secret += random_digit
        print(f"[DEBUG] Secret is {self.secret}")

    def makeGuess(self):
        # Ask the user for a guess, but keep asking until the user gives a valid request or quits
        invalidGuess=True
        while invalidGuess:
            self.guess = input(f"Give a {len(self.secret)} digit guess or (q) to quit:\n")
            if self.guess == "q":
                invalidGuess=False
                break
            else:
                if len(self.guess)!=len(self.secret):
                    print("Invalid length. Try again \n")
                else:
                    invalidGuess = False
                    # print(f"Your guess is {self.guess}")
                
            
        
        
        # split the array into bite sized chunks
        guess_arrray = [self.guess[i] for i in range(len(self.guess))]
        self.guess_history.append(self.guess)

    def checkGuess(self):
        # Fetch latest guess
        latest_guess = self.guess_history[-1]
        self.bull_count = 0
        self.cow_count = 0

        for i in range(len(self.secret)):
            # Check cow
            if latest_guess[i] in self.secret and  i != self.secret.index(latest_guess[i]):
                self.cow_count += 1

            # Check bull
            if latest_guess[i] == self.secret[i]:
                self.bull_count += 1

        result = f"{self.bull_count}B{self.cow_count}C"
        self.result_history.append(result)

    def playGame(self):
        self.getSecret()

        while self.bull_count != len(self.secret):
            game.makeGuess()
            if self.guess == "q":
                print("Quitters == Losers")
                break
            game.checkGuess()

            print("|--------------------------|")
            print("| ==== BULLS AND COWS ==== |")
            print("|--------------------------|")
            print("|   Guess   |    Result    |")
            for i in range(len(self.guess_history)):
                print(f"|   {self.guess_history[i]}    |     {self.result_history[i]}     |")
        
        print(" !!!!!!! YOU WON !!!!!!!!")




# Run this code if this is run as a script and not imported as a module
if __name__ == "__main__":
    game = cows_and_bulls()
    game.playGame()