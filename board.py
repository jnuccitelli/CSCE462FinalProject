class Board:
    

    '''The board is incoded through a string of numbers repersenting a move. For example 44555 means that the first
    player played in column four the 2nd player then played in column 4, the first player played in column 5, the second
    player played in column 5, and finally the first player played in column 5'''
    boardString = ""
    '''Number of columns and rows these are set to their defualt connect four values'''
    nCol = 7
    nRow = 6

    def __init__(self,nCol):
        self.nCol = nCol

    '''returns the total amount of moves made by both players'''
    def nMoves(self):
        return len(self.boardString)

    '''takes in a char for col number  0 through n - 1 inclusive where n is the number of columns.
    returns 0 for a column it cant play, 1 for a column it can play and -1 for invalid input'''
    def canPlay(self,col):
        if(int(col) >= self.nCol or int(col) < 0):
            return -1
        charCount = 0
        for char in self.boardString:
            if(char == col):
                charCount += 1
        if(charCount  == self.nRow):
            return 0
        return 1
    
    '''takes in a char for col number and plays in the col DOES NOT check if its playable'''
    def play(self,col):
        self.boardString += col
    
    '''takes in a char for col number  0 through n - 1 inclusive where n is the number of columns.
    returns 0 for a column that is not a winning move, 1 for a column where it is a winning move and -1 for invalid input'''
    def isWinningMove(self,col):
        '''TODO actually do this :('''
        return 1
    
