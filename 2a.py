import numpy as np

Fes = np.array([0,0,0,0,0])

sum = 0
Max = None
Min = None
for i in range(0,5):
      Fes[i] = input("숫자를 입력하세요")
      sum +=Fes[i]
for num in Fes:
    if (Max is None or num > Max):
        Max = num
for num in Fes:
    if (Min is None or num < Min):
        Min = num



print("받은 수는")
print(Fes)
print("받은 수의 합은")
print(sum)


print('최대값은 ', Max)
print('최소값은 ', Min)