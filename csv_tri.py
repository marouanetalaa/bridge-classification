import csv
import matplotlib.pyplot as plt
import numpy as np
l = []
i = 0
state = 'blank'
header = []
duration575 = []
duration595 = []
IArias = []
magn = []
dist = []
Vs30 = []
info = [duration575, duration595, IArias, magn, dist, Vs30]
index = [6, 7, 8, 12, 14, 16]
with open('searchResults.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        i += 1
        if i == 34:
            state = 'header'
            header = row
        if i > 34:
            if row == []:
                state = 'blank'
                break
            state = 'info'
            for k in range(len(info)):
                info[k].append(float(row[index[k]]))
avg = []
fig, axs = plt.subplots(2, 3)


"""axs[0, 1].plot(x, y, 'tab:orange')
axs[0, 1].set_title('Axis [0,1]')
axs[1, 0].plot(x, -y, 'tab:green')
axs[1, 0].set_title('Axis [1,0]')
axs[1, 1].plot(x, -y, 'tab:red')
axs[1, 1].set_title('Axis [1,1]')
for k in range (len(info)//2):
    for j in range (len(info)//2):
        axs[k, j].hist(info[k+j])
        axs[k, j].set_title(header[k+j])
plt.show()"""

axs[0, 0].hist(info[0], color='r')
axs[0, 0].set_title(header[index[0]])
axs[0, 1].hist(info[1], color='g')
axs[0, 1].set_title(header[index[1]])
axs[0, 2].hist(info[2], color='b')
axs[0, 2].set_title(header[index[2]])
axs[1, 0].hist(info[3], color='y')
axs[1, 0].set_title(header[index[3]])
axs[1, 1].hist(info[4], color='k')
axs[1, 1].set_title(header[index[4]])
axs[1, 2].hist(info[5], color='c')
axs[1, 2].set_title(header[index[5]])
plt.show()
