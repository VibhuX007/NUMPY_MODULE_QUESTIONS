#YOU ARE GIVEN A SPACE SEPARATED LIST OF NUMBERS. 
# YOUR TASK IS TO PRINT A REVERSED NUMPY ARRAY WITH THE ELEMENTS TYPE FLOAT.
import numpy
arr = list(map(int, input().split()))
a = numpy.array(arr,float)
print(numpy.flip(a))