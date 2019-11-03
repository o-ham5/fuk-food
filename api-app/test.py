import numpy as np
from sklearn.preprocessing import StandardScaler

data = np.array([
    [4, 5, 6, 8],
    [2, 5, 8, 2],
    [5, 2, 8, 4]
])

scaler = StandardScaler()
scaler.fit(data)
data = scaler.transform(data)

print(data)
