from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer
import time
import math

class tictactoe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] #we will use a single list to rep 3x3 board
        self.currentWinner = None #keep track of winner!

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:    # just getting the row
            print('| ' + ' | '.join(row) + ' |')


    @staticmethod
    def print_board_nums():
    # 0 | 1 | 2 etc(tell us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')


    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot ==' ']
      

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        #if valid move, then make a move(assign square the letter)
        # then return true. if invalid, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.currentWinner = letter 
            return True
        return False


    def winner(self, square, letter):
        # winner if 3 in a row anywere. we have to check all the possibility
        #first let's check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3] 
        if all([spot == letter for spot in row]):
            return True

        #check column
        col_ind = square % 3
        column = [self.board[col_ind*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        #check diagonals
        #but only if the square is an even number like [0, 2, 4, 6, 8]
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]     #left diagonal only
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]     #left diagonal only
            if all([spot == letter for spot in diagonal2]):
                return True

        #if all of these fails
        return False



def play(game, x_player, o_player, print_game=True):
    #return the winnner of the game(the letter)! or none for a tie
    if print_game:
        game.print_board_nums()

    letter = 'X'  # starting letter
    #iterate while the game still empty squares
    #(we don't have to worry about the winner because we'll just return that which breaks the loop)

    while game.empty_squares():
        #get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        #let's define a function to make move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' make a move to square {square}')
                game.print_board()
                print('')   #just empty line

            
            if game.currentWinner:
                if print_game:
                    print(letter + ' wins!')
                return letter

        #after we made our move, we need to alternate letters
            letter = 'O' if letter == 'X' else 'X'
    
    #break
        time.sleep(0.8)

    if print_game:
        print('It\'s a tie')

if __name__ == "__main__":
    x_player = GeniusComputerPlayer('X')
    o_player = HumanPlayer('O')
    t = tictactoe()
    play(t, x_player, o_player, print_game=True)
