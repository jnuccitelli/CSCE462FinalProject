from board import Board
from camera import CaptureBoard

'''calculate the best move of the board'''
def bestMove(board):
    if(board.nMoves == board.nRow * board.nCol):
        return (0,0) #draw
    
    for i in range(board.nCol):

        if(board.canPlay(i) and board.isWinningMove(i)):
            return ((board.nCol * board.nRow + 1 - board.nMoves) // 2,i)

    # the lower bound should be this  
    bestScore = - board.nCol * board.nRow

    bestCol = -1
    for i in range(board.nCol):
        if(board.canPlay(i)):
            nextboard = board
            nextboard.play(i)
            (score,col) = bestMove(nextboard)
            if(score  > bestScore):
                bestScore = score
                bestCol = col

    return (bestScore,bestCol)

def GetBestMoveFromPhoto():
    board = Board(7,6)
    grid = CaptureBoard()
    grid = grid -1
    newBoard = [[-1] * 6 for _ in range(7)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            newBoard[j][i] = grid[i][j]
    board.setBoard(newBoard)
    return bestMove(board)

print(GetBestMoveFromPhoto())





