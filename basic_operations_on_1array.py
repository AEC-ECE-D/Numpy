import numpy as np
a=np.array([1,2,5,3])
print("adding 1 to every element:",a+1)
print("subtracting 3 to every element:",a-3)
print("multiplying to every element:",a*10)
print("squaring to every element:",a**2)
a*=2
print("doubled each element of original array:",a)
a=np.array([[1,2,3],[3,4,5],[9,6,0]])
print("\n original array:\n",a)
print("transpose of array:\n",a.T)
