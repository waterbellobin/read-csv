#%%
import os
import re
import matplotlib.pyplot as plt
import csv
import numpy as np

ams1_ref = 3637.8000
ams2_ref = 4364.9200
ams3_ref = 5381.4000
ams4_ref = 6255.4000
ams5_ref = 7274.5000
myo2_ref = 8476.6500
ams6_ref = 9740.8000
cyto_ref = 12361.1000
myo1_ref = 16952.3000

ams1, ams2, ams3, ams4, ams5, myo2, ams6, cyto, myo1 = \
    ['AMS 1'],['AMS 2'],['AMS 3'],['AMS 4'],['AMS 5'],['[Myoglobin+2H+]2+'],['AMS 6'],\
        ['[CytochromeC+H+]+'],['[Myoglobin+H+]+']
ams1_cal, ams2_cal, ams3_cal, ams4_cal, ams5_cal, ams6_cal, myo2_cal, myo1_cal, cyto_cal \
    = [],[],[],[],[],[],[],[],[]
mz = []
alphabet = ['']

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [atoi(c) for c in re.split(r'(\d+)', text)]

i = 0
path = 'C:/Users/nosquest17/Desktop/Sujong/daily_works/'
folder = '20200625_AMS_centroid_change/AMS_centroid_70_2/'
files = os.listdir(path+folder)
files.sort(key=natural_keys)

save_csv = True

for file in files:
    #print(file)
    with open(path+folder+file, 'rt', encoding='UTF8') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        # ams1.clear()
        # ams2.clear()
        # ams3.clear()
        # ams4.clear()
        # ams5.clear()
        # myo2.clear()
        # ams6.clear()
        # cyto.clear()
        # myo1.clear()
        mz.clear()
        ams1_cal.clear()
        ams2_cal.clear()
        ams3_cal.clear()
        ams4_cal.clear()
        ams5_cal.clear()
        myo2_cal.clear()
        ams6_cal.clear()
        cyto_cal.clear()
        myo1_cal.clear()
        
        for row in plots:
            mz.append(row[0])

    mz.pop(0)

    ams1_cal, ams2_cal, ams3_cal, ams4_cal, ams5_cal, ams6_cal, myo2_cal, myo1_cal, cyto_cal \
        = [0]*len(mz), [0]*len(mz), [0]*len(mz), [0]*len(mz), [0]*len(mz), [0]*len(mz), [0]*len(mz), [0]*len(mz), [0]*len(mz),

    for i in range(len(mz)):
        mz[i] = float(mz[i])
        ams1_cal[i] = mz[i] - ams1_ref
        ams2_cal[i] = mz[i] - ams2_ref
        ams3_cal[i] = mz[i] - ams3_ref
        ams4_cal[i] = mz[i] - ams4_ref
        ams5_cal[i] = mz[i] - ams5_ref
        myo2_cal[i] = mz[i] - myo2_ref
        ams6_cal[i] = mz[i] - ams6_ref
        cyto_cal[i] = mz[i] - cyto_ref
        myo1_cal[i] = mz[i] - myo1_ref
    
    ams1_err = min(ams1_cal, key=abs)
    ams2_err = min(ams2_cal, key=abs)
    ams3_err = min(ams3_cal, key=abs)
    ams4_err = min(ams4_cal, key=abs)
    ams5_err = min(ams5_cal, key=abs)
    myo2_err = min(myo2_cal, key=abs)
    ams6_err = min(ams6_cal, key=abs)
    cyto_err = min(cyto_cal, key=abs)
    myo1_err = min(myo1_cal, key=abs)

    index_1 = file.index("_")
    index_2 = file.index("_", index_1+1)
    
    print(file[index_1+1:index_2])
    alphabet.append(file[index_1+1:index_2])

    # print(ams1_err/ams1_ref*1000000)
    # print(ams2_err/ams2_ref*1000000)
    # print(ams3_err/ams3_ref*1000000)
    # print(ams4_err/ams4_ref*1000000)
    # print(ams5_err/ams5_ref*1000000)
    # print(myo2_err/myo2_ref*1000000)
    # print(ams6_err/ams6_ref*1000000)
    # print(cyto_err/cyto_ref*1000000)
    # print(myo1_err/myo1_ref*1000000)

    ams1.append(ams1_err/ams1_ref*1000000)
    ams2.append(ams2_err/ams2_ref*1000000)
    ams3.append(ams3_err/ams3_ref*1000000)
    ams4.append(ams4_err/ams4_ref*1000000)
    ams5.append(ams5_err/ams5_ref*1000000)
    myo2.append(myo2_err/myo2_ref*1000000)
    ams6.append(ams6_err/ams6_ref*1000000)
    cyto.append(cyto_err/cyto_ref*1000000)
    myo1.append(myo1_err/myo1_ref*1000000)

    print('')

file_index_1 = folder.index("/")
file_index_2 = folder.index("/", file_index_1+1)

print(folder[0:file_index_1+1])
print(folder[file_index_1+1:file_index_2])

if save_csv == True:
    with open(path+folder[0:file_index_1+1]+folder[file_index_1+1:file_index_2]+'.csv', mode = 'w', newline='', encoding='UTF8') as single_data_writer:
        total_data = csv.writer(single_data_writer, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        total_data.writerow(alphabet)
        total_data.writerow(ams1)
        total_data.writerow(ams2)
        total_data.writerow(ams3)
        total_data.writerow(ams4)
        total_data.writerow(ams5)
        total_data.writerow(myo2)
        total_data.writerow(ams6)
        total_data.writerow(cyto)
        total_data.writerow(myo1)
    # for j in range(len(cyto2_total)):
    #     total_data.writerow([alphabet[j], inten_total[j], cyto2_total[j], intensity_sec_total[j], cyto_total[j]])

# %%
