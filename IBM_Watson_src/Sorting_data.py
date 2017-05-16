import csv
import os
import matplotlib.pyplot as plt
from shutil import copyfile
import shutil



melanoma = []
NOTmelanoma = []
remainder = []

f = open('ISIC-2017_Training_Part3_GroundTruth.csv')
csv_f = csv.reader(f)

for row in csv_f:
    if row[1] == "1.0":
        melanoma.append(row)
    elif row[2] == "1.0":
            NOTmelanoma.append(row)
    elif ((row[2] == "1.0") and (row[1] == "1.0")):
            print "WTF!!"
    else:
        remainder.append(row)
        
'''
for file in melanoma:
    folderName = '/home/zuhayr/BU/EC500J1/Project/Dataset/M_pos_SK_neg'
    fileName = '/home/zuhayr/BU/EC500J1/Project/Dataset/ISIC-2017_Training_Data/'+ file[0] +'.jpg'
    shutil.copy(fileName, folderName)   
'''
'''    
for file in NOTmelanoma:
    folderName = '/home/zuhayr/BU/EC500J1/Project/Dataset/M_neg_SK_pos'
    fileName = '/home/zuhayr/BU/EC500J1/Project/Dataset/ISIC-2017_Training_Data/'+ file[0] +'.jpg'
    shutil.copy(fileName, folderName) 
'''
    
remainder.pop(0)


for file in remainder:
    folderName = '/home/zuhayr/BU/EC500J1/Project/Dataset/M_neg_SK_neg'
    fileName = '/home/zuhayr/BU/EC500J1/Project/Dataset/ISIC-2017_Training_Data/'+ file[0] +'.jpg'
    shutil.copy(fileName, folderName) 