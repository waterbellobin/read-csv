#%%
import matplotlib.pyplot as plt
import csv
import numpy as np
import statistics
import math

x1 = []
y1 = []
y2 = []

origin_path = 'C:/Users/nosquest17/Desktop/Sujong/daily_works/20200601_GC_6402_Pico_flatness_repetition/'
file_name = 'GC_v1_flatness_6402_10'
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
    y2.append(y1[i])
y_med = statistics.median(y1)
#print(y2)

for j in range(len(x1)):
    y2[j] -= y_med
    y2[j] *= 1000
#print(y2)


y1_max = max(y1[1:])
y1_min = min(y1[1:])
# print(y1_max)
# print(y1_min)
print(y1_max - y1_min)

# print(statistics.median(y1))
# print(y1_max - statistics.median(y1))
# print(y1_min - statistics.median(y1))
y_sub = round(y1_max - y1_min, 4)
y_sub = float(y_sub*1000)
y_sub = format(y_sub, '.1f')
y1_max = round(y1_max - statistics.median(y1), 2)
y1_min = round(y1_min - statistics.median(y1), 2)

y2[0] = 0.0

fig = plt.figure(figsize = (15,5))

plt.bar(x1, y2, color = 'b', alpha = 1., width = 0.3)
plt.xlabel('spot', fontsize = 12)
plt.ylabel('flight time (ns)', fontsize = 12)
plt.xticks(rotation=90)
# plt.yticks(np.arange(math.floor(y1_min - 0.015), math.ceil(y1_max + 0.015), step = 0.005))
plt.yticks(np.arange(math.floor(y1_min - 0.015) * 1000, math.ceil(y1_max + 0.015) * 1000, step = 5))
plt.axhline(y = 0, linewidth = 0.5, color = 'black')
try_index = file_name.index("_", 18)
plt.title('Red Ink Flatness Test try '+file_name[try_index+1:]+' using GC '+ file_name[3:5]+ ' '+\
file_name[15:19]+' PicoScope', fontsize = 15)
plt.xlim(0, len(x1))
plt.ylim((y1_min - 0.011) * 1000, (y1_max + 0.011)* 1000)
props = dict(boxstyle = 'round', facecolor = 'yellow', alpha = 1)
plt.text(len(x1)-15, 1000*(y1_min - 0.008)+1.5,'median = '+str(round(y_med, 3))+'μs', fontsize = 20, fontweight = 'bold', bbox = props)
plt.text(len(x1)-15, 1000*(y1_min - 0.008)-1.5,'max - min = '+str(y_sub)+'ns', fontsize = 20, fontweight = 'bold', bbox = props)
if save_fig == True:
    plt.savefig(origin_path+file_name+'_zero_arrange_with_median')
plt.show()





# %%


# %%
