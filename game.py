import random

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4

# code generation


def generate_code():
    code = []

    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
    return code


# User guessing the code
def guess_code():
    # split takes all of inputs turned them into list based on space delimeter
    # "G G G G" -> ["G","G","G","G"]

    while True:
        guess = input("Guess: ").upper().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again")
                break
        else:
            break
    return guess


def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

        # guess = ["G","R"]
        # real = ["W","Y"]
        # zip gives list of tuple-> [("G","W"),("R","Y")]

    # for loop for correct color
    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1

        # ["G", "O", "O", "O"] real
        # ["G", "G", "W", "W"] guess

    # for loop for incorrect color
    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos


def game():
    print(f"Welcome to mastermid, you have ${
          TRIES} tries to guess the code...")
    print("The valid colors are", *COLORS)
    code = generate_code()
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries!")
            break
        print(f"Correct Positions:{
              correct_pos} | Incorrect Position {incorrect_pos}")
    else:
        print("You ran out of tries, the code was:", *code)

    # In Python, the * operator (often called the "splat" or "unpacking" 
    # operator) is used in differentcontexts to unpack or expand an iterable
    # (like a list, tuple, or set) into individual elements.
    # code is printed as space seperated


if __name__ == "__main__":
    game()
