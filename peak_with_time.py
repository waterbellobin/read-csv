#%%
import os
import matplotlib.pyplot as plt
import csv

intensity = []
time = []
inten_total = []
time_total = []
alphabet = []
i = 0
path = 'C:/Users/nosquest17/Desktop/Sujong/daily_works/20200707_GC_v2_Red_ink_flatness/'
folder = '20200706_Red_Ink_1/'

files = os.listdir(path+folder)

for file in files:
    #print(file)
    with open(path+folder+file, 'rt', encoding='UTF8') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        intensity.clear()
        time.clear()
        for row in plots:
            intensity.append(row[1])
            time.append(row[2])
    intensity.pop(0)
    time.pop(0)
    for i in range(len(intensity)):
        intensity[i] = float(intensity[i])
        time[i] = float(time[i])
    
    index_1 = file.index("_")
    index_2 = file.index("_", index_1+1)
    
    print(file[index_1+1:index_2])
    alphabet.append(file[index_1+1:index_2])
    max_i = max(intensity)
    print(max_i)
    for n in range(len(intensity)):
        if intensity[n] == max_i:
            inten_total.append(intensity[n])
            time_total.append(time[n])
            
#print(inten_total)
#print(len(inten_total))
with open(path+'example.csv', mode = 'w', newline='', encoding='UTF8') as single_data_writer:
    total_data = csv.writer(single_data_writer, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    total_data.writerow(['Spot', 'max intensity', 'time'])
    for j in range(len(time_total)):
        total_data.writerow([alphabet[j], inten_total[j], time_total[j]])

# %%
