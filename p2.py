# p2.py


import math

count = 0

'''
Use your Backtrack algorithm to solve the n-queens problem in Python, 

by providing appropriate implementation for the IsSolution, ConstructCandidates, Process and IsFinished  functions

'''


# From Lesson 13 - Backtracking


'''

Input:
	A : queen i, is placed in row i and column A[i]
	k:  number of queens placed so far
	S : set of input values, (not used)

def IsSolution(A, k, S)
1. return k > Length(A)	# each queen is placed without conflict 
      and we do not use array index 0

def ConstructCandidates(A, k, S)
1. Result = []		# empty array, will contain the column 
                        indexes where the k-th queen has no threat
2. for i = 1 to Length(A):	# try each column i in row k
3.   hasThreat = False
4.   for j = 1 to k-1:	# check all the previously placed queen in rows 1 to k-1
5.     if i == A[i] 	# if queen ir row j has same column as i	
         or abs(k-j) == abs(i-A[j): # or, queens are in the same diagonal means delta row 
	    (i.e., abs(k-j)) == delta column (i.e., abs(i-A[j])
6.     hasThreat = True # queen [k, i] and [j, A[j]] are in same column or diagonal
7.   if not hasThreat:
8.     Result.Append(i)
9. return Result

def Process(A, k, S)
1. global count = count + 1	# Count the number of solution in a global variable count. 
                  used by IsFinished callback
2. Print(A)

def IsFinished()
1. return count > 0		# Assuming we want to find any one solution

'''

def IsSolution(A, k, S):
    
    print("\tIsSolution() where k =", k, " is greater than the LENGTH of A =", A[1:len(A)], "? {0}\n".format(k > len(A)-1) )
    
    return k > len(A)-1

def ConstructCandidates(A, k, S):
    Result = []
    
    print("\tConstructCandidates()")
    #print("\t- for Queen",k)
    
    for i in range(1, len(A)):
        hasThreat = False
        
        #print("\t\ti=",i)
        
        for j in range(1, k-1):  
            #print("\t\t\tj=",j)
    
            # IF queen in row j has same column as i 
            # OR queens are in the same diagonal means delta row == delta column 
            if j == A[i] or abs(k-j) == abs(i-A[j]):
                #print("\t\t\t\t{0} == {1} OR abs({3}-{2}) == abs({0}-{4})".format(i, A[i], j, k, A[j]))
                hasThreat = True
                
        if not hasThreat:
            #print("\t\t\tQueen {0} offers no threat to Queen {1}.".format(i,k))
            Result.append(i)
            
            
    print("\n\t\tCC is returning Result = ",Result,"\n")
            
    return Result


def Process(A, k, S):
    print("\tProcess() - showing that we've been doing the work.")
    global count
    count = count + 1
    print("\t\tA ==--- Solution ---== >>>>> ",A)


def IsFinished():
    print("\tIsFinished() - Is count ({0}) > 0? {1}".format(count, count > 0))
    return count > 0


'''

def Backtrack(A, k, S)
	Input:
		A : Current partial candidate solution 
		k:  Current position in A
		S : set of input values
1. if IsSolution(A, k, S):
2.    Process(A, k, S)
3. else:
4.    L = ConstructCandidates(A, k, S)
5.    for each candidate c in L:
6.       a[k+1] = c
7.       Backtrack(A, k+1, S)
8.       if Finished():
9.          return

'''
def Backtrack(A, k, S):
    print("\nBacktrack(",A[1:len(A)],", ",k,")")
          
    if IsSolution(A, k, S):
        Process(A, k, S)
    else:
        L = ConstructCandidates(A, k, S)
        
        for c in L:
            
            print("\t\tc =",c," and len(A) is = " + str(len(A)) + " and k is = " + str(k))
            
            if k+1 < len(A):
                A[k+1] = c
            Backtrack(A, k+1, S)
                
            if IsFinished():
                return            
            

def main():
    
    n = 4   # NOTE, n must be 4 or greater for the n-queens problem
    
    print("Hello! n =",n)
    
    A = [0] * (n+1)
    k = 0
    S = None # unused
    
    result = Backtrack(A, k, S)
    


main()