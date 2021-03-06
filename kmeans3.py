import random as r
import math as m
from matplotlib import pyplot as plt
import numpy as np

p = []
c = []
thesi = []

profile = open("dataset.txt", "r")
points = int(profile.readline())
centroids = 10
while centroids > 8:
    centroids = int(input("Give me the centroids you want: "))
    if centroids > 8:
        print('The limit is 8 centroids')
dimensions = 2
for i in range(points):
    k = []
    for j in range(dimensions):
        num = float(profile.readline())
        k.append(num)
    p.append(k)
profile.close()
for i in range(centroids):
    k = []
    for j in range(dimensions):
        num = round(r.uniform(-100, 100), 2)
        k.append(num)
    c.append(k)
for i in range(points):
    sum = 0.0
    for j in range(dimensions):
        sum += (p[i][j]-c[0][j])**2
    min = m.sqrt(sum)
    minthesi = 0
    for j in range(1, centroids):
        sum = 0.0
        for k in range(dimensions):
            sum += (p[i][k]-c[j][k])**2
        if min > m.sqrt(sum):
            min = m.sqrt(sum)
            minthesi = j
    thesi.append(minthesi)
flag = 0
while flag == 0:
    count = 0
    for i in range(centroids):
        for j in range(dimensions):
            sin = 0
            sum = 0.0
            for k in range(points):
                if i == thesi[k]:
                    sum += p[k][j]
                    sin += 1
            if sin != 0:
                if sum/sin == c[i][j]:
                    count += 1
                c[i][j] = sum/sin
            else:
                count += 1
    for i in range(points):
        sum = 0.0
        for j in range(dimensions):
            sum += (p[i][j] - c[0][j]) ** 2
        min = m.sqrt(sum)
        minthesi = 0
        for j in range(1, centroids):
            sum = 0.0
            for k in range(dimensions):
                sum += (p[i][k] - c[j][k]) ** 2
            if min > m.sqrt(sum):
                min = m.sqrt(sum)
                minthesi = j
        thesi[i] = minthesi
    if count == centroids*dimensions:
        flag = 1
for i in range(len(c)):
    plt.scatter(c[i][0], c[i][1], color='black')
colors = ['red', 'yellow', 'blue', 'green',
          'purple', 'orange', 'brown', 'pink']
for i in range(len(thesi)):
    for j in range(centroids):
        if thesi[i] == j:
            plt.scatter(p[i][0], p[i][1], color=colors[j])
plt.show()
