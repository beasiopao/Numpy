import numpy as np
X = np.random.random((5,5))
print('X = ',X,'')
Z = (X - np.mean(X))/(np.std(X))
print("\nZ = ",Z,'')
np.save('X_normalized', Z)