import numpy as np
from tkinter import filedialog

path = filedialog.askopenfilename(title="Choose a CSV file", filetypes=[("CSV Files", "*.csv")])
data = np.loadtxt(path, delimiter=',', skiprows=1)

size = np.size(data)
average = np.sum(data) / size
orda = np.sort(data)
mid = len(orda)

if mid % 2 == 0:
    median = (orda[mid // 2 - 1] + orda[mid // 2]) / 2
else:
    median = orda[mid // 2]

frequency = {}

for i in orda:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

mode = None
higher_frequency = 0

for i, cont in frequency.items():
    if cont > higher_frequency:
        higher_frequency = cont
        mode = i

print(median)
print(average)
print(mode)