#Libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

#Set initial params & generate initial configuration
Iterations = 100
Size = 800
A = np.random.randint(0,2,(Size,Size))
fig, ax = plt.subplots()
R = []
Z = np.zeros((Size,Size),dtype='int')

#Apply the rule sof life
for iter in range(Iterations):
  B = np.zeros((Size,Size),dtype='int')
  for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        try:
          if (i > 0) & (j > 0):
            B[i,j] += A[i+1,j] + A[i,j+1] + A[i,j-1] + A[i-1,j]
          elif (i == 0) & (j > 0):
            B[i,j] += A[i+1,j] + A[i,j+1] + A[i,j-1]
          elif (i > 0) & (j == 0):
            B[i,j] += A[i+1,j] + A[i,j+1] + A[i-1,j]
          elif (i == 0) & (j == 0):
            B[i,j] += A[i+1,j] + A[i,j+1]
        except IndexError:
          if (i < Size-1) & (j > Size-1):
            B[i,j] += A[i-1,j] + A[i,j-1] + A[i,j+1] + A[i+1,j]
          elif (i == Size-1) & (j < Size-1):
            B[i,j] += A[i-1,j] + A[i,j-1] + A[i,j+1]
          elif (i < Size-1) & (j == Size-1):
            B[i,j] += A[i-1,j] + A[i,j-1] + A[i+1,j]
          elif (i == Size-1) & (j == Size-1):
            B[i,j] += A[i-1,j] + A[i,j-1]

  Z = np.where(B == 3, 1,
      np.where(B < 3, A,
      np.where(B > 3, 0, A)))
  A = Z
  R.append(Z)

#Create an animation to see the whole process unfold
def animate(i):
  ax.clear()
  data = R[i]
  ax.imshow(data, cmap='Greys', interpolation='none')
  ax.set_xticks([])
  ax.set_yticks([])
  plt.show()

anim = FuncAnimation(fig, animate, frames = Iterations, interval = 1000)

#Save the animation in mp4 format
anim.save('test_anim.mp4', extra_args=['-vcodec', 'libx264'])
