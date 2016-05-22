# 1.1 BinaryGap
def binaryGap(N):
    return len(max(str("{0:b}".format(N)).split("1")))
    
# 2.1 CyclicRotation
def cyclicRotation(A, K):
    return A[-K:]+A[:-K]
    
    
def main():
  binaryGap(15)
  cyclicRotation([3, 8, 9, 7, 6], 3) 
