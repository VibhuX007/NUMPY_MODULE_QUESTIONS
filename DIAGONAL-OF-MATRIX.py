#YOUR TASK IS TO PRINT AN ARRAY OF SIZE NXM WITH ITS MAIN DIAGONAL ELEMENTS AS 1'S AND 0'S EVERYWHERE ELSE.
import numpy as np
n = int(input("Enter the size of matrix: "))
l= []
print("Enter the Matrix: ")
for i in range(n):
    l.append(list(map(int,input().split())))
a = np.array(l)
print("Diagonal elements are: ")
print(a.diagonal())