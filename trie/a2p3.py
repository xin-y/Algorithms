"""
ECE606, F'20, Assignment 2, Problem 3
Skeleton solution file
"""

"""
You are not allowed to import anything
"""
## initialize the Trie
def CreateNode():
    ret = []
    for i in range(26):
        ret.append([[], False])
    return ret

def InsertIntoTrie(T, s):
    """
    You need to implement this method.
    You are certainly allowed to define any subroutines you want
    above this method in this file.
    """
    if len(T) == 0:
        T[:] = CreateNode()
   
    n = ord(s[0]) - ord('a')
    
    if len(s) > 1:
        InsertIntoTrie(T[n][0], s[1:])
    else:
        T[n][1] = True

def DeleteFromTrie(T, s):
    """
    You need to implement this method.
    You are certainly allowed to define any subroutines you want
    above this method in this file.
    """
    if len(T) == 0:
        return
    
    n = ord(s[0]) - ord('a')
    
    if len(s) > 1:
        if len(T[n][0]) == 0:
            return
        else:
            DeleteFromTrie(T[n][0], s[1:])
    else:
        T[n][1] = False
        
    emptyT = CreateNode()
         
    if T == emptyT:
        T[:] = []
        
##    isClear = 1
##    for i in range(26):
##        if T[i][1] == True:
##            isClear = 0
##            break
##        else:
##            pass
##        
##    if isClear == 1:
##        T[:] = []
