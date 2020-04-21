import matplotlib.pyplot as plt
import csv

x = []
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []

with open('C:/Users/nosquest17/Desktop/Sujong/daily_works/20200401_post_processing_document/savitzky_2.csv', 'rt', encoding='UTF8') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
        x.append(float(row[0]))
        y1.append(float(row[1]))
        y2.append(float(row[4]))
        #y3.append(float(row[7]))
        #y4.append(float(row[10]))
        #y5.append(float(row[13]))
    

fig = plt.figure(figsize = (30,15))
plt.plot(x, y1, color = 'blue', linewidth = 1.2, label = 'Raw data')
plt.plot(x, y2, color = 'red', linestyle = '--', linewidth = 1, label = 'Window size 5')
#plt.plot(x, y3, color = 'deeppink', linewidth = 0.7, label = 'Window size 9')
#plt.plot(x, y4, color = 'lime', linewidth = 0.7, label = 'Window size 17')
#plt.plot(x, y5, color = 'red', linewidth = 0.7, label = 'Quartic window size 9')
plt.xlabel('m/z')
plt.ylabel('Intensity')
plt.title('Savitzky-Golay Smoothing')
plt.xlim(6000, 6500)
plt.ylim(0, 3000)
plt.legend(loc = 1, prop = {'size':15})
plt.show
plt.savefig('C:/Users/nosquest17/Desktop/Sujong/daily_works/20200401_post_processing_document/savitzky_5_2')