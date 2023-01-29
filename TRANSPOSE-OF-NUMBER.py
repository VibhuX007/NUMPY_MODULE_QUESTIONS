import numpy as np
n = int(input('Enter the size of matrix: '))
l = []
print("Enter the Matrix: ")
for i in range(n):
    l.append(list(map(int,input().split())))
a = np.array(l)
print("Transpose of Matrix: \n",a.transpose())
