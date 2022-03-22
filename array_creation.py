import numpy as np
c=np.zeros((3,4))
print("\n AN array intialized with all zeros:\n",c)
e=np.random.random((2,2))
print("\n a random array:\n",e)
f=np.arange(0,30,5)
print("\n sequential array with steps of 5:\n",f)
g=np.linspace(0,5,10)
print("\n sequential array with 10 values between 0 and 5 :\n" ,g)
#reshaping 3*4 array as 2*2*3 array
arr=np.array([[1,2,3,4],[5,2,4,2],[1,2,0,1]])
newarr=arr.reshape(2,2,3)
print("\n original array:\n",arr)
print("\n reshaped array:\n",newarr)
