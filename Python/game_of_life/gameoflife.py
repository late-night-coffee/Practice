from random import randrange


def dead_state(width, height):
    board = [[0] * height for i in range(width)]

    for h in range(height):
        for w in range(width):
            print(board[w][h], end="")
        print()

    return board


def random_state(width, height):
    board = [[randrange(1)] * height for i in range(width)]

    for h in range(height):
        for w in range(width):
            print(board[w][h], end="")
        print()


dead_state(5, 5)

random_state(5, 5)
