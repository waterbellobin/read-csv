import matplotlib.pyplot as plt
import csv

x1 = []
y1 = []
x2 = []
y2 = []
x3 = []
y3 = []

file_date = '200519'
file_name1 = 'c9'
file_name2 = 'b9'
file_name3 = 'a9'
save_fig = 0

x_lim_min = 2500
x_lim_max = 13800

if save_fig == 0:
    x_lim_min = 2500
    x_lim_max = 13000
    



with open('C:/Users/nosquest17/Desktop/Sujong/daily_works/20200520_GC_Micro_ID/\
'+file_date+'_peak_list/'+file_name1+'.csv', 'rt', encoding='UTF8') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
        # print(type(row[0]))
        x1.append(row[0])
        y1.append(row[1])
        #x.append(float(row[0]))
        #y1.append(float(row[1]))
with open('C:/Users/nosquest17/Desktop/Sujong/daily_works/20200520_GC_Micro_ID/\
'+file_date+'_peak_list/'+file_name2+'.csv', 'rt', encoding='UTF8') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
        # print(type(row[0]))
        x2.append(row[0])
        y2.append(row[1])
with open('C:/Users/nosquest17/Desktop/Sujong/daily_works/20200520_GC_Micro_ID/\
'+file_date+'_peak_list/'+file_name3+'.csv', 'rt', encoding='UTF8') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
        # print(type(row[0]))
        x3.append(row[0])
        y3.append(row[1])
x1.pop(0)
y1.pop(0)
x2.pop(0)
y2.pop(0)
x3.pop(0)
y3.pop(0)
for i in range(len(x1)):
    x1[i] = float(x1[i])
    y1[i] = float(y1[i])
    x2[i] = float(x2[i])
    y2[i] = float(y2[i])
    x3[i] = float(x3[i])
    y3[i] = float(y3[i])
    
y1_max = max(y1)
y2_max = max(y2)
y3_max = max(y3)

for j in range(len(y1)):
    y1[j] = y1[j]/y1_max
for n in range(len(y2)):
    y2[n] = y2[n]/y2_max
for m in range(len(y3)):
    y3[m] = y3[m]/y3_max
    
if save_fig == True:
    fig = plt.figure(figsize = (20,7))
else:
    fig = plt.figure(figsize = (20,10))

plt.bar(x1, y1, color = 'r', alpha = 0.4, width = 20)
#plt.bar(x2, y2, color = 'b', alpha = 0.4, width = 20)
plt.bar(x3, y3, color = 'g', alpha = 0.4, width = 20)
plt.xlabel('m/z', fontsize = 12)
plt.ylabel('Intensity', fontsize = 12)
#plt.title('Spot '+file_name.capitalize()+' Peak List', fontsize = 15)
plt.xlim(x_lim_min, x_lim_max)
plt.ylim(0, 1.1)
#plt.text(x_lim_min + (x_lim_max-x_lim_min)*(0.75), 1, 'Maximum Intensity: '+str(round(y_max, 4)), fontsize = 15)
#if save_fig == True:
    #plt.savefig('C:/Users/nosquest17/Desktop/'+file_date+'_'+file_name.capitalize())
plt.savefig('C:/Users/nosquest17/Desktop/example')
plt.show()
#print(x)
#print(y1)





