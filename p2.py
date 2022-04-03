# p2.py


import copy

# global
solution_count = 0


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
    global solution_count
    solution_count = solution_count + 1   # increment the number of solutions found!
    print(A[1:len(A)])


def IsFinished():    
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
    
    n = 8  # NOTE, n must be 1, or 4+ for a solution to the n-queens problem    
    
    print("\nTrying to neutrally place",n,"queens on a",n,"x",n,"board.\n")
    
    A = [0] * (n+1)
    k = 1
    S = None # unused
    
    result = Backtrack(A, k, S)

    print("\n",solution_count,"solutions exist for the " + str(n) + "-Queens problem.")
    

main()