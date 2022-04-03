# p2.py


import copy

# globals
count = 0
solutions = []

SINGLE_RESULT = False


def IsSolution(A, k, S):   
    return k > len(A)-1


def HasThreatInColumn(A, i, j):
    return A[j] == i

def HasThreatOnDiagonal(A, i, k, j):
    return abs(j-k) == abs(i-A[j])

def ThreatIsFound(A, i, j, k):             
    # IF queen in row j has same column as i 
    # OR queens are in the same diagonal means delta row == delta column  
    return HasThreatInColumn(A, i, j) or HasThreatOnDiagonal(A, i, k, j)    
        
    
def ConstructCandidates(A, k, S):
    Result = []
    
    for i in range(1, len(A)):
        hasThreat = False
        
        # looking from 1st to (k-1)th placed queen      
        for j in range(1, k):                  
            if ThreatIsFound(A, i, j, k):
                hasThreat = True
                
        if not hasThreat:
            Result.append(i)
        
    return Result


def Process(A, k, S):
    global count
    count = count + 1   # increment the number of solutions found!

    global solutions
    solutions.append(copy.copy(A[1:len(A)]))


def IsFinished():    
    if SINGLE_RESULT:
        return count > 0
    
    # don't stop until all results are generated
    return False


def Backtrack(A, k, S):
          
    if IsSolution(A, k, S):
        Process(A, k, S)
    else:
        L = ConstructCandidates(A, k, S)
        
        for c in L:
            A[k] = c
            Backtrack(A, k+1, S)
                
            if IsFinished():
                return True   
    

def main():
    
    n = 8  # NOTE, n must be 4 or greater for the n-queens problem    
    
    print("There are",n,"queens.")
    
    A = [0] * (n+1)
    k = 1
    S = None # unused
    
    result = Backtrack(A, k, S)
    
    global solutions
    #print("Set of all solutions =\n" + str(solutions))
    if SINGLE_RESULT and len(solutions) == 1:
        print("Here's one solution:",solutions[0],"\n")
    else:
        print(len(solutions),"solutions were found.\n")
    

main()