#%%
import os
import re
import matplotlib.pyplot as plt
import csv
import numpy as np

cyto3_ref = 3637.8000
cyto2_ref = 6180.6200
cyto1_ref = 12360.2400

cyto3, cyto2, cyto1 = \
    ['cyto 3'],['cyto 2'],['cyto 1']

cyto3_cal, cyto2_cal, cyto1_cal\
    = [],[],[]
mz = []
alphabet = ['']

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [atoi(c) for c in re.split(r'(\d+)', text)]

i = 0
path = 'C:/Users/nosquest17/Desktop/Sujong/daily_works/'
folder = '20200626_GC_v1_cyto_test/GC_v1_200626_cyto_3/'
files = os.listdir(path+folder)
files.sort(key=natural_keys)

save_csv = 0

for file in files:
    #print(file)
    with open(path+folder+file, 'rt', encoding='UTF8') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        mz.clear()
        cyto3_cal.clear()
        cyto2_cal.clear()
        cyto1_cal.clear()
        
        for row in plots:
            mz.append(row[0])

    mz.pop(0)

    cyto3_cal, cyto2_cal, cyto1_cal \
        = [0]*len(mz), [0]*len(mz), [0]*len(mz)

    for i in range(len(mz)):
        mz[i] = float(mz[i])
        cyto3_cal[i] = mz[i] - cyto3_ref
        cyto2_cal[i] = mz[i] - cyto2_ref
        cyto1_cal[i] = mz[i] - cyto1_ref
        
    cyto3_err = min(cyto3_cal, key=abs)
    cyto2_err = min(cyto2_cal, key=abs)
    cyto1_err = min(cyto1_cal, key=abs)
    
    index_1 = file.index("_")
    index_2 = file.index("_", index_1+1)
    
    print(file[index_1+1:index_2])
    alphabet.append(file[index_1+1:index_2])

    cyto3.append(cyto1_err/cyto3_ref*1000000)
    cyto2.append(cyto2_err/cyto2_ref*1000000)
    cyto1.append(cyto3_err/cyto1_ref*1000000)
    
    print('')

file_index_1 = folder.index("/")
file_index_2 = folder.index("/", file_index_1+1)

print(folder[0:file_index_1+1])
print(folder[file_index_1+1:file_index_2])

if save_csv == True:
    with open(path+folder[0:file_index_1+1]+folder[file_index_1+1:file_index_2]+'.csv', mode = 'w', newline='', encoding='UTF8') as single_data_writer:
        total_data = csv.writer(single_data_writer, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        total_data.writerow(alphabet)
        total_data.writerow(cyto3)
        total_data.writerow(cyto2)
        total_data.writerow(cyto1)
        
    # for j in range(len(cyto2_total)):
    #     total_data.writerow([alphabet[j], inten_total[j], cyto2_total[j], intensity_sec_total[j], cyto_total[j]])

# %%
