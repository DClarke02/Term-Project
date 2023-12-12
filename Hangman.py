import random

class HangmanGame:
    def __init__(self):
        self.words = ["worcestershire", "bluecoLab", "pandas", "Sequences", "Numpy",
                      "computer", "python", "program", "function", "classes",
                      "inheritance", "accumulation", "syntax", "software", "looping",
                      "coding", "pleasantville", "pace", "sidenburg", "leanne"]
        self.word_to_guess = ""
        self.guessed_letters = []
        self.attempts = 6

    def choose_word(self):
        self.word_to_guess = random.choice(self.words)

    def display_word(self):
        display = ""
        for letter in self.word_to_guess:
            if letter in self.guessed_letters:
                display += letter
            else:
                display += "_"
        return display

    def display_hangman(self):
        hangman_parts = [
            "  -----  \n |     | \n       | \n       | \n       | \n       | \n",
            "  -----  \n |     | \n O     | \n       | \n       | \n       | \n",
            "  -----  \n |     | \n O     | \n |     | \n       | \n       | \n",
            "  -----  \n |     | \n O     | \n/|     | \n       | \n       | \n",
            "  -----  \n |     | \n O     | \n/|\\    | \n       | \n       | \n",
            "  -----  \n |     | \n O     | \n/|\\    | \n/      | \n       | \n",
            "  -----  \n |     | \n O     | \n/|\\    | \n/ \\    | \n       | \n"
        ]

        print(hangman_parts[6 - self.attempts])

    def play(self):
        print("Welcome to Hangman!")
        print("Hangman Rules:")
        print("1. You have to guess a word.")
        print("2. You can guess one letter at a time or the entire word.")
        print("3. You have 6 attempts to guess the word.")
        print("4. The hangman figure will be displayed as you make incorrect guesses.")
        print("5. If the hangman figure is completed before you guess the word, you lose.")
        print("6. Good luck!\n")

        play_again = 'yes'

        while play_again == 'yes':
            self.choose_word()
            self.guessed_letters = []
            self.attempts = 6

            while self.attempts > 0:
                print("\nAttempts left:", self.attempts)
                self.display_hangman()
                current_display = self.display_word()
                print("Current Word:", current_display)

                guess = input("Enter a letter or guess the word: ").lower()

                if guess.isalpha() and len(guess) == 1:
                    if guess in self.guessed_letters:
                        print("You already guessed that letter. Try again.")
                        continue

                    self.guessed_letters.append(guess)

                    if guess not in self.word_to_guess:
                        self.attempts -= 1
                        print("Incorrect guess!")
                elif guess.isalpha() and len(guess) > 1:
                    if guess == self.word_to_guess:
                        print("Congratulations! You guessed the word:", self.word_to_guess)
                        break
                    else:
                        self.attempts -= 1
                        print("Incorrect guess! The word is not", guess)
                else:
                    print("Invalid input. Please enter a single letter or guess the entire word.")
                    continue

                if "_" not in self.display_word():
                    print("Congratulations! You guessed the word:", self.word_to_guess)
                    break

            if self.attempts == 0:
                print("Yikes!, you ran out of attempts. The word was:", self.word_to_guess)

            play_again = input("Do you want to play again? (yes/no): ").lower()


if __name__ == "__main__":
    hangman_game = HangmanGame()
    hangman_game.play()
