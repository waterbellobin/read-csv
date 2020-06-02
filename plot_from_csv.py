import matplotlib.pyplot as plt
import csv

x = []
y1 = []
y2 = []
y3 = []
r = []

with open('C:/Users/nosquest17/Desktop/Sujong/daily_works/20200401_post_processing_document/baseline_correction.csv', 'rt', encoding='UTF8') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
        # print(type(row[0]))
        x.append(float(row[0]))
        y1.append(float(row[1]))
        y2.append(float(row[8]))
        y3.append(float(row[9]))
        r.append(float(row[1]) - float(row[9]))

fig = plt.figure(figsize = (30,15))
plt.plot(x, y1, color = 'blue', linewidth = 1, label = 'Raw data')
#plt.plot(x, y2, color = 'green', linewidth = 1, label = 'Erosion')
#plt.plot(x, y3, color = 'deeppink', linewidth = 1.2, label = 'Dilation after erosion')
#plt.plot(x, r, color = 'blue', linewidth = 1, label = 'Baseline corrected result')
plt.xlabel('m/z')
plt.ylabel('Intensity')
plt.title('Baseline Correction')
plt.xlim(2000, 20000)
plt.ylim(0, 20000)
plt.legend(loc = 1, prop = {'size':15})
plt.show
#plt.savefig('C:/Users/nosquest17/Desktop/Sujong/daily_works/20200401_post_processing_document/raw_data')
plt.savefig('C:/Users/nosquest17/Desktop/figure')