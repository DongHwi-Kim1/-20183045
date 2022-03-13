
import numpy as np

A = np.array([[2,5],
             [1,3],
             [4,1]])

B = np.array([[4,-1],
              [2,3],
              [6,2]])

C = np.array([[1,2,2],
            [3,4,5]])  

        

print("Mtr(A)+ Mtr(B)")
print(A+B)

print("Mtr(B)-Mtr(A)")
print(B-A)

print("Mtr(B) X Mtr(C)")
print(B.dot(C))

print("Mtr(C) X Mtr(A)")
print(C.dot(A))
