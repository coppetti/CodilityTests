# 1.1 BinaryGap
def binaryGap(N):
    return len(max(str("{0:b}".format(N)).split("1")))
    
# 2.1 CyclicRotation
def cyclicRotation(A, K):
    return A[-K:]+A[:-K]

# 2.2 OddsOccurence
def oddOccur(A):
   return [a for a in A if A.count(a)%2==1][0]
    
def main():
  binaryGap(15)
  cyclicRotation([3, 8, 9, 7, 6], 3) 
  oddsOccur([9, 3, 9, 3, 9, 7, 9])
