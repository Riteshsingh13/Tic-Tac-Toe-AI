import math
import random

class player:
    def __init__(self, letter):
        #letter is X and O
        self.letter = letter

    def get_move(self, game):
        pass

class RandomComputerPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        #get a random valid spot for our next move 
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0, 8):')
            # we're going to check that this is a correct value by trying to cast
            # it to an integer, and if it's not, than we say it's invalid 
            # if that spot is not available on the board, we also say its invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True  # if this are successful, than yay!
            except ValueError:
                print('Ops!, invalid square. Try again')
        return val


class GeniusComputerPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())  #randomly choose one
        else:
            #get the square based off minimax algorithm
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player  = self.letter  #yourself!
        other_player = 'O' if player == 'X' else 'X'   #the other player....so whatever letter is not u

        #first check if the previous move is winner
        # the bace condition
        if state.currentWinner == other_player:
            #we should return the position and score
            # for minimax to work
            return {'position':None,
                    'score':1*(state.num_empty_squares() + 1) if other_player == max_player 
                    else -1*(state.num_empty_squares() + 1)
                    }

        elif not state.empty_squares():  #no empty square
            return {'position': None, 'score': 0}


        if player == max_player:
            best = {'position': None, 'score': -math.inf}   #each score should maximize (be larger)
        else:
            best = {'position': None, 'score': math.inf}    #each score should minimize

        for possible_move in state.available_moves():
            #step1 - make a move, try that spot
            state.make_move(possible_move, player)

            #step2 - recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(state, other_player)  #now, we alternate player

            #step3 - undo the move
            state.board[possible_move] = ' '
            state.currentWinner  = None
            sim_score['position'] = possible_move   #otherwise this will get messed up from the recursion

            #step4 - update the dictionaries if necessary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score   #replace best
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score   #replace best
        return best

                    


