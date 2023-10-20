##############将单端fasta中数据进行样本编号格式化为: >id.i(i会切换样本置零)
import os

path = "re_id/input/"

file_name_list = os.listdir(path)
try:
    os.listdir("re_id/otuput")
except FileNotFoundError:
    os.mkdir("re_id/otuput")

count = 1

for i in file_name_list:
    name = i[0:i.find('.')]   #截取名字
    file_path = path+i
    print(file_path)
    count += 1
    with open(file_path,'r',encoding="utf-8") as rf:  #某一文件文件
        lines = rf.readlines()
        new_file_name = "re_id/otuput/" + name + '.fasta'
        with open(new_file_name,'w',encoding="utf-8") as rw :
            prin = "开始生成第"+str(count-1)+"个文件"
            print(prin)
            at_line = 0
            sample_count = 1
            for ri in range(0,len(lines)):   #写入单个文件
                if ri == at_line:
                    tx = ">" + name+ "." + str(sample_count) + '\n'
                    sample_count += 1
                    tag = True
                    rw.write(tx)
                    add = ri + 1
                    # print(lines[ri])
                    # print(lines[ri].find('@D00236:386'))
                    # rw.write(ri)
                    while(tag):
                        rw.write(lines[add])

                        add += 1

                        fin = -1

                        try:
                            fin = lines[add].find('@')
                        except IndexError:
                            prind = "第"+str(count-1)+"个文件生成完毕"
                            print(prind)
                            tag = False

                        if fin !=-1:
                            tag = False
                            at_line = add



        rw.close()
    rf.close()

