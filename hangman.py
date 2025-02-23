import random

def choose_random_word(word_list):
    return random.choice(word_list)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word_list = ["python", "hangman", "programming", "artificial", "intelligence"]
    chosen_word = choose_random_word(word_list)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print("Try to guess the word, one letter at a time.")
    print("You have", max_incorrect_guesses, "incorrect guesses allowed.")

    while incorrect_guesses < max_incorrect_guesses:
        print("\nWord:", display_word(chosen_word, guessed_letters))
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try a different one.")
            continue

        guessed_letters.add(guess)

        if guess in chosen_word:
            print("Good guess!")
        else:
            incorrect_guesses += 1
            print(f"Wrong guess! You have {max_incorrect_guesses - incorrect_guesses} guesses left.")

        if all(letter in guessed_letters for letter in chosen_word):
            print("\nCongratulations! You guessed the word:", chosen_word)
            break
    else:
        print("\nGame over! The word was:", chosen_word)

if __name__ == "__main__":
    hangman()
