#%%
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import csv
import numpy as np
import math

x1 = []
y1 = []
y2 = []
y3 = []
err1 = []
err2 = []
err_max = []
err_min = []

origin_path = 'C:/Users/nosquest17/Desktop/Sujong/daily_works/20200615_GC_v2_flatness_measurement/'
file_name = 'GC_v2_flatness_measurement'
save_fig = 0

with open(origin_path+file_name+'.csv', 'rt', encoding='UTF8') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
        x1.append(row[0])
        y1.append(row[1])
        y2.append(row[2])
        y3.append(row[3])
        
for i in range(len(x1)):
    y1[i] = float(y1[i])
    y2[i] = float(y2[i])
    y3[i] = float(y3[i])
    
fig = plt.figure(figsize = (15,5))

### divide two graphs
r1 = np.arange(len(x1))
r2 = [x - 0.3 for x in r1]
r3 = [x + 0.3 for x in r1]
plt.bar(r1, y1, color = 'r', alpha = 0.7, width = 0.2)
# plt.bar(r2, y2, color = 'b', alpha = 0.7, width = 0.2)
# plt.bar(r3, y3, color = 'g', alpha = 0.7, width = 0.2)
plt.xticks([r + 0.15 for r in range(len(x1))], x1, rotation=90)

plt.xlabel('spot', fontsize = 12)
plt.ylabel("Height from A0 (μm)", fontsize = 12)
# plt.yticks(np.arange(err_min_value, err_max_value + 100, step = 100))
plt.axhline(y = 0, linewidth = 0.5, color = 'black')
try_index = file_name.index("_", 11)
plt.title('Cytochrome C Error(ppm) Test try '+file_name[try_index+1:]+' using GC '+ file_name[3:5], fontsize = 15)
plt.xlim(0, len(x1))
# plt.ylim(err_min_value - 50, err_max_value + 50)
# patch1 = mpatches.Patch(color='r', alpha = 0.7,linewidth= 0.3, label = "Cytochrome C [M+2H]")
# patch2 = mpatches.Patch(color='b', alpha = 0.7, linewidth=0.3, label = "Cytochrome C")
# plt.legend(handles = [patch1, patch2], prop={'size':8})
if save_fig == True:
    plt.savefig(origin_path+file_name)
plt.show()






 # %%