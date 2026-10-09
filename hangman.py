import random

words = ["apple", "school", "python", "computer", "college"]

print("Welcome to Hangman!")

while True:
    word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0

    print("\nGuess the word one letter at a time.")

    while wrong_guesses < 6:
        display = ""

        for letter in word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "

        print("\nWord:", display)
        print("Incorrect guesses left:", 6 - wrong_guesses)

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one letter!")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")
        else:
            wrong_guesses += 1
            print("Wrong guess!")

        if all(letter in guessed_letters for letter in word):
            print("You Win!")
            break
    else:
        print("Game Over!")
        print("The word was:", word)

    again = input("Play again? (yes/no): ").lower()

    if again != "yes":
        print("Thanks for playing!")
        break