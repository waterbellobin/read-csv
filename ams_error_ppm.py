#%%
import os
import matplotlib.pyplot as plt
import csv
import numpy as np

intensity = []
intensity_sec = []
intensity_sec_total = []
cyto2 = []
cyto = []
inten_total = []
cyto2_total = []
cyto_total = []
alphabet = []

ams1_ref = 3637.8000
ams2_ref = 4364.9200
ams3_ref = 5381.4000
ams4_ref = 6255.4000
ams5_ref = 7274.5000
myo2_ref = 8476.6500
ams6_ref = 9740.8000
cyto_ref = 12361.1000
myo1_ref = 16952.3000

ams1, ams2, ams3, ams4, ams5, ams6, myo2, myo1, cyto = [],[],[],[],[],[],[],[],[]
ams1_cal, ams2_cal, ams3_cal, ams4_cal, ams5_cal, ams6_cal, myo2_cal, myo1_cal, cyto_cal \
    = [],[],[],[],[],[],[],[],[]
mz = []

i = 0
path = 'C:/Users/nosquest17/Desktop/Sujong/daily_works/20200617_AMS_error_ppm/20200617_AMS_error_ppm_ex/'
files = os.listdir(path)

for file in files:
    #print(file)
    with open(path+file, 'rt', encoding='UTF8') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        ams1.clear()
        ams2.clear()
        ams3.clear()
        ams4.clear()
        ams5.clear()
        myo2.clear()
        ams6.clear()
        cyto.clear()
        myo1.clear()
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
    
    ams1_err_abs = min(np.abs(ams1_cal))
    ams2_err_abs = min(np.abs(ams2_cal))
    ams3_err_abs = min(np.abs(ams3_cal))
    ams4_err_abs = min(np.abs(ams4_cal))
    ams5_err_abs = min(np.abs(ams5_cal))
    myo2_err_abs = min(np.abs(myo2_cal))
    ams6_err_abs = min(np.abs(ams6_cal))
    cyto_err_abs = min(np.abs(cyto_cal))
    myo1_err_abs = min(np.abs(myo1_cal))
    
    if ams1_err_abs == min(ams1_cal):
        ams1_err = ams1_err_abs
    else:
        ams1_err = ams1_err_abs * (-1)

    if ams2_err_abs == min(ams2_cal):
        ams2_err = ams2_err_abs
    else:
        ams2_err = ams2_err_abs * (-1)

    if ams3_err_abs == min(ams3_cal):
        ams3_err = ams3_err_abs
    else:
        ams3_err = ams3_err_abs * (-1)

    if ams4_err_abs == min(ams4_cal):
        ams4_err = ams4_err_abs
    else:
        ams4_err = ams4_err_abs * (-1)

    if ams5_err_abs == min(ams5_cal):
        ams5_err = ams5_err_abs
    else:
        ams5_err = ams5_err_abs * (-1)

    if myo2_err_abs == min(myo2_cal):
        myo2_err = myo2_err_abs
    else:
        myo2_err = myo2_err_abs * (-1)

    if ams6_err_abs == min(ams6_cal):
        ams6_err = ams6_err_abs
    else:
        ams6_err = ams6_err_abs * (-1)

    if cyto_err_abs == min(cyto_cal):
        cyto_err = cyto_err_abs
    else:
        cyto_err = cyto_err_abs * (-1)

    if myo1_err_abs == min(myo1_cal):
        myo1_err = myo1_err_abs
    else:
        myo1_err = myo1_err_abs * (-1)

    print(ams1_err/ams1_ref*1000000)
    print(ams2_err/ams2_ref*1000000)
    print(ams3_err/ams3_ref*1000000)
    print(ams4_err/ams4_ref*1000000)
    print(ams5_err/ams5_ref*1000000)
    print(myo2_err/myo2_ref*1000000)
    print(ams6_err/ams6_ref*1000000)
    print(cyto_err/cyto_ref*1000000)
    print(myo1_err/myo1_ref*1000000)
    # index_1 = file.index("_")
    # index_2 = file.index("_", index_1+1)
    
    # print(file[index_1+1:index_2])
    # alphabet.append(file[index_1+1:index_2])
    # max_i = max(intensity)
    # print(max_i)
    



#     for n in range(len(mz)):
#         if intensity[n] == max_i:
#             inten_total.append(intensity[n])
#             cyto2_total.append(cyto2[n])
        
#         if cyto2[n] >= 12000:
#             intensity_sec.append(intensity[n])
#             cyto.append(cyto2[n])
    
#     max_s = max(intensity_sec)
#     for m in range(len(intensity_sec)):
#         if intensity_sec[m] == max_s:
#             intensity_sec_total.append(intensity_sec[m])
#             cyto_total.append(cyto[m])
#     print(intensity_sec)

# with open(path[0:70]+path[70:-1]+'.csv', mode = 'w', newline='', encoding='UTF8') as single_data_writer:
#     total_data = csv.writer(single_data_writer, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     total_data.writerow(['Spot', 'max intensity', 'Cyto 2+', 'second inten', 'Cyto C'])
#     for j in range(len(cyto2_total)):
#         total_data.writerow([alphabet[j], inten_total[j], cyto2_total[j], intensity_sec_total[j], cyto_total[j]])

# %%
