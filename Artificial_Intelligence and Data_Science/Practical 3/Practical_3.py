# Practical 3 Implement 4 Queen Problem Using Backtracking
########################################################
# Author    -   Karan Gupta
# Roll No.  -   2020PMD4224
# Degree    -   M.Tech (Mobile Computing and Data Analytics)
#########################################################

class NQueens:
    # Prints the Current Visualization of Board
    def displayBoard(self,board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                print(board[i][j],end=" ")
            print()
        print()

    # Function for checking the place of Queens
    def Place(self, i, j, board):
        # Main diagonal
        ti, tj = i - 1, j - 1
        while ti > -1 and tj > -1:
            if board[ti][tj] == 'Q':
                return False
            ti, tj = ti - 1, tj - 1

        ti, tj = i - 1, j + 1
        while ti > -1 and tj < len(board):
            if board[ti][tj] == 'Q':
                return False
            ti, tj = ti - 1, tj + 1

        # column
        ti, tj = i - 1, j
        while ti > -1:
            if board[ti][tj] == 'Q':
                return False
            ti -= 1

        return True

    # FUnction To perform placing the Queen and Return all Possible Solution
    def NQueens(self, i, board):
        if i == len(board):
            return [board[:]]

        res = list()
        for j in range(len(board)):
            
            if self.Place(i, j, board):
                
                board[i] = board[i][:j] + 'Q' + board[i][j + 1:]
                res.extend(self.NQueens(i + 1, board))
                self.displayBoard(board)
            board[i] = '.' * len(board)
            
        return res
        
    # Return a list of list of strings
    def solveNQueens(self, A):
        return self.NQueens(0, ['.' * A] * A)

if __name__ == "__main__":
    Q=NQueens()
    S=Q.solveNQueens(4)
    print(S)