#
# Connect 4 Part 1
#
# A Connect Four Board class
# KRISH AGARWAL
# CS 111
#

class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """   
    ### add your constructor here ###
    
    
    def __init__(self, height, width):
        "constructor to initiaalize variables"  
        self.width= width
        self.height= height
        self.slots = [[' '] * self.width for row in range(self.height)]

    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''         # begin with an empty string
        
        # add one row of slots at a time to s
        for row in range(self.height):
            s += '|'    # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        ### add your code here ###
        for hyphen in range(self.width*2 + 1):
            s+= '-' 
        s += '\n'  
        for i in range(self.width):
            s+= ' ' + str(i%10)
        return s


    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        ### put the rest of the method here ###
        row = -1     
        while True:
            if self.slots[row][col]!= ' ':
                row-= 1
            else:
                self.slots[row][col] = checker
                break
    
    ### add your reset method here ###
    
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    ### add your remaining methods here
    
    def reset(self):
        "resetting the board to all one spaces"
        self.slots = [[' ']*self.width for row in range(self.height)]
        
    def can_add_to(self, col):
        "return true if columns are not full else returns false"
        if col > self.width - 1 or col<0:
            return False
        else:
            for row in range(self.height):
                if self.slots[row][col] == ' ':
                    return True
            return False
    
    def is_full(self):
        "return true if board is full else returns false if there is space in the grid"
        for col in range(self.width):
            if self.can_add_to(col)==True:
                return False
        return True
    
    def remove_checker(self, col):
        "removes top checker from the column col"
        row= 0
        while row < self.height:
            if self.slots[row][col] != ' ':
                self.slots[row][col] = ' '
                break
            else:
                row+= 1
        
    #inserting helper functions to support function is_win_for(self, checker)
    
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal 4-pair checker counted as a win
        """
        for row in range(self.height):
            for col in range(self.width-3):
                if self.slots[row][col] == checker and self.slots[row][col + 1] == checker and \
                    self.slots[row][col + 2] == checker and self.slots[row][col + 3] == checker:
                    return True
        return False
    
    def is_vertical_win(self, checker):
        """Checks for a vertical 4-pair checker counted as a win
        """
        for col in range(self.width):
            for row in range(self.height-3):
                if self.slots[row][col] == checker and self.slots[row +1][col] == checker and \
                    self.slots[row +2][col] == checker and self.slots[row +3][col] == checker:
                    return True
        return False
    
    def is_up_diagonal_win1(self, checker):
        """Checks for a horizontal-up 4-pair checker counted as a win
        """
        for row in range(3, self.height):
            if self.slots[row][0] == checker and self.slots[row -1][1] == checker and \
                self.slots[row -2][2] == checker and self.slots[row -3][3] == checker:
                return True
        for col in range(1, self.width-3):
            for row in range(3, self.height):
                if self.slots[row][col] == checker and self.slots[row -1][col +1] == checker and \
                    self.slots[row -2][col +2] == checker and self.slots[row -3][col +3] == checker:
                        return True
        return False
    
    def is_down_diagonal_win2(self, checker):
        """Checks for a horizontal down 4-pair checker counted as a win"""
        for row in range(self.height -3):
            if self.slots[row][0] == checker and self.slots[row +1][1] == checker and \
                self.slots[row +2][2] == checker and self.slots[row +3][3] == checker:
                return True
        for col in range(1, self.width-3):
            for row in range(self.height -3):
                if self.slots[row][col] == checker and self.slots[row +1][col +1] == checker and \
                    self.slots[row +2][col +2] == checker and self.slots[row +3][col +3] == checker:
                        return True
        return False
    
    def is_win_for(self, checker):
        "returns True if there are four consecutive checker"
        assert(checker == 'X' or checker == 'O')
        if self.is_vertical_win(checker) or self.is_horizontal_win(checker) or \
            self.is_up_diagonal_win2(checker) or self.is_down_diagonal_win1(checker):
            return True
        return False
        