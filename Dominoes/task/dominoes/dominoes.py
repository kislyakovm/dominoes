import random

player_pieces = []
computer_pieces = []
domino_chain = []
stock_pieces = []
status = ''


def first_element():
    computer_domino_snake = 0
    player_domino_snake = 0
    computer_domino_snake_string = ''
    player_domino_snake_string = ''

    for i in computer_pieces:
        if i[0] == i[1]:
            computer_domino_snake_string += str(i[0])

    if computer_domino_snake_string != '':
        computer_domino_snake = int(max(computer_domino_snake_string))

    for i in player_pieces:
        if i[0] == i[1]:
            player_domino_snake_string += str(i[0])

    if player_domino_snake_string != '':
        player_domino_snake = int(max(player_domino_snake_string))

    if computer_domino_snake_string == '' and player_domino_snake_string == '':
        domino_split()
    else:
        global status
        if player_domino_snake > computer_domino_snake:
            player_pieces.remove([player_domino_snake, player_domino_snake])
            status = "computer"
            domino_chain.append([player_domino_snake, player_domino_snake])

        else:
            computer_pieces.remove([computer_domino_snake, computer_domino_snake])
            status = "player"
            domino_chain.append([computer_domino_snake, computer_domino_snake])

        print_message()


def domino_split():
    pieces = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [1, 1], [1, 2], [1, 3],
              [1, 4], [1, 5], [1, 6], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [3, 3], [3, 4],
              [3, 5], [3, 6], [4, 4], [4, 5], [4, 6], [5, 5], [5, 6], [6, 6]]

    for i in range(7):
        a = random.choice(pieces)
        player_pieces.append(a)
        pieces.remove(a)

    for i in range(7):
        a = random.choice(pieces)
        computer_pieces.append(a)
        pieces.remove(a)

    for i in range(14):
        a = random.choice(pieces)
        stock_pieces.append(a)
        pieces.remove(a)

    first_element()


def print_message():
    print('=' * 70)
    print("Stock size:", len(stock_pieces))
    print("Computer pieces:", len(computer_pieces))
    print()

    domino_chain_format()
    print()

    print("Your pieces:")
    for i in range(len(player_pieces)):
        print(f"{i + 1}:{player_pieces[i]}")
    print()


def input_message():
    a = input()

    if a == '':
        computer_moves()
    else:
        try:
            a = int(a)
        except ValueError:
            print("Invalid input. Please try again.")
            return

        if abs(a) <= len(player_pieces):
            if a == 0:
                take_extra_piece(player_pieces)
            elif a > 0:
                if player_pieces[a - 1][0] == domino_chain[len(domino_chain) - 1][1]:
                    domino_chain.append(player_pieces.pop(a - 1))
                elif player_pieces[a - 1][1] == domino_chain[len(domino_chain) - 1][1]:
                    domino_chain.append([player_pieces[a - 1][1], player_pieces[a - 1][0]])
                    player_pieces.remove(player_pieces[a - 1])
                else:
                    print('Illegal move. Please try again.')
                    input_message()
                    return
            else:
                if player_pieces[-a - 1][1] == domino_chain[0][0]:
                    domino_chain.insert(0, player_pieces.pop(-a - 1))
                elif player_pieces[-a - 1][0] == domino_chain[0][0]:
                    domino_chain.insert(0, [player_pieces[-a - 1][1], player_pieces[-a - 1][0]])
                    player_pieces.remove(player_pieces[-a - 1])
                else:
                    print('Illegal move. Please try again.')
                    input_message()
                    return
        else:
            print("Invalid input. Please try again.")
            return

    print_message()

    global status
    if status == 'player':
        status = 'computer'
    else:
        status = 'player'


def domino_chain_format():

    if len(domino_chain) > 6:
        print(''.join(str(i) for i in domino_chain[:3]) + '...' + ''.join(str(i) for i in domino_chain[-3:]))
    else:
        print(*domino_chain)


def take_extra_piece(pieces):
    if stock_pieces:
        a = random.choice(stock_pieces)
        pieces.append(a)
        stock_pieces.remove(a)


def computer_moves():
    a = random.randint(-len(computer_pieces) + 1, len(computer_pieces) - 1)

    if a == 0:
        take_extra_piece(computer_pieces)
    elif a > 0:
        if computer_pieces[a][0] == domino_chain[len(domino_chain) - 1][1]:
            domino_chain.append(computer_pieces.pop(a - 1))
        elif computer_pieces[a][1] == domino_chain[len(domino_chain) - 1][1]:
            domino_chain.append([computer_pieces[a][1], computer_pieces[a][0]])
            computer_pieces.remove(computer_pieces[a])
        else:
            computer_moves()
    else:
        if computer_pieces[-a][1] == domino_chain[0][0]:
            domino_chain.insert(0, computer_pieces.pop(-a - 1))
        elif computer_pieces[-a][0] == domino_chain[0][0]:
            domino_chain.insert(0, [computer_pieces[-a][1], computer_pieces[-a][0]])
            computer_pieces.remove(computer_pieces[-a])
        else:
            computer_moves()


def end_game():

    element_1 = domino_chain[0]
    element_2 = domino_chain[len(domino_chain) - 1]
    b = 0

    if not player_pieces:
        print('Status: The game is over. You won!')
        return False

    if not computer_pieces:
        print('Status: The game is over. The computer won!')
        return False

    if element_1[0] == element_2[1]:
        for i in domino_chain:
            if i[0] == element_1[0]:
                b += 1
            if i[1] == element_1[0]:
                b += 1
        if b >= 8:
            print("Status: The game is over. It's a draw!")
            return False

    if status != "computer":
        print("Status: Computer is about to make a move. Press Enter to continue...")
    else:
        print("Status: It's your turn to make a move. Enter your command.")
    return True


domino_split()

if status == 'player':
    status = 'computer'
else:
    status = 'player'

while end_game():
    input_message()
