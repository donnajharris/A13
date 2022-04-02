# p2.py


import math
from re import T

count = 0

solutions = []

'''
Use your Backtrack algorithm to solve the n-queens problem in Python, 

by providing appropriate implementation for the IsSolution, ConstructCandidates, Process and IsFinished  functions

'''


def IsSolution(A, k, S):
    
    print("\tIsSolution( {0}, {1} ) - where k > len(A)? {1} > {2}? {3}\n".format(A, k, len(A), k > len(A)) )
    
    return k > len(A)


def HasThreatInColumn(A, col_index_of_candidate, row_of_existing_queen):
    
    result = A[row_of_existing_queen] == col_index_of_candidate
    
    if result:
        print("\t\t\tThere is a threat in the same column.")
    
    return result
  

def HasThreatOnDiagonal(A, i, k, j):
    
    # two points are on the same diagonal, if either
    #   y_2 - y_1 == x_2 - x_1    (postive slope)
    #   y_2 - y_1 == x_1 - x_2    (negative slope)
    
    # y values are like the rows  (k and j)
    # x values are like the columns  (i and A[row_index])
    
    # 1 is the placed queen
    # 2 is the candidate placement of the next queen
    
    result = abs(j-k) == abs(i-A[j])
    
    if result:
        print("\t\t\tThere is a threat on one of the diagonals.")
    
    return result
        
    
def ConstructCandidates(A, k, S):
    Result = []
    
    print("\tConstructCandidates()\t- for Queen in Row k =",k)
    
    # i is column...
    for i in range(1, len(A)):
        hasThreat = False
        
        print("\t\tcolumn i=",i)
        
        # looking at ***PREVIOUSLY*** placed queens
        for j in range(1, k): # k-1):  this SHOULD be k, because the upper range is NOT inclusive

            print("\t\t\tlooking at row j = ",j)
                
            # IF queen in row j has same column as i 
            # OR queens are in the same diagonal means delta row == delta column 
                        
            if HasThreatInColumn(A, i, j) or HasThreatOnDiagonal(A, i, k, j):
            #if i == A[i] or abs(k-j) == abs(i-A[j]):
                print("\t\tFound a threat...")
                hasThreat = True
                
                
        if not hasThreat:
            #print("\t\t\tQueen {0} offers no threat to Queen {1}.".format(i,k))
            Result.append(i)
        else:
            print()
            #print("Threat... returning nuthin'")
            
            
    print("\n\t\tReturning Result = ",Result,"\n")
            
    return Result


def Process(A, k, S):
    print("\tProcess() - ")
    global count
    count = count + 1   # increment the number of solutions found!
    print("\t\t==--- Solution Found ---== >>>>> ",A)
    global solutions
    solutions.append(A)


def IsFinished():
    #print("\tIsFinished() - Is count ({0}) > 0? {1}".format(count, count > 0))
    
    # assuming we only want to return 1 result, otherwise always return False
    #return count > 0
    
    return False


def Backtrack(A, k, S):
    print("\nBacktrack(",A,", ",k,")")
          
    if IsSolution(A, k, S):
        Process(A, k, S)
    else:
        L = ConstructCandidates(A, k, S)
        
        for c in L:
            
            
            
            if k+1 < len(A):
                A[k+1] = c
                print("\t\tKeep going...!")
            #else:
            #    print("\t\t\tk+1 is bigger than len(A), so we're gonna hit the stop")
            Backtrack(A, k+1, S)
                
            # if IsFinished():
            #     return True
            # else:
            #     print("\tStill not done looking for solutions.\n")   
                
    # return False      
            

def main():
    
    n = 4   # NOTE, n must be 4 or greater for the n-queens problem
    
    print("Hello! n =",n)
    
    A = [0] * (n+1)
    k = 0
    S = None # unused
    
    result = Backtrack(A, k, S)
    #print("One or more solutions found? ",result,"\n")
    
    global solutions
    print("Set of all solutions =\n" + str(solutions))
    


main()