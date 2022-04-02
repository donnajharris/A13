# p2.py


import math
import copy

count = 0

solutions = []

'''
Use your Backtrack algorithm to solve the n-queens problem in Python, 

by providing appropriate implementation for the IsSolution, ConstructCandidates, Process and IsFinished  functions

'''


def IsSolution(A, k, S):
    
    print(S,"\tIsSolution( {0}, {1} ) - where k > len(A)-1? {1} > {2}? {3}\n".format(A, k, len(A)-1, k > len(A)-1) )
    
    return k > len(A) -1


def HasThreatInColumn(A, col_index_of_candidate_i, row_of_existing_queen_j):
    
    result = A[row_of_existing_queen_j] == col_index_of_candidate_i
    
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


def ThreatsAreFound(A, i, j, k):
    
    # TODO:  fix this to be the right CHECKS
    #print("ALERT - only checking for same row/col")
    
    return HasThreatInColumn(A, i, j) or HasThreatOnDiagonal(A, i, k, j)
    #return HasThreatInColumn(A, i, j)
    
        
    
def ConstructCandidates(A, k, S):
    Result = []
    
    print(S,"\tConstructCandidates()\t- for Queen in Row k =",k)
    
    # i is column...
    for i in range(1, len(A)):
        hasThreat = False
        
        print(S,"\t\tcolumn i=",i)
        
        # looking at ***PREVIOUSLY*** placed queens
        for j in range(1, k): # k-1):  this SHOULD be k, because the upper range is NOT inclusive

            print(S,"\t\t\tlooking at row j = ",j)
                
            # IF queen in row j has same column as i 
            # OR queens are in the same diagonal means delta row == delta column 
                        
            #if HasThreatInColumn(A, i, j) or HasThreatOnDiagonal(A, i, k, j):
            if ThreatsAreFound(A, i, j, k):
                hasThreat = True

            
            #if i == A[i] or abs(k-j) == abs(i-A[j]):
                #print("\t\tFound a threat...")
  
                
        if not hasThreat:

            Result.append(i)
        # else:
        #     print("\t\t\tBreak - experiment")
        #     break
            
            
    print("\n",S,"\t\tReturning Result = ",Result,"\n")
            
    return Result


def Process(A, k, S):
    print("S,\tProcess() - ")
    global count
    count = count + 1   # increment the number of solutions found!
    print(S,"\t\t==--- Solution Found ---== >>>>> ",A)
    global solutions
    #solutions.append(A)

    solutions.append(copy.copy(A))


def IsFinished():    
    # assuming we only want to return 1 result, otherwise always return False
    #return count > 0
    
    return False


def Backtrack(A, k, S):
    print("\n",S,"Backtrack(",A,", ",k,")")
          
    if IsSolution(A, k, S):
        Process(A, k, S)
    else:
        L = ConstructCandidates(A, k, S)
        
        for c in L:
            
            #if k+1 < len(A):
            A[k] = c
                #print("\t\tKeep going...!")

            S = S + "\t"
            Backtrack(A, k+1, S)
                
            # if IsFinished():
            #     return True
            # else:
            #     print("\tStill not done looking for a solution.\n")      
            

def Test_HasThreatInColumn():
    # def HasThreatInColumn(A, col_index_of_candidate_i, row_of_existing_queen_j):
    
    # k is the candidate queen... k in the A array is the candidate loctaion
    #       I THINK we're checking to see if that candidate IS a solution
    
    # A[j] == i ?

    A = [0, 0, 0, 0, 0]
    #for row in range(1,len(test)):
        # print("row (j?) =", row)
        # print(HasThreatInColumn(test, 2, row))
        
    # HasThreadInColumn(A, column of  , row of existing queen being checked (k-1))
    print(HasThreatInColumn(A, 1, 1))
    print(HasThreatInColumn(A, 2, 1))
    print(HasThreatInColumn(A, 3, 1))
    print(HasThreatInColumn(A, 4, 1))
    print(HasThreatInColumn(A, 5, 1))
    
    
    

def main():
    
    n = 4  # NOTE, n must be 4 or greater for the n-queens problem
 
    
    #return
    
    
    print("Hello! n =",n)
    
    A = [0] * (n+1)
    k = 0
    S = None # unused
    S = "" # using as spacing for now
    
    result = Backtrack(A, k, S)
    
    global solutions
    print("Set of all solutions =\n" + str(solutions))
    print("Number of possible solutions? ",len(solutions),"\n")
    


main()