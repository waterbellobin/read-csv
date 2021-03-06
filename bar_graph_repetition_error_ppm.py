#%%
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import csv
import numpy as np
import math

x1 = []
y1 = []
y2 = []
err1 = []
err2 = []
err_max = []
err_min = []

origin_path = 'C:/Users/nosquest17/Desktop/Sujong/daily_works/20200602_GC_cyto_peaks/'
file_name = 'GC_v2_cyto_peak_1'
save_fig = 0

with open(origin_path+file_name+'.csv', 'rt', encoding='UTF8') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
        x1.append(row[0])
        y1.append(row[2])
        y2.append(row[4])
        
x1.pop(0)
y1.pop(0)
y2.pop(0)
#x1.insert(0, str(" "))
#y1.insert(0, str(0))
#y2.insert(0, str(0))

for i in range(len(x1)):
    y1[i] = float(y1[i])
    y2[i] = float(y2[i])
    err1.append(0)
    err2.append(0)
    
for j in range(len(x1)):
    err1[j] = (y1[j]-6180.6200)/6180.6200 * 1000000
    err2[j] = (y2[j]-12360.2400)/12360.2400 * 1000000

for n in range(len(err1)):
    err_max.append(err1[n])
    err_max.append(err2[n])
    err_min.append(err1[n])
    err_min.append(err2[n])

err_max_value = max(err_max)
print(err_max_value)
err_max_value = math.ceil(err_max_value/100)
err_max_value *= 100
print(err_max_value)
err_min_value = min(err_min)
print(err_min_value)
err_min_value = math.floor(err_min_value/100)
err_min_value *= 100
print(err_min_value)

fig = plt.figure(figsize = (15,5))

# ### overlap two graphs
# plt.bar(x1, err1, color = 'b', alpha = 0.5, width = 0.3)
# plt.bar(x1, err2, color = 'r', alpha = 0.5, width = 0.3)
# plt.xticks(rotation = 90)

### divide two graphs
r1 = np.arange(len(x1))
r2 = [x + 0.3 for x in r1]
r3 = [x + 0.3 for x in r2]
plt.bar(r1, err1, color = 'r', alpha = 0.7, width = 0.3)
plt.bar(r2, err2, color = 'b', alpha = 0.7, width = 0.3)
plt.xticks([r + 0.15 for r in range(len(x1))], x1, rotation=90)


plt.xlabel('spot', fontsize = 12)
plt.ylabel('Error(ppm)', fontsize = 12)
plt.yticks(np.arange(err_min_value, err_max_value + 100, step = 100))
plt.axhline(y = 0, linewidth = 0.5, color = 'black')
try_index = file_name.index("_", 11)
plt.title('Cytochrome C Error(ppm) Test try '+file_name[try_index+1:]+' using GC '+ file_name[3:5], fontsize = 15)
plt.xlim(0, len(x1))
plt.ylim(err_min_value - 50, err_max_value + 50)
patch1 = mpatches.Patch(color='r', alpha = 0.7,linewidth= 0.3, label = "Cytochrome C [M+2H]")
patch2 = mpatches.Patch(color='b', alpha = 0.7, linewidth=0.3, label = "Cytochrome C")
plt.legend(handles = [patch1, patch2], prop={'size':8})
if save_fig == True:
    plt.savefig(origin_path+file_name)
plt.show()






# %%