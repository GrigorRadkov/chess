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
            self.whitToMove = not self.whiteToMove #swap player turn
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