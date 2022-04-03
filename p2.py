# p2.py


import copy

# globals
count = 0
solutions = []

SINGLE_RESULT = False


def IsSolution(A, k, S):   
    return k > len(A) -1


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
    
    # i is column...
    for i in range(1, len(A)):
        hasThreat = False
        
        # print("\t\tcolumn i=",i)
        
        # looking at ***PREVIOUSLY*** placed queens
        for j in range(1, k):
            # k-1):  this SHOULD be k, because the upper range is NOT inclusive in Python

            # print("\t\t\tlooking at row j = ",j)
                        
            if ThreatIsFound(A, i, j, k):
                hasThreat = True
                
        if not hasThreat:
            Result.append(i)

                        
    return Result


def Process(A, k, S):
    global count
    count = count + 1   # increment the number of solutions found!
    #print("\t\t==--- Solution Found ---== >>>>> ",A)
    global solutions
    solutions.append(copy.copy(A[1:len(A)]))


def IsFinished():    
    # assuming we only want to return 1 result, otherwise always return False
    
    if SINGLE_RESULT:
        return count > 0
    
    return False


def Backtrack(A, k, S):
    # print("\nBacktrack(",A,", ",k,")")
          
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
    
    print("Hello! n =",n)
    
    A = [0] * (n+1)
    k = 1
    S = None # unused
    
    result = Backtrack(A, k, S)
    
    global solutions
    #print("Set of all solutions =\n" + str(solutions))
    print("Number of possible solutions? ",len(solutions),"\n")
    


main()