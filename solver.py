from board import Board


'''calculate the best move of the board'''
def bestMove(board):
    if(board.nMoves() == board.nRow * board.nCol):
        return (0,0) #draw
    
    for i in range(board.nCol):

        if(board.canPlay(str(i)) and board.isWinningMove(i)):
            return ((board.nCol * board.nRow + 1 - board.nMoves()) / 2,i)

    # the lower bound should be this  
    bestScore = - board.nCol * board.nRow
    bestCol = 0
    for i in range(board.nCol):
        if(board.canPlay(str(i))):
            nextboard = board
            nextboard.play(str(i))
            (score,col) = bestMove(nextboard)
            if(score  > bestScore):
                bestScore = score
                bestCol = col

    return (bestScore,bestCol)
#create a standard connect four board
board = Board(7,6)
print(bestMove(board))