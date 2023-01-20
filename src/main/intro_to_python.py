import numpy as np

arr = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
w, h = arr.shape

for i in range(h):
    for j in range(w):
        if i == j:
            arr[i][j] = 1

print(arr, "\n")

for i in range(h):
    for j in range(w):
        if i != j:
            arr[i][j] += 3

print(arr, "\n")

arr = np.delete(arr, 2, 1)

print(arr, "\n")
