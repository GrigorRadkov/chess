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
                print(f"Row: {r}, Col: {c}, Turn: {turn}")
                if (self.whiteToMove and turn == "w") or (not self.whiteToMove and turn == "b"):
                    piece = self.board[r][c][1]
                    print(f"Row: {r}, Col: {c}, Piece: {piece}")
                    if piece == 'p': # Switch to match case statements/dictionary that calls a function for each piece type
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

    def getPawnMoves(self, row, col, moves): #Promotion done elsewhere
        if self.whiteToMove == True:
            if(row+1 != -1):
                if self.board[row-1][col] == "--":
                    moves.append(Move((row, col), (row-1, col), self.board))
                if row == 6 and self.board[row-2][col] == "--":
                    moves.append(Move((row, col), (row-2, col), self.board))
                if  ((col - 1) >= 0) and ((row - 1) >= 0):
                    if (self.board[row-1][col-1][0] == "b"): #Capture diagonally left
                        moves.append(Move((row, col), (row-1, col-1), self.board))
                if  ((col + 1 ) <= 7) and ((row - 1) >= 0):
                    if (self.board[row-1][col+1][0] == "b"): #Capture diagonally right
                        moves.append(Move((row, col), (row-1, col+1), self.board))
                
        else:
            if(row+1 != 8):
                if self.board[row+1][col] == "--":
                    moves.append(Move((row, col), (row+1, col), self.board))
                if row == 1 and self.board[row+2][col] == "--":
                    moves.append(Move((row, col), (row+2, col), self.board))
                if  ((col - 1) >= 0) and ((row + 1) <= 7):
                    if (self.board[row+1][col-1][0] == "w"): #Capture diagonally left
                        moves.append(Move((row, col), (row+1, col-1), self.board))
                if  ((col + 1 ) <= 7) and ((row + 1) <= 7):
                    if (self.board[row+1][col+1][0] == "w"): #Capture diagonally right
                        moves.append(Move((row, col), (row+1, col+1), self.board))

        return moves

    def getKnightMoves(self, row, col, moves):
        directions = ((2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)) #All directions
        enemyColor =  "b" if self.whiteToMove else "w"

        for d in directions:
            currRow = row + d[0]  
            currCol = col + d[1]  
            print(d, currRow, currCol)
            if((0 <= currRow < 8) and (0 <= currCol < 8)):
                if(self.board[currRow][currCol] == "--"):
                    moves.append(Move((row, col), (currRow, currCol), self.board))
                elif (self.board[currRow][currCol][0] == enemyColor):
                    moves.append(Move((row, col), (currRow, currCol), self.board))

        return moves

    def getBishopMoves(self, row, col, moves):
        directions = ((-1, -1), (1, -1), (-1, 1), (1, 1)) #Up left diagonally, Down Left diagonally, Up right diagonally, Down right diagonally
        enemyColor =  "b" if self.whiteToMove else "w"

        for d in directions:
            for i in range(1, 8, 1):
                currRow = row + d[0] * i #Iterate from current row towards current direction
                currCol = col + d[1] * i #Iterate from current col towards current direction
                if((0 <= currRow < 8) and (0 <= currCol < 8)):
                    if(self.board[currRow][currCol] == "--"):
                        moves.append(Move((row, col), (currRow, currCol), self.board))
                    elif (self.board[currRow][currCol][0] == enemyColor):
                        moves.append(Move((row, col), (currRow, currCol), self.board))
                        break #Break upon first enemy encountered
                    else:
                        break #Break in friendly unit case

        return moves
    
    def getRookMoves(self, row, col, moves):
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1)) #Up, Down, Left, Right
        enemyColor =  "b" if self.whiteToMove else "w"

        for d in directions:
            for i in range(1, 8, 1):
                currRow = row + d[0] * i #Iterate from current row towards current direction
                currCol = col + d[1] * i #Iterate from current col towards current direction
                if((0 <= currRow < 8) and (0 <= currCol < 8)):
                    if(self.board[currRow][currCol] == "--"):
                        moves.append(Move((row, col), (currRow, currCol), self.board))
                    elif (self.board[currRow][currCol][0] == enemyColor):
                        moves.append(Move((row, col), (currRow, currCol), self.board))
                        break #Break upon first enemy encountered
                    else:
                        break #Break in friendly unit case

        return moves
    
    def getQueenMoves(self, row, col, moves):
        self.getRookMoves(row, col, moves)
        self.getBishopMoves(row, col, moves)
        

    def getKingMoves(self, row, col, moves):    
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)) #All directions
        enemyColor =  "b" if self.whiteToMove else "w"

        for d in directions:
            currRow = row + d[0]  
            currCol = col + d[1]  
            print(d, currRow, currCol)
            if((0 <= currRow < 8) and (0 <= currCol < 8)):
                if(self.board[currRow][currCol] == "--"):
                    moves.append(Move((row, col), (currRow, currCol), self.board))
                elif (self.board[currRow][currCol][0] == enemyColor):
                    moves.append(Move((row, col), (currRow, currCol), self.board))

        return moves
    
    def promotePawn(self, row, col, moves):
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
        print("Move Init:", self.moveId)

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveId == other.moveId
        return False

    #Add full chess.com notation
    def getChessNotation(self):
        return self.getRankAndFile(self.startRow, self.startCol) + self.getRankAndFile(self.endRow, self.endCol)
        
    def getRankAndFile(self, r, c):
        return self.colsToFile[c] + self.rowsToRank[r]