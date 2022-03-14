import numpy as np

A = np.array([[2,3,4],
             [4,8,2],
             [1,2,1]])

AT = A.T
a = [0,1,2,3]
TT=0
print("A는 대칭행렬인가?")

"""
for i in range(0,4):

    for j in range(0,4):

        if A[i][j]==AT[i][j]:
          pass
          else:
          print("false")
          break


"""
print(A==AT)
