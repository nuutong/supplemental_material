import csv
import os

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
                                while(line):
                                    line=file_obj.readline()
                                    if 'run time' in line:
                                        row.append(ucLength)
                                        row.append(line.split(":")[1][:-3])
                                        break
                                    ucLength.append(line.strip('\n'))
                                break
                            muc.append(line.strip('\n'))
                    if 'SAT' in line:
                        row.append(line.split(":")[1].strip('\n'))
                    if 'UCValid' in line:
                        row.append(line.split(":")[1].strip('\n'))
                    if 'UCInvalid' in line:
                        row.append(line.split(":")[1].strip('\n'))
                    if 'UCSatTime' in line:
                        row.append(line.split(":")[1][:-3].strip('\n'))
                    if line.split(":")[0]== "UC":
                        row.append(line.split(":")[1].strip('\n'))
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
                    if 'SAT' in line:
                        row.append(line.split(":")[1].strip('\n'))
                    if 'UC' in line:
                        row.append(line.split(":")[1].strip('\n'))
                    line=file_obj.readline()
            data.append(row)
    with open(file_name, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for r in data:
            writer.writerow(r)
        f.close()       

#global
def write_csv3(file_name, headers,src_folder):
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
                    if 'global' in line:
                        flag=True
                    if 'MUC' in line:
                        while(line):
                            line=file_obj.readline()
                            if 'run time' in line:
                                row.append(muc)
                                row.append(line.split(":")[1][:-3])
                                break
                            muc.append(line.strip('\n'))
                    line=file_obj.readline()
            if flag==False:
                row=[]
            data.append(row)
    with open(file_name, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for r in data:
            writer.writerow(r)
        f.close()

if(__name__=="__main__"):
    file_name="./naive.csv"
    headers = ['formula','SAT times','SAT for UC','MUC','time(ms)']
    src_folder = r'./naive_res/log_res'
    write_csv2(file_name, headers,src_folder)

    headers = ['formula','SAT times','SAT for UC','UCValid','UCInvalid','UCSatTime(ms)','MUC' ,'LengthComp','time(ms)']
    file_name='./naiveuc.csv'
    src_folder = r'./naiveuc_res/log_res'
    write_csv(file_name, headers,src_folder)

    headers = ['formula','SAT times','SAT for UC','MUC','time(ms)']
    file_name='./binary.csv'
    src_folder = r'./binary_res/log_res'
    write_csv2(file_name, headers,src_folder)

    headers = ['formula','SAT times','SAT for UC','UCValid','UCInvalid','UCSatTime(ms)','MUC' ,'LengthComp','time(ms)']
    file_name='./binaryuc.csv'
    src_folder = r'./binaryuc_res/log_res'
    write_csv(file_name, headers,src_folder)

    headers = ['formula' ,'MUC','time(ms)']
    file_name='./global.csv'
    src_folder = r'./global_res/log_res'
    write_csv3(file_name, headers,src_folder)

