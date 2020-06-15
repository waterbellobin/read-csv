#%%
import os
import matplotlib.pyplot as plt
import csv

intensity = []
intensity_sec = []
intensity_sec_total = []
cyto2 = []
cyto = []
inten_total = []
cyto2_total = []
cyto_total = []
alphabet = []
i = 0
path = 'C:/Users/nosquest17/Desktop/Sujong/daily_works/20200602_GC_cyto_peaks/GC_v2_cyto_peak_4/'
files = os.listdir(path)

for file in files:
    #print(file)
    with open(path+file, 'rt', encoding='UTF8') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        intensity.clear()
        cyto2.clear()
        cyto.clear()
        intensity_sec.clear()
        for row in plots:
            intensity.append(row[1])
            cyto2.append(row[0])
    intensity.pop(0)
    cyto2.pop(0)
    for i in range(len(intensity)):
        intensity[i] = float(intensity[i])
        cyto2[i] = float(cyto2[i])
    
    index_1 = file.index("_")
    index_2 = file.index("_", index_1+1)
    
    print(file[index_1+1:index_2])
    alphabet.append(file[index_1+1:index_2])
    max_i = max(intensity)
    print(max_i)
    
    for n in range(len(intensity)):
        if intensity[n] == max_i:
            inten_total.append(intensity[n])
            cyto2_total.append(cyto2[n])
        
        if cyto2[n] >= 12000:
            intensity_sec.append(intensity[n])
            cyto.append(cyto2[n])
    
    max_s = max(intensity_sec)
    for m in range(len(intensity_sec)):
        if intensity_sec[m] == max_s:
            intensity_sec_total.append(intensity_sec[m])
            cyto_total.append(cyto[m])
    print(intensity_sec)

with open(path[0:70]+path[70:-1]+'.csv', mode = 'w', newline='', encoding='UTF8') as single_data_writer:
    total_data = csv.writer(single_data_writer, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    total_data.writerow(['Spot', 'max intensity', 'Cyto 2+', 'second inten', 'Cyto C'])
    for j in range(len(cyto2_total)):
        total_data.writerow([alphabet[j], inten_total[j], cyto2_total[j], intensity_sec_total[j], cyto_total[j]])