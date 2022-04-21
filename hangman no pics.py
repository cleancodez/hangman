import random
import time

word_list = [
"abruptly", 
"absurd", 
"abyss", 
"affix", 
"askew", 
"avenue", 
"awkward",
"axiom",
"azure",
"bagpipes",
"bandwagon",
"banjo",
"bayou",
"beekeeper",
"bikini",
"blitz",
"blizzard",
"boggle",
"bookworm",
"boxcar",
"boxful",
"buckaroo",
"buffalo",
"buffoon",
"buxom",
"buzzard",
"buzzing",
"buzzwords",
"caliph",
"cobweb",
"cockiness",
"croquet",
"crypt",
"curacao",
"cycle",
"daiquiri",
"dirndl",
"disavow",
"dizzying",
"duplex",
"dwarves",
"embezzle",
"equip",
"espionage",
"euouae",
"exodus",
"faking",
"fishhook",
"fixable",
"fjord",
"flapjack",
"flopping",
"fluffiness",
"flyby",
"foxglove",
"frazzled",
"frizzled",
"fuchsia",
"funny",
"gabby",
"galaxy",
"galvanize",
"gazebo",
"giaour",
"gizmo",
"glyph",
"gnarly",
"gnostic",
"gossip",
"grogginess",
"haiku",
"haphazard",
"hyphen",
"iatrogenic",
"icebox",
"injury",
"ivory",
"jackpot",
"jaundice",
"jawbreaker",
"jaywalk",
"jazziest",
"jazzy",
"jelly",
"jigsaw",
"jinx",
"jiujitsu",
"jockey",
"jogging",
"joking",
"jovial",
"joyful",
"juicy",
"jukebox",
"jumbo",
"kayak",
"kazoo",
"keyhole",
"khaki",
"kilobyte",
"kiosk",
"kitsch",
"kiwifruit",
"klutz",
"knapsack",
"larynx",
"lengths",
"lucky",
"luxury",
"lymph",
"marquis",
"matrix",
"megahertz",
"microwave",
"mnemonic",
"mystify",
"naphtha",
"nightclub",
"nowadays",
"numbskull",
"nymph",
"onyx",
"ovary",
"oxidize",
"oxygen",
"pajama",
"peekaboo",
"phlegm",
"pixel",
"pizazz",
"pneumonia",
"polka",
"pshaw",
"psyche",
"puppy",
"puzzling",
"quartz",
"queue",
"quips",
"quixotic",
"quiz",
"quizzes",
"quorum",
"razzmatazz",
"rhubarb",
"rhythm",
"rickshaw",
"schnapps",
"scratch",
"shiv",
"snazzy",
"sphinx",
"spritz",
"squawk",
"staff",
"strength",
"strengths",
"stretch",
"stronghold",
"stymied",
"subway",
"swivel",
"syndrome",
"thriftless",
"thumbscrew",
"titties",
"topaz",
"transcript",
"transgress",
"transplant",
"triphthong",
"twelfth",
"twelfths",
"unknown",
"unworthy",
"unzip",
"uptown",
"vaporize",
"vixen",
"vodka",
"voodoo",
"vortex",
"voyeurism",
"walkway",
"waltz",
"wave",
"wavy",
"waxy",
"wellspring",
"wheezy",
"whiskey",
"whizzing",
"whomever",
"wimpy",
"witchcraft",
"wizard",
"woozy",
"wristwatch",
"wyvern",
"xylophone",
"yachtsman",
"yippee",
"yoked",
"youthful",
"yummy",
"zephyr",
"zigzag",
"zigzagging",
"zilch",
"zipper",
"zodiac",
"zombie"
]


def get_word(word_list):
    word = random.choice(word_list)
    return word.lower()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job", guess, "is a letter!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
            if "_" not in word_completion:
                guessed = True            
        elif len(guess) == len(word) and guess.isalpha():   
            if guess in guessed_words:
                print("You've already guessed this letter", guess)
            elif guess != word:
                print(guess, "is not the letter.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("Nice dude, you guessed the word! You win!")
    else:
        print("I'm sorry, you ran out of tries. The word was " + word.upper() + ". Maybe next time!")

            
def display_hangman(tries):
    stages = [  """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """
    ]
    return stages[tries]

def main():
    word = get_word(word_list)
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word(word_list)
        play(word)

if __name__ == "__main__":
    main()
            
