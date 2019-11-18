import numpy as np
X = np.linspace(1,100,100)
X.resize(10,10)
A = np.int64(np.square(X))
mod = A%3
div3 = A[mod==0]
print('Given the array A which is equivalent to:')
print('A = ',A,'')
print('\nElements in A that are disvisible by 3 are:')
print('div3 = ',div3,'')
np.save('div_by_3', div3)
