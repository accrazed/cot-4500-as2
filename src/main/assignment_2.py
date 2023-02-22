import numpy as np
np.set_printoptions(precision=7, suppress=True, linewidth=100)

# 1

xx = [3.6, 3.8, 3.9]
yy = [1.675, 1.436, 1.318]
w = 3.7

nev = [[0 for _ in range(len(xx))] for _ in range(len(xx))]

for x in range(len(xx)):
    nev[x][0] = yy[x]

for x in range(1, len(xx)):
    for y in range(1, x + 1):
        a = (w - xx[x - y]) * nev[x][y - 1]
        b = (w - xx[x]) * nev[x - 1][y - 1]

        nev[x][y] = (a - b) / (xx[x] - xx[x - y])


print(nev[2][2])
print()

# 2

xx = [7.2, 7.4, 7.5, 7.6]
yy = [23.5492, 25.3913, 26.8224, 27.4589]

dif = [[0 for _ in range(len(xx))] for _ in range(len(xx))]

for x in range(len(xx)):
    dif[x][0] = yy[x]

for x in range(1, len(xx)):
    for y in range(1, x + 1):
        a = dif[x][y - 1] - dif[x - 1][y - 1]
        b = xx[x] - xx[x - y]
        dif[x][y] = a / b

diag = np.diag(dif).tolist()
print(diag[1:])
print()

# 3

x = 7.3
val = 0
for x in range(len(xx)):
    mlt = diag[x]
    for y in range(x):
        mlt *= x - xx[y]
    val += mlt

print(val)
print()

# 4

xx = [3.6, 3.8, 3.9]
yy = [1.675, 1.436, 1.318]
uu = np.repeat(xx, 2)
mm = [-1.195, -1.188, -1.182]

zl = len(uu)

dif = np.zeros((zl, zl))
dif[:, 0] = np.repeat(yy, 2)

for x in range(1, zl):
    if x % 2 == 0:
        a = (dif[x][0] - dif[x-1][0])
        b = (uu[x] - uu[x-1])
        dif[x][1] = a / b
    else:
        dif[x][1] = mm[x//2]

for x in range(2, zl):
    for y in range(2, x + 1):
        a = dif[x][y - 1] - dif[x - 1][y - 1]
        b = uu[x] - uu[x - y]
        dif[x][y] = a / b

for i in range(len(dif)):
    np.insert(dif, 0, uu[i])

res = np.delete(dif, -1, axis=1)
print(np.array(res))
print()

# 5

xx = [2, 5, 8, 10]
yy = [3, 5, 7, 9]

xl = len(xx)-1

hh = []
for i in range(xl):
    hh.append(xx[i+1]-xx[i])

aa = []
for i in range(1, xl):
    a = (3 / hh[i]) * (yy[i+1] - yy[i])
    b = (3 / hh[i-1]) * (yy[i] - yy[i-1])
    aa.append(a-b)

ll = [1]
uu = [0]
zz = [0]

for i in range(1, xl):
    ll.append(2 * (xx[i+1] - xx[i-1]) - (hh[i-1] * uu[i-1]))
    uu.append(hh[i] / ll[i])
    zz.append((aa[i-1] - hh[i-1] * zz[i-1]) / ll[i])

ll.append(1)
zz.append(0)
cc = [0 for _ in range(xl+1)]
bb = [0 for _ in range(xl)]
dd = [0 for _ in range(xl)]

for j in reversed(range(xl)):
    cc[j] = zz[j] - (uu[j] * cc[j+1])
    bb[j] = ((yy[j+1] - yy[j]) / hh[j]) - (hh[j] * (cc[j+1] + 2 * cc[j]) / 3)
    dd[j] = (cc[j+1] - cc[j]) / (3 * hh[j])

A = np.zeros((xl+1, xl+1))
for i in range(0, xl-1):
    A[i+1][i] = hh[i]
    A[i+1][i+1] = 2 * (hh[i] + hh[i+1])
    A[i+1][i+2] = hh[i+1]

A[0][0] = 1
A[-1][-1] = 1

print(A)
print()

b = aa
b.insert(0, 0)
b.append(0)

print(np.float64(b))
print()

print(np.float64(cc))
print()
