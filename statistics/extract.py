import csv
import os

benckmarks=[]

#with uc
def write_csv(file_name, headers,src_folder):
    data=[]
    for dirpath, dirnames, filenames in os.walk(src_folder):
        for file in filenames:
            fullname=dirpath+'/'+file
            row=[]
            muc=[]
            ucLength=[]
            flag=False
            row.append(file)
            with open(fullname) as file_obj:
                line=file_obj.readline()
                while line:
                    if 'MUC' in line:
                        while(line):
                            line=file_obj.readline()
                            if 'LengthComp' in line:
                                row.append(muc)
                                while (line):
                                    line = file_obj.readline()
                                    if 'run time' in line:
                                        row.append(line.split(":")[1][:-3])
                                        break
                                break
                                # while(line):
                                #     line=file_obj.readline()
                                #     if 'run time' in line:
                                #         row.append(ucLength)
                                #         row.append(line.split(":")[1][:-3])
                                #         break
                                #     ucLength.append(line.strip('\n'))
                                # break
                            else:
                                if 'run time' in line:
                                    row.append(muc)
                                    row.append(line.split(":")[1][:-3])
                                    break
                            muc.append(line.strip('\n'))

                    # if 'SAT' in line:
                    #     row.append(line.split(":")[1].strip('\n'))
                    # if 'UCValid' in line:
                    #     row.append(line.split(":")[1].strip('\n'))
                    # if 'UCInvalid' in line:
                    #     row.append(line.split(":")[1].strip('\n'))
                    # if 'UCSatTime' in line:
                    #     row.append(line.split(":")[1][:-3].strip('\n'))
                    # if line.split(":")[0]== "UC":
                    #     row.append(line.split(":")[1].strip('\n'))
                    line=file_obj.readline()
            data.append(row)
    with open(file_name, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for r in data:
            writer.writerow(r)
        f.close()       

#without uc
def write_csv2(file_name, headers,src_folder):
    data=[]
    for dirpath, dirnames, filenames in os.walk(src_folder):
        for file in filenames:
            fullname=dirpath+'/'+file
            row=[]
            muc=[]
            flag=False
            row.append(file)
            with open(fullname) as file_obj:
                line=file_obj.readline()
                while line:
                    if 'MUC' in line:
                        while(line):
                            line=file_obj.readline()
                            if 'run time' in line:
                                row.append(muc)
                                row.append(line.split(":")[1][:-3])
                                break
                            muc.append(line.strip('\n'))
                    # if 'SAT' in line:
                    #     row.append(line.split(":")[1].strip('\n'))
                    # if 'UC' in line:
                    #     row.append(line.split(":")[1].strip('\n'))
                    line=file_obj.readline()
            data.append(row)
    with open(file_name, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for r in data:
            writer.writerow(r)
        f.close()       

#global
globalFormulas=[]
def write_csv3(file_name, headers,src_folder):
    for dirpath, dirnames, filenames in os.walk(r'./naive_res/log_res'):
        for file in filenames:
            benckmarks.append(file)
    data=[]
    for dirpath, dirnames, filenames in os.walk(src_folder):
        for file in filenames:
            globalFormulas.append(file)

    for i in range(0,len(benckmarks)):
        row = []
        muc = []
        row.append(benckmarks[i])
        if(benckmarks[i] in globalFormulas):
            flag = False
            solvetime = 0
            fullname = dirpath + '/' + benckmarks[i]
            with open(fullname) as file_obj:
                line = file_obj.readline()
                while line:
                    if 'MUC' in line:
                        while (line):
                            line = file_obj.readline()
                            if 'run time' in line:
                                row.append(muc)
                                if flag == False:
                                    solvetime = line.split(":")[1][:-3]
                                break
                            muc.append(line.strip('\n'))
                    if 'run time of muser2' in line:
                        flag = True
                        solvetime = line.split(":")[1][:-3]
                    line = file_obj.readline()
                row.append(solvetime)
        else:
            row.append(muc)
        data.append(row)
    # for dirpath, dirnames, filenames in os.walk(src_folder):
    #     for file in filenames:
    #         fullname=dirpath+'/'+file
    #         row=[]
    #         muc=[]
    #         flag=False
    #         row.append(file)
    #         with open(fullname) as file_obj:
    #             line=file_obj.readline()
    #             while line:
    #                 if 'global' in line:
    #                     flag=True
    #                 if 'MUC' in line:
    #                     while(line):
    #                         line=file_obj.readline()
    #                         if 'run time' in line:
    #                             row.append(muc)
    #                             row.append(line.split(":")[1][:-3])
    #                             break
    #                         muc.append(line.strip('\n'))
    #                 line=file_obj.readline()
    #         if flag==False:
    #             row=[]
    #         data.append(row)
    with open(file_name, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for r in data:
            writer.writerow(r)
        f.close()

if(__name__=="__main__"):
    file_name="./naive.csv"
    # headers = ['formula','SAT times','SAT for UC','MUC','time(ms)']
    headers = ['formula', 'MUC', 'time(ms)']
    src_folder = r'./naive_res/log_res'
    write_csv2(file_name, headers,src_folder)

    # headers = ['formula','SAT times','SAT for UC','UCValid','UCInvalid','UCSatTime(ms)','MUC' ,'LengthComp','time(ms)']
    headers = ['formula', 'MUC', 'time(ms)']
    file_name='./naiveuc.csv'
    src_folder = r'./naiveuc_res/log_res'
    write_csv(file_name, headers,src_folder)

    # headers = ['formula','SAT times','SAT for UC','MUC','time(ms)']
    headers = ['formula', 'MUC', 'time(ms)']
    file_name='./binary.csv'
    src_folder = r'./binary_res/log_res'
    write_csv2(file_name, headers,src_folder)

    # headers = ['formula','SAT times','SAT for UC','UCValid','UCInvalid','UCSatTime(ms)','MUC' ,'LengthComp','time(ms)']
    headers = ['formula', 'MUC', 'time(ms)']
    file_name='./binaryuc.csv'
    src_folder = r'./binaryuc_res/log_res'
    write_csv(file_name, headers,src_folder)

    headers = ['formula','MUC','time(ms)']
    file_name='./global.csv'
    src_folder = r'./global_res/log_res'
    write_csv3(file_name, headers,src_folder)

