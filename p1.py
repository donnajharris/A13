# -----------------------------------------------------------
# p1.py
# -----------------------------------------------------------
# Donna Harris (harr2890)
# CP600 W22 - Assignment 13, Question 1
# -----------------------------------------------------------
# Question 1 is implementation only and cannot be executed.
# 
# See a13.pdf for more information.
# 
# -----------------------------------------------------------

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
    

def IsSolution(A, k, S):   
    pass
    
def ConstructCandidates(A, k, S):
    pass

def Process(A, k, S):
    pass

def IsFinished():    
    pass