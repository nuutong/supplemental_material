
import os
import csv

formulaNameList='processedformula.txt'
outFile = 'overlap_of_muc'
csvFile = 'mucSize.csv'

def getMUC(src_folder,list):
    for dirpath, dirnames, filenames in os.walk(src_folder):
        for file in filenames:
            muc=[]
            fullname = dirpath + '/' + file
            with open(fullname) as file_obj:
                for line in file_obj:
                    if 'MUC' in line:
                        MUC = next(file_obj)
                        while "LengthComp:" not in MUC and "The run time is" not in MUC:
                            muc.append(MUC.strip('\n'))
                            MUC = next(file_obj)
            list.append(muc)

def getOverlap(list1,list2,outFile):
    with open(outFile, 'w') as f:
        cnt0 = 0
        cnt1 = 0
        for i in range(0, 1292):
            M1 = list1[i]
            M2 = list2[i]
            overlap = 0
            for m in M1:
                if m in M2:
                    overlap = overlap + 1
            s = len(M1) + len(M2) - overlap
            if s != 0:
                index = round(overlap / s, 2)
            else:
                index = 1.0
            print(index)
            if (index == 0.0):
                cnt0 = cnt0 + 1
            if (index == 1.0):
                cnt1 = cnt1 + 1
            f.write(str(i + 1) + ' ' + str(index) + '\n')
        f.close()
        print(cnt0)
        print(cnt1)


if(__name__=="__main__"):
    binaryMUC = []
    binaryucMUC = []
    naiveucMUC = []
    getMUC(r'./binary_res/log_res',binaryMUC)
    getMUC(r'./binaryuc_res/log_res', binaryucMUC)
    getMUC(r'./naiveuc_res/log_res', naiveucMUC)
    getOverlap(binaryMUC,binaryucMUC,'overlap_binarymuc_binaryucmuc')
    getOverlap(binaryucMUC,naiveucMUC, 'overlap_naiveucmuc_binaryucmuc')
