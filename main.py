# 1.1 BinaryGap
def binaryGap(N):
    return len(max(str("{0:b}".format(N)).split("1")))
   
    
# 2.1 CyclicRotation
def cyclicRotation(A, K):
    return A[-K:]+A[:-K]


# 2.2 OddsOccurence
def oddOccur(A):
   return [a for a in A if A.count(a)%2==1][0]
   
   
# 3.1 FrogJmp
def frogJmp(X, Y, D):
    return [(Y-X)/D if (Y-X)%D==0 else ((Y-X)/D)+1][0]


# 3.2 TapeEquilibrium
def tapeEq(A):def solution(A):
    min = max(A)
    for i in range(len(A)):
        min = abs(sum(A[i:])-sum(A[:i])) if abs(sum(A[i:])-sum(A[:i]))<min else min
    return min
    
    
# 3.3 PermMissingElem
def permMissingElem(A):
    A.sort()
    return [A[i]-1 for i in range(len(A)) if A[i]<>i+1][0]
    

print "BinaryGap: ",binaryGap(15)
print "CyclicRotation: ",cyclicRotation([3, 8, 9, 7, 6], 3) 
print "OddsOccurence: ",oddsOccur([9, 3, 9, 3, 9, 7, 9])
print "FrogJmp: ",frogJmp(10,85,30)
print "TapeEquilibrium: ",tapeEq([3, 1, 2, 4, 3])
print "PermMissingElem: ",permMissingElem([2, 1, 4, 5])
