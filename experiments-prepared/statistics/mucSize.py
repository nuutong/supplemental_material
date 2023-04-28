
import os
import csv

formulaNameList='processedformula.txt'
outFile = 'size_of_muc'
csvFile = 'mucSize.csv'
mucMax = 100  # can't get an uc

def countMUC(src_folder,list):
    for dirpath, dirnames, filenames in os.walk(src_folder):
        for file in filenames:
            fullname = dirpath + '/' + file
            flag = False
            with open(fullname) as file_obj:
                mucSize=0
                for line in file_obj:
                    if 'MUC' in line:
                        flag = True
                        MUC = next(file_obj)
                        while "LengthComp:" not in MUC and "The run time is" not in MUC:
                            mucSize = mucSize + 1
                            MUC = next(file_obj)
            if flag == False:
                mucSize = mucMax
            list.append(mucSize)


if(__name__=="__main__"):
    naive = []
    naiveuc = []
    binary = []
    binaryuc = []
    countMUC(r'./naive_res/log_res',naive)
    countMUC(r'./naiveuc_res/log_res',naiveuc)
    countMUC(r'./binary_res/log_res',binary)
    countMUC(r'./binaryuc_res/log_res',binaryuc)
    with open (formulaNameList, 'r') as f:
        formulas = f.readlines()

    with open(outFile, 'w') as f:
        for i in range(0, 1292):
            f.write(str(i + 1) + ' ' + str(naive[i]) + ' ' + str(naiveuc[i]) + ' ' + str(binary[i]) + ' ' + str(
                binaryuc[i])  + '\n')
        f.close()

    with open(csvFile, "a", newline='') as f:
        headers = ['formula', 'naive', 'naiveuc','binary','binaryuc']
        writer = csv.writer(f)
        writer.writerow(headers)
        for i in range (0,1292):
            row=[]
            row.append(formulas[i].split('/')[-1].strip())
            row.append(naive[i])
            row.append(naiveuc[i])
            row.append(binary[i])
            row.append(binaryuc[i])
            writer.writerow(row)
        f.close()
