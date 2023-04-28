from datetime import time
import math
import csv
import pandas as pd


dataDir="./statistics/"
timeout=300000
a = open("naive.csv",'r')
Hlength=len(a.readlines())
#naive VS binary
data_x=pd.read_csv(filepath_or_buffer='binary.csv',sep=',',keep_default_na=False)["time(ms)"].values
data_y=pd.read_csv(filepath_or_buffer='naive.csv',sep=',',keep_default_na=False)["time(ms)"].values
output=open('data1',"w")
for i in range(0,Hlength-1):
      if(data_x[i]=='' or int(data_x[i])>timeout):
        data_x[i]=timeout
      if(data_y[i]=='' or int(data_y[i])>timeout):
        data_y[i]=timeout
      output.write(str(data_x[i]))
      output.write(' ')
      output.write(str(data_y[i]))
      output.write('\n')
output.close()

#naive VS naiveuc
data_x=pd.read_csv(filepath_or_buffer='naive.csv',sep=',',keep_default_na=False)["time(ms)"].values
data_y=pd.read_csv(filepath_or_buffer='naiveuc.csv',sep=',',keep_default_na=False)["time(ms)"].values
output=open('data2',"w")
for i in range(0,Hlength-1):
      if(data_x[i]=='' or int(data_x[i])>timeout):
        data_x[i]=timeout
      if(data_y[i]=='' or int(data_y[i])>timeout):
        data_y[i]=timeout
      output.write(str(data_x[i]))
      output.write(' ')
      output.write(str(data_y[i]))
      output.write('\n')
output.close()

#binary VS binaryuc
data_x=pd.read_csv(filepath_or_buffer='binary.csv',sep=',',keep_default_na=False)["time(ms)"].values
data_y=pd.read_csv(filepath_or_buffer='binaryuc.csv',sep=',',keep_default_na=False)["time(ms)"].values
output=open('data3',"w")
for i in range(0,Hlength-1):
      if(data_x[i]=='' or int(data_x[i])>timeout):
        data_x[i]=timeout
      if(data_y[i]=='' or int(data_y[i])>timeout):
        data_y[i]=timeout
      output.write(str(data_x[i]))
      output.write(' ')
      output.write(str(data_y[i]))
      output.write('\n')
output.close()

#naiveuc VS binary
data_x=pd.read_csv(filepath_or_buffer='naiveuc.csv',sep=',',keep_default_na=False)["time(ms)"].values
data_y=pd.read_csv(filepath_or_buffer='binary.csv',sep=',',keep_default_na=False)["time(ms)"].values
output=open('data4',"w")
for i in range(0,Hlength-1):
      if(data_x[i]=='' or int(data_x[i])>timeout):
        data_x[i]=timeout
      if(data_y[i]=='' or int(data_y[i])>timeout):
        data_y[i]=timeout
      output.write(str(data_x[i]))
      output.write(' ')
      output.write(str(data_y[i]))
      output.write('\n')
output.close()

#naive VS naiveuc VS binary VS binaryUC
data_n=pd.read_csv(filepath_or_buffer='naive.csv',sep=',', keep_default_na=False)["time(ms)"].values
data_nc=pd.read_csv(filepath_or_buffer='naiveuc.csv',sep=',', keep_default_na=False)["time(ms)"].values
data_b=pd.read_csv(filepath_or_buffer='binary.csv',sep=',', keep_default_na=False)["time(ms)"].values
data_bc=pd.read_csv(filepath_or_buffer='binaryuc.csv',sep=',', keep_default_na=False)["time(ms)"].values
output=open('data5',"w")
index = 1
data1 = data2 = data3 = data4 = data5 = data_best = 0
for i in range(0, Hlength-1):
    if(data_n[i] == '' or int(data_n[i])>timeout):
        data_n[i] = timeout
    if(data_nc[i] == '' or int(data_nc[i])>timeout):
        data_nc[i] = timeout
    if (data_b[i] == '' or int(data_b[i])>timeout):
        data_b[i] = timeout
    if(data_bc[i] == '' or int(data_bc[i])>timeout):
        data_bc[i] = timeout
    data1 = data1 + int(data_n[i])
    data2 = data2 + int(data_nc[i])
    data3 = data3 + int(data_b[i])
    data4 = data4 + int(data_bc[i])
    data5 = int(data_n[i])
    if(int(data_nc[i]) < data5):
        data5 = int(data_nc[i])
    if(int(data_b[i]) < data5):
        data5 = int(data_b[i])
    if(int(data_bc[i]) < data5):
        data5 = int(data_bc[i])
    data_best = data_best + data5
    output.write(str(index))
    output.write(' ')
    output.write(str(data1))
    output.write(' ')
    output.write(str(data2))
    output.write(' ')
    output.write(str(data3))
    output.write(' ')
    output.write(str(data4))
    output.write(' ')
    output.write(str(data_best))
    output.write('\n')
    index=index+1
output.close()

#binary VS binaryuc VS global
data_x=pd.read_csv(filepath_or_buffer='data6(sorted).csv',sep=',',keep_default_na=False)["binary"].values
data_y=pd.read_csv(filepath_or_buffer='data6(sorted).csv',sep=',',keep_default_na=False)["binaryuc"].values
data_z=pd.read_csv(filepath_or_buffer='data6(sorted).csv',sep=',',keep_default_na=False)["time(ms)"].values

output=open('data6',"w")
index=1
data1=data2=data3=data4=data_best=0
for i in range(0,Hlength-1):
      if(data_z[i]!=''):
        if(data_x[i]=='' or int(data_x[i])>timeout):
          data_x[i]=timeout
        if(data_y[i]==''or int(data_y[i])>timeout):
          data_y[i]=timeout
        data1= data1 + int(data_x[i])
        data2= data2 + int(data_y[i])
        data3= data3 + int(data_z[i])
        data_best = int(data_x[i])
        if(int(data_y[i]) < data_best):
            data_best = int(data_y[i])
        if(int(data_z[i]) < data_best):
            data_best = int(data_z[i])
        data4 = data4 + data_best
        output.write(str(index))
        output.write(' ')
        output.write(str(data1))
        output.write(' ')
        output.write(str(data2))
        output.write(' ')
        output.write(str(data3))
        output.write(' ')
        output.write(str(data4))
        output.write('\n')
        index=index+1
output.close()
