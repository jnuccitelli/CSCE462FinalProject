class Board:
    board = []
    '''Number of columns and rows these are set to their defualt connect four values'''
    nCol = 7
    nRow = 6
    curPlayer = 0
    nMoves = 0 
    def __init__(self,nCol,nRow):
        self.nCol = nCol
        self.nRow = nRow
        self.board = []
        self.board = [[-1] * self.nRow for _ in range(self.nCol)]
    '''returns the total amount of moves made by both players'''
    def numMoves(self):
        return self.nMoves
    '''use error checking'''
    def setBoard(self,board):
        self.board = board
    '''takes in a int for col number  0 through n - 1 inclusive where n is the number of columns.
    returns 0 for a column it cant play, 1 for a column it can play and -1 for invalid input'''
    def canPlay(self,col):
        if(col >= self.nCol or col < 0):
            return -1
        for i in range(self.nRow):
            if(self.board[col][i] == -1):
                return 1
        return 0
    '''takes in a int for col number and plays in the col DOES NOT check if its playable'''
    def play(self,col):
        for i in range(self.nRow):
            if(self.board[col][i] == -1):
                self.board[col][i] = self.curPlayer
                self.curPlayer = (self.curPlayer + 1) % 2
                self.nMoves += 1
                return
    '''takes in a char for col number  0 through n - 1 inclusive where n is the number of columns.
    returns 0 for a column that is not a winning move, 1 for a column where it is a winning move and -1 for invalid input'''
    def isWinningMove(self,col):

        count3 = 0
        for i in self.board[col]:
            if(i == -1):
                break
            count3 += 1
        current_player = self.curPlayer
        if(count3 >= 3 and self.board[col][count3-1] == current_player and self.board[col][count3-2] == current_player and self.board[col][count3-3] == current_player):
            return True

        for dy in (-1,0,1):  # Iterate on horizontal (dy = 0) or two diagonal directions (dy = -1 or dy = 1)
            nb = 0                     # counter of the number of stones of current player surronding the played stone in tested direction.
            for dx in (-1,1):# count continuous stones of current player on the left, then right of the played column
                x = col + dx
                y = count3 + dx * dy 
                while( x >= 0 and x < self.nCol and y >= 0 and y < self.nRow and self.board[x][y] == current_player): 
                    nb += 1
                    x += dx
                    y += dx*dy

            if(nb >= 3):
                return True

        return False


