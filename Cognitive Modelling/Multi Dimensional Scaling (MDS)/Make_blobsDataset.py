import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.manifold import MDS

#Generate a sample dataset
X, _ = make_blobs(n_samples = 100, n_features = 3, centers = 2, random_state = 42)
print('Original Dimension of X = ', X.shape)

#Perform MDS to reduce the dimensionality to 2D
mds = MDS(n_components = 2, random_state = 42)
X_2d = mds.fit_transform(X)
print('Dimension of X after MDS = ', X_2d.shape)

#Plot the results
plt.scatter(X_2d[:,0], X_2d[:,1])
plt.title("MDS Visualiztion")
plt.xlabel("MDS Dimension 1")
plt.ylabel("MDS Dimension 2")
plt.show()