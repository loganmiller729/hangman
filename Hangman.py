import random
def hangman(word):
    wrong = 0
    stages = ["",
              "________     ",
              "|            ",
              "|      |     ",
              "|      0     ",
              "|     /|\    ",
              "|     / \    ",
              "|            "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    wletters = list()
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        print("Incorrect guesses: ")
        print (', '.join(wletters))
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters \
                   .index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong +=1
            wletters.append(char)
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: \
                                   wrong]))
        print("You lose! It was {}.".format(word))

words = ["cat", "dog", "apple", "banana", "movie", "picture", "awkward", "bagpipes",
         "banjo", "bungler", "croquet", "crypt", "dwarves", "fervid", "fishhook", "fjord",
         "gazebo", "gypsy", "haiku", "haphazard", "hypen", "ivory", "jazzy", "jiffy",
         "jinx", "jukebox", "kayak", "kiosk", "klutz", "memento", "mystify", "numbskull",
         "ostracize", "oxygen", "pajama", "phlegm", "pixel", "quad", "quip", "rhythmic",
         "rogue", "sphinx", "squawk", "swivel", "toady", "twelfth", "unzip", "waxy",
         "wildebeest", "yacht", "zealuos", "zigzag", "zippy", "zombie"]

start = input("Press any key to start, Press q to quit: ")
while(start != 'q'):
    playwords = random.choice(words)
    hangman(playwords)
    start = input("Press any key to play again, press q to quit: ")

    
