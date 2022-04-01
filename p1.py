# p1.py

'''
Implement the generic Backtrack algorithm from the lesson note in Python.

??? Question -- what am I backtracking?

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