import numpy
a,b = map(int,input("Enter the dimension of Matrix: ").split())
n = []
print("Elements of first matrix: ")
for i in range(a):
    n.append(list(map(int,input().split())))
a1 = numpy.array(n)
c,d = map(int,input("Enter the dimension of Matrix: ").split())
m = []
print("Elements of second matrix: ")
for i in range(c):
    m.append(list(map(int,input().split())))
a2 = numpy.array(m)
print("Product of Matrix: ")
print(numpy.dot(a1,a2))