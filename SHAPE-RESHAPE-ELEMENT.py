import numpy
a,b = map(int,input("Enter the dimension of Matrix: ").split())
n = []
print("Elements of matrix: ")
for i in range(a):
    n.append(list(map(int,input().split())))
arr = numpy.array(n)
print(arr.reshape(b,a))