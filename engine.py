###
###
###

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
                if self.whiteToMove == turn or not self.whiteToMove == turn:
                    piece = self.board[r][c][1]
                    if piece == 'p': # Switch to match case statements, but need to fix pylance version or something
                        self.getPawnMoves(r, c, moves)
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
        pass
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
        self.startCol = start[0]
        self.startRow = start[1]
        self.endCol = end[0]
        self.endRow = end[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]

    #Add full chess.com notation
    def getChessNotation(self):
        return self.getRankAndFile(self.startRow, self.startCol) + self.getRankAndFile(self.endRow, self.endCol)
        
    def getRankAndFile(self, r, c):
        return self.colsToFile[c] + self.rowsToRank[r]