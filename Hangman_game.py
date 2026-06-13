import random
def play_hangman():
    words=["python","developer","internship","software","codealpha","programming","Kanpur","institute","technology","game"]
    target=random.choice(words)

    guessed_letters = set()

    incorrect_guesses_left = 6

    print("=== Welcome to CodeAlpha Hangman Game ===")
    print("Try to guess the secret word, one letter at a time. ")

    #Basic console input/output loop
    while incorrect_guesses_left >0:
        displayed_word=[letter if letter in guessed_letters else "_" for letter in target]
        print(f"\nWord : {' '.join(displayed_word)}")
        print(f"Incorrect guesses remaining :{incorrect_guesses_left}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

        #if player won
        if "_" not in displayed_word:
            print(f"\nCongratulations! You guessed the word: {target.upper()}")
            break

        #get player input
        guess = input("Guess a letter: ").lower().strip()
        if len(guess) != 1 or not guess.isalpha():
            print("please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue
        
        #process
        guessed_letters.add(guess)

        if guess in target:
            print(f"Good job! '{guess}' is in the word.")
        else:
            print(f"sorry, '{guess}' is not in the word.")
            incorrect_guesses_left -= 1

    if incorrect_guesses_left == 0:
        print("\nGame Over!")
        print(f"The correct word was: {target.upper()}")

if __name__ == "__main__":
    play_hangman() 
