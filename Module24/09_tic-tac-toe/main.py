# TODO здесь писать код
class Cell:

    def __init__(self, number):
        self.number = number

    def is_free(self):
        if self.number in taken_places:
            print(f'Cell {self.number} is not free, please choose another one.')
            return False
        else:
            taken_places.append(self.number)
            return True


class Board:
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def draw_board(self):
        print('-' * 14)
        for i in range(3):
            print(f' | {self.board[0 + i * 3]} | {self.board[1 + i * 3]} | {self.board[2 + i * 3]}|')
        print('-' * 14)


def turn(player):
    cell.number = int(input(f'{player.name} please enter the number of cell where you want to place your symbol: '))
    if cell.is_free():
        game_board.board[cell.number - 1] = player.symbol
        game_board.draw_board()
    else:
        turn(player)


class Player:
    def __init__(self, name, symbol):
        self.symbol = symbol
        self.name = name


def check_win(board, player):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            print(f'{player.name} are winner!')
            return 1


taken_places = []
game_board = Board()
cell = Cell(0)
game_board.draw_board()
first_player = Player('Petr', 'X')
second_player = Player('Nadya', 'O')

for i in range(9):
    if i % 2 == 0:
        turn(first_player)
        if i > 3:
            if check_win(game_board.board, first_player):
                break
    else:
        turn(second_player)
        if i > 3:
            if i > 3:
                if check_win(game_board.board, second_player):
                    break

if not check_win(game_board.board, first_player) or not check_win(game_board.board, second_player):
    print('It is draw!')
