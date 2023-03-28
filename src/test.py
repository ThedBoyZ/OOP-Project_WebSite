"""
A = [ [1,2], [1,1] ]
B = [ [0,1], [4,3] ]
C = []
for i in range (len(A)):
 C.append([0]*len(A[i]))
 for j in range (len(A)):
  C[i][j] = A[i][j] + B[i][j]
print(len(C)-len(C[1]))
"""
dog1 = []; dog2 = []
def cat(rat):
   for c1 in rat:
     d1 = d2 = c1[0]
     print("-",c1[0])
     for c2 in c1:
       print("+",c2)
       if d1>c2:
        d1 = c2
       elif d2<c2:
        d2 = c2
     dog1.append(d1); dog2.append(d2)
cat([[2,3],[4,-5],[0,1]])
print(dog1[1])