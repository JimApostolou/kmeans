import random
f = open('dataset.txt','w')
totalpoints = int(input('Give me the amount of points you want : '))
f.write(str(totalpoints)+'\n')
for i in range(totalpoints*2):
    x = str(random.uniform(-1000, 1000))+'\n'
    f.write(x)
f.close()