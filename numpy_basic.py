import numpy as np
x=np.zeros(10)
print(x)


import numpy as np
a=np.zeros(10)
print("fifth value to one")
a[4]=1
print(a)


import numpy as np
z=np.arange(10,50)
print(z)


import numpy as np
b=np.arange(0,9).reshape(3,3)
print(b)


import numpy as np
nz=np.nonzero([1,2,0,0,4,0])
print(nz)


import numpy as np
y=np.eye(3)
print(y)


import numpy as np
c=np.ones((5,5))
print("1 0n border and 0 inside ")
c[1:-1,1:-1]=0
print(c)


import numpy as np
c=np.ones((5,5))
print("0 on border and 1 inside the array")
c=np.pad(c, pad_width=1, mode='constant', constant_values=0)
print(c)

import numpy as np
T=np.ones((4,2))
S=np.zeros((4,2))
print("concatenate array equal=")
print(np.concatenate([T,S],axis=1))


