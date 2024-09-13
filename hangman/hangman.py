import random

#Pool of words to be used for the game
WORDBANK = ["JAZZ", "BUZZ", "HARRY POTTER", "WAYNE VALLEY", "SQUASH"]

#ascii art for hangman
HANG0 = """
     ____
    |    |
    |    |
    |    
    |   
    |    
    |
____|______

"""
HANG1 = """
     ____
    |    |
    |    |
    |    0
    |
    |
    |
____|_______

"""
HANG2 = """
     ____
    |    |
    |    |
    |    0
    |    |
    |    |
    |
____|_______

"""
HANG3 = """
     ____
    |    |
    |    |
    |    0
    |   /|
    |    |
    |
____|_______

"""
HANG4 = """
     ____
    |    |
    |    |
    |    0
    |   /|\\
    |    |
    |
____|______

"""
HANG5 = """
     ____
    |    |
    |    |
    |    0
    |   /|\\
    |    |
    |     \\
____|________

"""

HANG6 = """
     ____
    |    |
    |    |
    |    0
    |   /|\\
    |    |
    |   / \\
____|_______

"""
HANG = [HANG0, HANG1, HANG2, HANG3, HANG4, HANG5, HANG6]

def clear():
    print("\n" * 100) #clears screen

#main game loop
def play_round():
    word = random.choice(WORDBANK) #picks random word from WORDBANK
    incorrect = []
    word_len = len(word)
    i = 0
    strike = 0
    blank_str = ""
    reprompt = False
    while i < word_len:
        if word[i] != ' ':
            blank_str += "_"
        else:
            blank_str += ' '
        i += 1
    while '_' in blank_str:
        clear()
        if reprompt:
            print("Bad input, try again")
        reprompt = False
        print(HANG[strike])
        print(blank_str)
        print("\nIncorrect guesses: ", incorrect)
        guess = input("\nYour guess: ")
        if (len(guess) != 1) or not(guess.isalpha()):
            #reprompt
            reprompt = True
        else:
            guess = guess.upper()
            j = 0
            in_word = False
            while j < word_len:
                if guess == word[j]:
                    in_word = True
                    s = list(blank_str)
                    s[j] = guess
                    blank_str = "".join(s);
                j += 1
            if not in_word and not (guess in incorrect):
                strike += 1
                incorrect.append(guess)
                if strike > 5:
                    clear()
                    print("YOU LOSE")
                    print(HANG6)
                    print(word, '\n')
                    input("Press Enter to continue")
                    return
    clear()
    print("YOU WIN!")
    print(HANG[strike])
    print(blank_str)
    input("\nPress Enter to continue")
    return
                    
#menu loop
while 1:
    clear()
    choice = input("""H A N G M A N

1. New Game
2. How To Play
3. Exit
Your option: """)
    if choice == '1':
        play_round()
    elif choice == '2':
        clear()
        print("""HOW TO PLAY:

You will be prompted with an empty string
Guess one letter at a time for what you think the word might be
For every Incorrect guess, a body part is added to the hangman
If the entire body is completed, you lose
Guess the entire word to win
""")
        input("Press Enter to go back")
    elif choice == '3':
        exit()
    else:
        clear()
        print("Bad input, choose an option")


