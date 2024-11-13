class Board:
    

    '''The board is incoded through a string of numbers repersenting a move. For example 44555 means that the first
    player played in column four the 2nd player then played in column 4, the first player played in column 5, the second
    player played in column 5, and finally the first player played in column 5'''
    boardString = ""
    '''Number of columns and rows these are set to their defualt connect four values'''
    nCol = 7
    nRow = 6

    def __init__(self,nCol,nRow):
        self.nCol = nCol
        self.nRow = nRow

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
        #turn the board into a list of lists
        boardList= [[-1] * self.nRow for _ in range(self.nCol)]
        
        count  = 0
        for c in self.boardString:
            count2 = 0
            for r in boardList[int(c)]:
                if(r == -1):
                    boardList[int(c)][count2] = (count % 2)
                    count += 1
                    break
                count2 += 1

        count3 = 0

        for i in boardList[col]:
            if(i == -1):
                break
            count3 += 1

        current_player = count % 2
        if(count3 >= 3 and boardList[col][count3-1] == current_player and boardList[col][count3-2] == current_player and boardList[col][count3-3] == current_player):
            return True

        for dy in (-1,0,1):  # Iterate on horizontal (dy = 0) or two diagonal directions (dy = -1 or dy = 1)
            nb = 0                     # counter of the number of stones of current player surronding the played stone in tested direction.
            for dx in (-1,1):# count continuous stones of current player on the left, then right of the played column
                x = col + dx
                y = count3 + dx * dy
                while( x >= 0 and x < self.nCol and y >= 0 and y < self.nRow and boardList[x][y] == current_player): 
                    nb += 1
                    x += dx
                    y += dx*dy

            if(nb >= 3):
                return True

        return False


