#!/bin/usr/python
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])


        def search(m,n,i,j,board,word, visited):
            vis = visited.copy()
            vis.add((i,j))
            if len(word) == 0:
                return True

            if i < m-1 and (i+1,j) not in vis:
                if word[0] == board[i+1][j]:
                    res = search(m,n,i+1,j, board, word[1:], vis)
                    if res == True:
                        return True
            if i > 0 and (i-1,j) not in vis:
                if word[0] == board[i-1][j]:
                    res = search(m,n,i-1,j, board, word[1:], vis)
                    if res == True:
                        return True
            if j < n-1 and (i,j+1) not in vis:
                if word[0] == board[i][j+1]:
                    res = search(m,n,i,j+1, board, word[1:], vis)
                    if res == True:
                        return True
            if j > 0 and (i,j-1) not in vis:
                if word[0] == board[i][j-1]:
                    res = search(m,n,i,j-1, board, word[1:], vis)
                    if res == True:
                        return True

        for i in range(m):
            for j in range(n):
                vis = set()
                if board[i][j] == word[0]:
                    vis.add((i,j))
                    res = search(m,n,i,j,board,word[1:], vis)
                    if res == True:
                        return True


        return False
