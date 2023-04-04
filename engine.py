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

        if self.whiteToMove == True:
            #Check Downwards
            try:
                if(self.board[row+2][col+1][0] != "w"):
                    moves.append(Move((row, col), (row+2, col+1), self.board))
            except IndexError:
                pass
            try:
                if(self.board[row+2][col-1][0] != "w"):
                    moves.append(Move((row, col), (row+2, col-1), self.board))
            except IndexError:
                pass
            #Check Upwards
            try:
                if(self.board[row-2][col+1][0] != "w"):
                    moves.append(Move((row, col), (row-2, col+1), self.board))
            except IndexError:
                pass
            try:
                if(self.board[row-2][col-1][0] != "w"):
                    moves.append(Move((row, col), (row-2, col-1), self.board))
            except IndexError:
                pass
                
            #Check Right
            try:
                if(self.board[row+1][col+2][0] != "w"):
                    moves.append(Move((row, col), (row+1, col+2), self.board))
            except IndexError:
                pass
            try:
                if(self.board[row-1][col+2][0] != "w"):
                    moves.append(Move((row, col), (row-1, col+2), self.board))
            except IndexError:
                pass

            #Check Left
            try:
                if(self.board[row+1][col-2][0] != "w"):
                    moves.append(Move((row, col), (row+1, col-2), self.board))
            except IndexError:
                pass
            try:
                if(self.board[row-1][col+2][0] != "w"):
                    moves.append(Move((row, col), (row-1, col-2), self.board))
            except IndexError:
                pass
        #BLACK TURN
        else:
            #Check Upwards
            try:
                if(self.board[row+2][col+1][0] != "b"):
                    moves.append(Move((row, col), (row+2, col+1), self.board))
            except IndexError:
                pass
            try:
                if(self.board[row+2][col-1][0] != "b"):
                    moves.append(Move((row, col), (row+2, col-1), self.board))
            except IndexError:
                pass
            #Check Downwards
            try:
                if(self.board[row-2][col+1][0] != "b"):
                    moves.append(Move((row, col), (row-2, col+1), self.board))
            except IndexError:
                pass
            try:
                if(self.board[row-2][col-1][0] != "b"):
                    moves.append(Move((row, col), (row-2, col-1), self.board))
            except IndexError:
                pass
                
            #Check Right
            try:
                if(self.board[row+1][col+2][0] != "b"):
                    moves.append(Move((row, col), (row+1, col+2), self.board))
            except IndexError:
                pass
            try:
                if(self.board[row-1][col+2][0] != "b"):
                    moves.append(Move((row, col), (row-1, col+2), self.board))
            except IndexError:
                pass

            #Check Left
            try:
                if(self.board[row+1][col-2][0] != "b"):
                    moves.append(Move((row, col), (row+1, col-2), self.board))
            except IndexError:
                pass
            try:
                if(self.board[row-1][col+2][0] != "b"):
                    moves.append(Move((row, col), (row-1, col-2), self.board))
            except IndexError:
                pass

        return moves

    def getBishopMoves(self, row, col, moves):
        pass
    def getRookMoves(self, row, col, moves):

        blockedUp = 0
        blockedDw = 0
        blockedRi = 0
        blockedLe = 0

        if self.whiteToMove == True:
            #UPWARDS
            for i in range(row-1, -1, -1): #Check all current column positions from the start row to the upward board edge. I.e. from curr row to row 0.
                if(blockedUp == 1):
                    break
                if (self.board[i][col] == "--"):
                    moves.append(Move((row, col), (i, col), self.board))
                if (self.board[i][col][0] == "b"):
                    blockedUp = 1 #If an enemy piece is encountered mark it as a valid move, but block further checking up the board.
                    moves.append(Move((row, col), (i, col), self.board))
                if (self.board[i][col][0] == "w"): #If a friendly piece is encountered then mark as blocked and do nothing.
                    blockedUp = 1

            #DOWNWARDS
            for i in range(row+1, 8, 1): #Check all current column positions from the start row to the downward board edge. I.e. from curr row to row 7.
                if(blockedDw == 1):
                    break
                if (self.board[i][col] == "--"):
                    moves.append(Move((row, col), (i, col), self.board))
                if (self.board[i][col][0] == "b"):
                    blockedDw = 1 #If an enemy piece is encountered mark it as a valid move, but block further checking up the board.
                    moves.append(Move((row, col), (i, col), self.board))
                if (self.board[i][col][0] == "w"): #If a friendly piece is encountered then mark as blocked and do nothing.
                    blockedDw = 1
          
            #RIGHT, towards H
            for i in range(col+1, 8, 1): #Check all current row positions from the start col to the rightmost board edge. I.e. from curr col to col H.
                if(blockedRi == 1):
                    break
                if (self.board[row][i] == "--"):
                    moves.append(Move((row, col), (row, i), self.board))
                if (self.board[row][i][0] == "b"):
                    blockedRi = 1 #If an enemy piece is encountered mark it as a valid move, but block further checking up the board.
                    moves.append(Move((row, col), (row, i), self.board))
                if (self.board[row][i][0] == "w"): #If a friendly piece is encountered then mark as blocked and do nothing.
                    blockedRi = 1

            #LEFT, towards A
            for i in range(col-1, -1, -1): #Check all current row positions from the start col to the leftmost board edge. I.e. from curr col to col A.
                if(blockedLe == 1):
                    break
                if (self.board[row][i] == "--"):
                    moves.append(Move((row, col), (row, i), self.board))
                if (self.board[row][i][0] == "b"):
                    blockedLe = 1 #If an enemy piece is encountered mark it as a valid move, but block further checking up the board.
                    moves.append(Move((row, col), (row, i), self.board))
                if (self.board[row][i][0] == "w"): #If a friendly piece is encountered then mark as blocked and do nothing.
                    blockedLe = 1

        else:
            #UPWARDS
            for i in range(row-1, -1, -1): #Check all current column positions from the start row to the upward board edge. I.e. from curr row to row 0.
                if(blockedUp == 1):
                    break
                if (self.board[i][col] == "--"):
                    moves.append(Move((row, col), (i, col), self.board))
                if (self.board[i][col][0] == "w"):
                    blockedUp = 1 #If an enemy piece is encountered mark it as a valid move, but block further checking up the board.
                    moves.append(Move((row, col), (i, col), self.board))
                if (self.board[i][col][0] == "b"): #If a friendly piece is encountered then mark as blocked and do nothing.
                    blockedUp = 1

            #DOWNWARDS
            for i in range(row+1, 8, 1): #Check all current column positions from the start row to the downward board edge. I.e. from curr row to row 7.
                if(blockedDw == 1):
                    break
                if (self.board[i][col] == "--"):
                    moves.append(Move((row, col), (i, col), self.board))
                if (self.board[i][col][0] == "w"):
                    blockedDw = 1 #If an enemy piece is encountered mark it as a valid move, but block further checking up the board.
                    moves.append(Move((row, col), (i, col), self.board))
                if (self.board[i][col][0] == "b"): #If a friendly piece is encountered then mark as blocked and do nothing.
                    blockedDw = 1
          
            #RIGHT, towards H
            for i in range(col+1, 8, 1): #Check all current row positions from the start col to the rightmost board edge. I.e. from curr col to col H.
                if(blockedRi == 1):
                    break
                if (self.board[row][i] == "--"):
                    moves.append(Move((row, col), (row, i), self.board))
                if (self.board[row][i][0] == "w"):
                    blockedRi = 1 #If an enemy piece is encountered mark it as a valid move, but block further checking up the board.
                    moves.append(Move((row, col), (row, i), self.board))
                if (self.board[row][i][0] == "b"): #If a friendly piece is encountered then mark as blocked and do nothing.
                    blockedRi = 1

            #LEFT, towards A
            for i in range(col-1, -1, -1): #Check all current row positions from the start col to the leftmost board edge. I.e. from curr col to col A.
                if(blockedLe == 1):
                    break
                if (self.board[row][i] == "--"):
                    moves.append(Move((row, col), (row, i), self.board))
                if (self.board[row][i][0] == "w"):
                    blockedLe = 1 #If an enemy piece is encountered mark it as a valid move, but block further checking up the board.
                    moves.append(Move((row, col), (row, i), self.board))
                if (self.board[row][i][0] == "b"): #If a friendly piece is encountered then mark as blocked and do nothing.
                    blockedLe = 1

        return moves
    
    def getQueenMoves(self, row, col, moves):
        pass
    def getKingMoves(self, row, col, moves):
        
        if self.whiteToMove == True:
            for i in range(-1, 2):
                try:
                    if self.board[row+1][col+i][0] not in ("w"): #Check Downwards
                        moves.append(Move((row, col), (row+1, col+i), self.board))
                except IndexError:
                    pass
                try:
                    if self.board[row-1][col+i][0] not in ("w"): #Check Upwards
                        moves.append(Move((row, col), (row-1, col+i), self.board))
                except IndexError:
                    pass

            try:
                if self.board[row][col-1][0] not in ("w"): #Check left of king
                    moves.append(Move((row, col), (row, col-1), self.board)) 
            except IndexError:
                pass
            try:
                if self.board[row][col+1][0] not in ("w"): #Check right of king
                    moves.append(Move((row, col), (row, col+1), self.board)) 
            except IndexError:
                pass
        else:
            for i in range(-1, 2):
                try:
                    if self.board[row+1][col+i][0] not in ("w"): #Check Downwards
                        moves.append(Move((row, col), (row+1, col+i), self.board))
                except IndexError:
                    pass
                try:
                    if self.board[row-1][col+i][0] not in ("w"): #Check Upwards
                        moves.append(Move((row, col), (row-1, col+i), self.board))
                except IndexError:
                    pass

            try:
                if self.board[row][col-1][0] not in ("w"): #Check left of king
                    moves.append(Move((row, col), (row, col-1), self.board)) 
            except IndexError:
                pass
            try:
                if self.board[row][col+1][0] not in ("w"): #Check right of king
                    moves.append(Move((row, col), (row, col+1), self.board)) 
            except IndexError:
                pass

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