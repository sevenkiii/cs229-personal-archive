from matplotlib.image import imread, imsave
import matplotlib.pyplot as plt
import numpy as np

def dist(x, y):
    return np.sum((x - y) ** 2)

img = imread('../data/peppers-small.tiff').astype(np.float64)
K = 16

dat = img.reshape(-1, img.shape[-1])
m = dat.shape[0]

centroid = dat[np.random.choice(m, size=K, replace=False)]

bel = np.zeros(m)

eps = 1
it = 0
loss = 0
prev_loss = None
while it < 30 or prev_loss is None or abs(prev_loss - loss) >= eps:
    prev_loss = loss
    for i in range(m):
        for j in range(K):
            if dist(dat[i], centroid[j]) < dist(dat[i], centroid[int(bel[i])]):
                bel[i] = j
    for j in range(K):
        if np.sum(bel == j) > 0:
            centroid[j] = np.average(dat[bel == j], axis=0)
        else:
            centroid[j] = np.random.choice(m)
    it += 1
    loss = 0
    for i in range(m):
        loss += dist(dat[i], centroid[int(bel[i])])
    print("iter ", it, " | Loss = ", loss)
    
A = imread('../data/peppers-large.tiff')

for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        approx = 0
        for k in range(K):
            if dist(A[i][j], centroid[k]) < dist(A[i][j], centroid[approx]):
                approx = k
        A[i][j] = centroid[approx]

plt.imshow(A)
plt.show()

imsave('./output/p05_compressed.png', A)
