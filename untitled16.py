#NAME=DIYA ROLL NO:21001003039

# performing matrix operations in python
# uou need import numpy for performing matrix operations
import numpy 
# Two matrices are initialized by value
x = numpy.array([[1, 2], [4, 5]])
y = numpy.array([[7, 8], [9, 10]])
print(x)
print(y)
#  add()is used to add matrices
print ("Addition of two matrices: ")
print (numpy.add(x,y))
# subtract()is used to subtract matrices
print ("Subtraction of two matrices : ")
print (numpy.subtract(x,y))
# divide()is used to divide matrices
print ("Matrix Division : ")
print (numpy.divide(x,y)) #elementwise division
print ("Multiplication of two matrices elementwise: ")
print (numpy.multiply(x,y)) #elementwise multiply
print ("Product of two matrices : ")
print (numpy.dot(x,y)) #normal matrix multiplication
print ("square root is : ")
print (numpy.sqrt(x)) # all elements are square rooted
print ("The summation of elements : ")
print (numpy.sum(y)) # sum all elements of matrix
print ("The column wise summation  : ")
print (numpy.sum(y,axis=0))
print ("The row wise summation: ")
print (numpy.sum(y,axis=1))
# using "T" to transpose the matrix
print ("Matrix transpose: ")
print (x.T)

