#YOU ARE GIVEN TWO INTEGERS ARRAY, A AND B OF DIMENSIONS NXM. YOUR TASK IS TO PERFORM THE FOLLOWING OPERATIONS.
import numpy
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
A = numpy.array(l1)
B = numpy.array(l2)
print('ADDITION')
print(A+B)
print('SUBTRACTION')
print(A-B)
print('MULTIPLICATION')
print(A*B)
print('DIVISION')
print(A//B)
print('MODULUS')
print(A%B)
print('POWER')
print(A**B)