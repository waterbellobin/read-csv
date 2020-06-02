import matplotlib.pyplot as plt
import csv
import numpy as np

x1 = []
y1 = []

origin_path = 'C:/Users/nosquest17/Desktop/Sujong/daily_works/20200601_GC_6402_Pico_flatness_repetition/'
file_name = 'GC_v2_flatness_6402_11'
save_fig = 1

with open(origin_path+file_name+'.csv', 'rt', encoding='UTF8') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
        x1.append(row[0])
        y1.append(row[2])
        
x1.pop(0)
y1.pop(0)
x1.insert(0, str(" "))
y1.insert(0, str(0))

for i in range(len(x1)):
    y1[i] = float(y1[i])
    
y1_max = max(y1[1:])
y1_min = min(y1[1:])
y_sub = round(y1_max - y1_min, 3)
y_sub = int(y_sub*1000)
y1_max = round(y1_max, 2)
y1_min = round(y1_min, 2)

fig = plt.figure(figsize = (15,5))

plt.bar(x1, y1, color = 'b', alpha = 1., width = 0.3)
plt.xlabel('spot', fontsize = 12)
plt.ylabel('flight time (μs)', fontsize = 12)
plt.xticks(rotation=90)
plt.yticks(np.arange(y1_min - 0.01, y1_max + 0.01, step = 0.005))
try_index = file_name.index("_", 18)
plt.title('Red Ink Flatness Test try '+file_name[try_index+1:]+' using GC '+ file_name[3:5]+ ' '+\
file_name[15:19]+' PicoScope', fontsize = 15)
plt.xlim(0, len(x1))
plt.ylim(y1_min - 0.01, y1_max + 0.01)
props = dict(boxstyle = 'round', facecolor = 'yellow', alpha = 1)
plt.text(len(x1)-12, y1_min-0.005,'max - min = '+str(y_sub)+'ns', fontsize = 16, fontweight = 'bold', bbox = props)
if save_fig == True:
    plt.savefig(origin_path+file_name)
plt.show()



