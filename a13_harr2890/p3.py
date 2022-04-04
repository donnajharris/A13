# -----------------------------------------------------------
# p3.py
# -----------------------------------------------------------
# Donna Harris (harr2890)
# CP600 W22 - Assignment 13, Question 3
# -----------------------------------------------------------
# Question 3 can be demonstrated by running:
#    $ python3 p3.py
# 
# See a13.pdf for more information and analysis of results.
#
# The main() code is at the bottom of the file.
# 
# -----------------------------------------------------------

import copy

PRINT_ON = False   # toggles the printing of the in-progress statements (excluding table print)

# globals
solution_count = 0
recursive_call_count = 0

def ResetGlobals():
   global solution_count
   solution_count = 0
   
   global recursive_call_count
   recursive_call_count = 0
    

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
   if PRINT_ON:
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
         global recursive_call_count
         recursive_call_count += 1
         Backtrack(A, k+1, S)
               
         if IsFinished():
               return True   
   
   
##############################################
#  Question 3 code for running test cases
#     and displaying results
#
def Solve_N_Queens(n):
       ResetGlobals()
   
       if PRINT_ON:
              print("\nTrying to neutrally place",n,"queens on a",n,"x",n,"board.\n")

       A = [0] * (n+1)
       k = 1
       S = None # unused

       Backtrack(A, k, S)

       if PRINT_ON:
              print("\n",solution_count,"solutions exist for the " + str(n) + "-Queens problem.")  

       return solution_count, recursive_call_count     


def PrintResultsSummary(results):       
       print("\n%4s %12s  %22s" % ("n","solutions","recursive calls made"))
       print("%4s %12s  %22s" % ("--","----------","--------------------"))
       
       for result in results:
              print("%4s %12s %22s" % (result[0],result[1][0],result[1][1]))
       
       print("\n")


def main():
       table_results = []
       table_results.append((8, Solve_N_Queens(8)))
       table_results.append((10, Solve_N_Queens(10)))
       table_results.append((12,Solve_N_Queens(12)))
       
       PrintResultsSummary(table_results)
   
   
main()