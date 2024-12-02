from board import Board
from camera import CaptureBoard

def bestMove(board, depth, alpha=float('-inf'), beta=float('inf')):
    def evaluate_board(board):
        score = 0
        center_col = 3
        for col in range(board.nCol):
            for row in range(board.nRow):
                if board.board[col][row] == board.curPlayer:
                    score += 4 - abs(center_col - col)  
        return score


    if board.nMoves == board.nRow * board.nCol:
        return 0, -1 


    if depth == 0:
        return evaluate_board(board), -1

    for col in range(board.nCol):
        if board.canPlay(col) and board.isWinningMove(col):
            return (board.nCol * board.nRow + 1 - board.nMoves) // 2, col
    bestScore = float('-inf')
    bestCol = -1

    playable_cols = [col for col in range(board.nCol) if board.canPlay(col)]

    for col in playable_cols:
        for row in range(board.nRow):
            if board.board[col][row] == -1:
                board.board[col][row] = board.curPlayer
                board.curPlayer = (board.curPlayer + 1) % 2
                board.nMoves += 1
                break


        score, _ = bestMove(board, depth - 1, -beta, -alpha)
        score *= -1  
        for row in range(board.nRow - 1, -1, -1):
            if board.board[col][row] != -1:
                board.board[col][row] = -1
                board.curPlayer = (board.curPlayer + 1) % 2
                board.nMoves -= 1
                break

        if score > bestScore:
            bestScore = score
            bestCol = col

        alpha = max(alpha, bestScore)
        if alpha >= beta:
            break  
    return bestScore, bestCol

def winCheck(board):
    orgPlayer = board.curPlayer
    opponent = (board.curPlayer + 1) % 2
    board.curPlayer = opponent

    for col in range(board.nCol):
        if(board.canPlay(col) and board.isWinningMove(col)):
            return -21,col
        
    board.curPlayer = orgPlayer
    return bestMove(board,9)

def GetBestMoveFromPhoto():
    board = Board(7,6)
    grid = CaptureBoard()
    grid = grid -1
    print(grid)
    newBoard = [[-1] * 6 for _ in range(7)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            newBoard[j][i] = grid[i][j]
    board.setBoard(newBoard)
    res = winCheck(board)
    print("best move: ",res)
    return res

