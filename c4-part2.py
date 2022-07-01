#
# Connect 4 Part 2
#
# A Connect Four Board class
# KRISH AGARWAL
# CS 111
#  

from ps9pr1 import Board

# write your class below.

class Player:
    def __init__(self, checker):
        " constructor for class connect4 to initiaize variables"
        assert(checker == 'X' or checker == 'O')
        self.checker= str(checker)
        self.num_moves= 0
        
    def __repr__(self):
        'function to print the output appropriately'
        return 'Player '+self.checker
    
    def opponent_checker(self):
        "returns opponent's checker (X/O)"
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
        
    def next_move(self, b):
        "returns the column number where the current player wishes to make the next move"
        self.num_moves+= 1
        while True:
            col = int(input('Enter a column: '))
            if col >= 0 and col < b.width:
                return col
            else:
                print('Try again!')
            