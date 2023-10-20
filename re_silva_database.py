##############将单端fasta中数据进行样本编号格式化为: >ASV_i(i不随样本切换置零)
import os

path = "./re_silva/input/"

file_name_list = os.listdir(path)

try:
    os.listdir("re_silva/otuput")
except FileNotFoundError:
    os.mkdir("re_silva/otuput")

count = 1
sample_count = 1

for i in file_name_list:

    file_path = path+i
    count += 1
    with open(file_path,'r',encoding="utf-8") as rf:  #某一文件文件
        lines = rf.readlines()
        new_file_name = "re_silva/otuput/silva_re.fa"
        with open(new_file_name,'w',encoding="utf-8") as rw :
            prin = "开始生成第"+str(count-1)+"个文件"
            print(prin)
            at_line = 0

            for ri in range(0,len(lines)):   #写入单个文件

                if ri == at_line:
                    tx = lines[ri]
                    rw.write(tx)
                    sample_count += 1
                    tag = True
                    add = ri + 1
                    fa = ''
                    while(tag):
                        fa+=lines[add][0:-1]

                        add += 1

                        fin = -1

                        try:
                            fin = lines[add].find('>')
                        except IndexError:
                            prind = "第"+str(count-1)+"个文件生成完毕"
                            print(prind)
                            tag = False

                        if fin !=-1:
                            tag = False
                            at_line = add
                    rw.write(fa+'\n')


rw.close()
rf.close()

