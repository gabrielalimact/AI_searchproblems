import math
import time
import random


class Player():
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_move = False
        value = None
        while not valid_move:
            move = input(self.letter + '\'s turn. Input move (0 - 8): ')
            try:
                value = int(move)
                if value not in game.available_moves():
                    raise ValueError
                valid_move = True
            except ValueError:
                print('Invalid move!')
        return value


class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            move = random.choice(game.available_moves())
        else:
            move = self.minimax(game, self.letter)['position']
        return move

    def minimax(self, state, player):
        max_player = self.letter
        opponent = 'O' if self.letter == 'X' else 'X'

        # lets check if the previous move is a winner
        if state.winner == opponent:
            return {'position': None, 'score': 1*(state.empty_spaces() + 1) if opponent == max_player else -1*(state.empty_spaces() + 1)}

        elif not state.is_empty():
            return {'position': None, 'score': 0}

        if player == max_player:
            best_score = {'position': None, 'score': -
                          math.inf}  # score should maximize
        else:
            # score should minimize
            best_score = {'position': None, 'score': math.inf}

        for possible_moves in state.available_moves():
            state.make_move(possible_moves, player)
            # simulate a game after the move
            possible_score = self.minimax(state, opponent)

            # undo move
            state.board[possible_moves] = ' '
            state.winner = None
            possible_score['position'] = possible_moves

            if player == max_player:
                if possible_score['score'] > best_score['score']:
                    best_score = possible_score
            else:
                if possible_score['score'] < best_score['score']:
                    best_score = possible_score
        return best_score


class RandomMove(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        return random.choice(game.available_moves())


class Game():
    def __init__(self):
        self.board = self.make_board()
        self.winner = None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_nums():
        num = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]

        for i in num:
            print('| ' + ' | '.join(i) + ' |')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.check_winner(square, letter):
                self.winner = letter
            return True
        return False

    def check_winner(self, square, letter):
        # row
        row_i = math.floor(square/3)
        row = self.board[row_i*3:(row_i+1)*3]
        if all([l == letter for l in row]):
            return True

        # col
        col_i = square % 3
        col = [self.board[i*3+col_i] for i in range(3)]
        if all([l == letter for l in col]):
            return True

        if square % 2 == 0:
            diag1 = [self.board[i] for i in [0, 4, 8]]
            diag2 = [self.board[i] for i in [2, 4, 6]]

            if all([l == letter for l in diag1]):
                return True
            if all([l == letter for l in diag2]):
                return True
        return False

    def is_empty(self):
        return ' ' in self.board

    def empty_spaces(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]


def lets_play(game, x_player, o_player, print_game=True):

    if print_game:
        game.print_nums()
        game.print_board()

    letter = 'O'
    while game.is_empty():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + ' makes a move to {} square'.format(square))
                game.print_board()
                print('')

            if game.winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

        letter = 'O' if letter == 'X' else 'X'
        # time.sleep(.2)

    if print_game:
        print('Draw!')


def main():
    game = Game()
    choice = int(
        input("Enter 1 to play against computer, 2 to play against another player or 3 to computer against computer: "))

    if choice == 1:
        x_player = HumanPlayer('X')
        o_player = ComputerPlayer('O')
    elif choice == 2:
        x_player = HumanPlayer('X')
        o_player = HumanPlayer('O')
    elif choice == 3:
        x_player = ComputerPlayer('X')
        o_player = ComputerPlayer('O')

    lets_play(game, x_player, o_player, print_game=True)


if __name__ == '__main__':
    main()
    yn = input('Play again? (y/n): ')
    while yn == 'y':
        main()
        yn = input('Play again? (y/n): ')

        if yn == 'n':
            print('Bye!')
