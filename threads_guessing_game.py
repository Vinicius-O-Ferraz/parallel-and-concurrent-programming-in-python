import threading
import time
import random

class Guess_Game():
    def __init__(self) -> None:
        self.time_up = False
        self.attempts = 0
        self.number = random.randint(1,100)

    def timer(self):
        time.sleep(30)
        print("You didn't guessed right :( Wish you luck next time")

        self.time_up = True
        return self.time_up
    
    def guess_game(self):
        timer_thread = threading.Thread(target= Guess_Game.timer, args=(20,),daemon=True).start()

        while not self.time_up:
            n = int(input('Guess a number from 1 to 100: '))

            if n > self.number:
                print("Guess lower ")
                self.attempts += 1

            elif n < self.number :
                print("Guess higher ")
                self.attempts += 1

            else:
                print(f"Congratulations, you guessed the right number: {self.number} with {self.attempts}")

if __name__ == '__main__':
    game = Guess_Game()
    game.guess_game()

        