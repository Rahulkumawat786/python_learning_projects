#from IPython.display import clear_output
#above module is working only in jupyter notebook
def display_board(board):
    """
    this function display the tic-tac-toe board to the players
    so that they can easily fill the position
    :param board:
    :return:
    """
    #clear_output()
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-----------")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-----------")
    print(board[7] + "|" + board[8] + "|" + board[9])


def user_input(acceptable_valuse):
    """
    this function is used to take valid input from the user
    input should be integer and valid for the board
    :param acceptable_valuse:
    :return:
    """
    position = -1
    while True:
        try:
            print("Enter the position: ", end="")
            position = int(input())
            if position not in acceptable_values:
                raise IOError
        except ValueError:  #if the input is not a degit
            print("Please enter an integer!!!")
        except IOError: #if input is not valid
            print("please enter valid position!!!")
        else:
            break
    acceptable_values.remove(position)
    return (position, acceptable_valuse)


def player_choice(palyer1, player2):
    """
    this is used to take valid choices of players
    and return the choices as tuple
    :param palyer1:
    :param player2:
    :return:
    """
    available_choice = ['X', 'O']
    player1_choice = "wrong"
    player2_choice = "wrong"
    while player1_choice not in available_choice:
        player1_choice = input(f"What do you want to choose {player1} (O/X): ")
        if player1_choice not in available_choice:
            print("sorry,don't understand, please input O or X!!!")

    if player1_choice == "X":
        player2_choice = "O"
    else:
        player2_choice = "X"
    return (player1_choice, player2_choice)


def update_board(player_number, board, choices, position):
    """
    this is used to update the board after each input position
    :param player_number:
    :param board:
    :param choices:
    :param position:
    :return:
    """
    board[position] = " " + choices[player_number] + " "
    return board


def is_won(board, player_choice):
    """
    this is used to check weather any user is won or not
    if not play game continuoue else declare the winner
    :param board:
    :param player_choice:
    :return:
    """
    player_choice = " " + player_choice + " "
    board_list = [
        [board[1], board[2], board[3]],
        [board[4], board[5], board[6]],
        [board[7], board[8], board[9]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[3], board[6], board[9]],
        [board[1], board[5], board[9]],
        [board[3], board[5], board[7]],
    ]
    winning_list = [player_choice, player_choice, player_choice]

    if winning_list in board_list:
        return True
    else:
        return False



"""
from here our driver code is starting this will take names of player
and use all the function defined above to play the game
"""
if __name__ == '__main__':

    print("***************************Welcomne to tic - tac - toi game**********************************")
    player1 = input("Enter 1st player name: ")
    player2 = input("Enter 2nd player name: ")
    players = [player1, player2]
    choices = [-1, -1]
    board = ["", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
    choices[0], choices[1] = player_choice(player1, player2)
    temp = 0
    game_won = False
    i = 0
    display_board(board)
    acceptable_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while temp != 9 and game_won == False:
        i = (i + 1) % 2
        print(f"\t{players[i]}--->>")
        position, acceptable_values = user_input(acceptable_values)
        board = update_board(i, board, choices, position)
        display_board(board)
        game_won = is_won(board, choices[i])
        if game_won == True:
            print(f"congratulation {players[i]}, you have won the game:)")
        temp += 1

    if game_won == False:
        print("Game is tie!!!!")
