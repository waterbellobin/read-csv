import matplotlib.pyplot as plt
import csv

x = []
y1 = []
y2 = [1,2,331,2,2,1,1,1,2,1,2,2,2,2,2,2,2,2,2,2,2,2,22,2,2,2,1,1,1,2,2,1,1,2,2,21,321,321,321,3,213,21,421,4,14,1,412,4,124,21,421,421,4,214,21,421,421,4,214,21,421,421,3,2,2,2,32,32,3,232]
print(len(y2))
y3 = []
r = []

with open('C:/Users/nosquest17/Desktop/data.csv', 'rt', encoding='UTF8') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
        # print(type(row[0]))
        x.append(float(row[0]))
        y1.append(float(row[1]))

fig, ax = plt.subplots(figsize = (50,7))
ax.bar(x, y1, color = 'cyan')

#plt.xlabel('m/z')
#plt.ylabel('Intensity')
#plt.title('Baseline Correction')
#plt.xlim(0, 20000)
#plt.ylim(0, 5000)
plt.show()
#print(x)
#print(y1)
#plt.savefig('C:/Users/nosquest17/Desktop/graph')