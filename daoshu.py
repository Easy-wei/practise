import os


path = r'D:\data\3'

if os.path.isdir(path):
    print('aa')

#print(os.path.splitext(r'D:\data\3\power_date.zip')[-1])

a = os.listdir(path)
list_csv = []
def find_csv(path):
    for i in os.listdir(path):
        if os.path.isdir(path+'/'+i):
            find_csv(path+'/'+i)
        elif os.path.splitext(i)[-1]=='.csv':
            list_csv.append(path+i)
        else:
            pass
    return list(set(list_csv))


print(find_csv(path),'\n',len(find_csv(path)))