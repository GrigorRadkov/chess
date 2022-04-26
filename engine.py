###
###
###

from numpy import isin


class GameState():
    def __init__(self):

        self.board = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
        ]
        self.whiteToMove = True
        self.moveLog = []

    def makeMove(self, move):
        if move.pieceMoved != "--":
            self.board[move.startRow][move.startCol] = "--"
            self.board[move.endRow][move.endCol] = move.pieceMoved
            self.moveLog.append(move)
            self.whiteToMove = not self.whiteToMove #swap player turn

    def undoMove(self):
        if len(self.moveLog) != 0: 
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol]     = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove #swap player turn when undoing

    def getValidMoves(self):
        pass

    def getAllPossibleMoves(self):
        moves = []
        for r in range(len(self.board)): #rows
            for c in range(len(self.board[r])): #columns in row
                turn = self.board[r][c][0]
                if (self.whiteToMove and turn == "w") or (not self.whiteToMove and turn == "b"):
                    piece = self.board[r][c][1]
                    if piece == 'p': # Switch to match case statements, update to python 3.10 maybe
                        moves = self.getPawnMoves(r, c, moves)         
                    elif piece == 'N':
                        self.getKnightMoves(r, c, moves)
                    elif piece == 'B':
                        self.getBishopMoves(r, c, moves)
                    elif piece == 'R':
                        self.getRookMoves(r, c, moves)
                    elif piece == 'Q':
                        self.getQueenMoves(r, c, moves)
                    elif piece == 'K':
                        self.getKingMoves(r, c, moves)

        return moves

    def getPawnMoves(self, row, col, moves):
        if self.whiteToMove == True:
            if self.board[row-1][col] == "--":
                moves.append(Move((row, col), (row-1, col), self.board))
            if  ((col - 1) >= 0) and ((row - 1) >= 0):
                if (self.board[row-1][col-1][0] == "b"): #Capture diagonally left
                    moves.append(Move((row, col), (row-1, col-1), self.board))
            if  ((col + 1 ) <= 7) and ((row - 1) >= 0):
                if (self.board[row-1][col+1][0] == "b"): #Capture diagonally right
                    moves.append(Move((row, col), (row-1, col+1), self.board))
        else:
            if self.board[row+1][col] == "--":
                moves.append(Move((row, col), (row+1, col), self.board))
            if  ((col - 1) >= 0) and ((row + 1) <= 7):
                if (self.board[row+1][col-1][0] == "w"): #Capture diagonally left
                    moves.append(Move((row, col), (row+1, col-1), self.board))
            if  ((col + 1 ) <= 7) and ((row + 1) <= 7):
                if (self.board[row+1][col+1][0] == "w"): #Capture diagonally right
                    moves.append(Move((row, col), (row+1, col+1), self.board))

        return moves

    def getKnightMoves(self, row, col, moves):
        pass
    def getBishopMoves(self, row, col, moves):
        pass
    def getRookMoves(self, row, col, moves):
        pass
    def getQueenMoves(self, row, col, moves):
        pass
    def getKingMoves(self, row, col, moves):
        pass

class Move():

    #Notation switch
    ranksToRows =  {"1": 7, "2": 6, "3": 5, "4": 4, "5":3, "6": 2, "7": 1, "8": 0}
    rowsToRank = {val: key for key, val in ranksToRows.items()}
    filesToCols =  {"a": 0, "b": 1, "c": 2, "d": 3, "e":4, "f": 5, "g": 6, "h":7}
    colsToFile = {val: key for key, val in filesToCols.items()}

    def __init__(self, start, end, board):
        self.startRow = start[0]
        self.startCol = start[1]
        self.endRow = end[0]
        self.endCol = end[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        self.moveId = self.startRow*1000 + self.startCol*100 + self.endRow*10 + self.endCol
        print(self.moveId)

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveId == other.moveId
        return False

    #Add full chess.com notation
    def getChessNotation(self):
        return self.getRankAndFile(self.startRow, self.startCol) + self.getRankAndFile(self.endRow, self.endCol)
        
    def getRankAndFile(self, r, c):
        return self.colsToFile[c] + self.rowsToRank[r]