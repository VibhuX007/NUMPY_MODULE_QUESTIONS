import numpy
a,b = map(int,input("Enter the dimension of Matrix: ").split())
n = []
print("Elements of first matrix: ")
for i in range(a):
    n.append(list(map(int,input().split())))
arr = numpy.array(n)
print("Max element: ",numpy.max(arr))
print("Min element: ",numpy.min(arr))