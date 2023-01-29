#YOU ARE GIVEN A NXM INTEGER ARRAY MATRIX WITH 
# SPACE SEPARATED ELEMENTS (N=ROWS AND M=COLUMNS). YOUR TASK IS TO PRINT THE TRANSPOSE AND FLATTEN RESULTS.
import numpy
m, n = list(map(int, input().split()))
l = []
for i in range(m):
    l.append(list(map(int, input().split())))
a = numpy.array(l)
tr = numpy.transpose(a)
ft = numpy.ndarray.flatten(a)
print(tr)
print(ft)