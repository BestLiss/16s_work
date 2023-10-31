##############将单端fasta中数据进行样本编号格式化为: >ASV_i(i不随样本切换置零)
import os

path = "toFasta/input/"

file_name_list = os.listdir(path)
count = 1
sample_count = 1

for i in file_name_list:
    name = i[0:i.find('.')]   #截取名字
    file_path = path+i
    count += 1
    with open(file_path,'r',encoding="utf-8") as rf:  #某一文件文件
        lines = rf.readlines()
        new_file_name = "merge/input/" + name + '.fa'
        with open(new_file_name,'w',encoding="utf-8") as rw :
            prin = "开始生成第"+str(count)+"个文件"
            print(prin)
            at_line = 0

            for ri in range(0,len(lines)):   #写入单个文件
                if ri == at_line:
                    tx = ">" + name+ '.' + str(sample_count) + '\n'
                    sample_count += 1
                    tag = True
                    rw.write(tx)
                    add = ri + 1
                    while(tag):
                        rw.write(lines[add])

                        add += 3

                        fin = -1

                        try:
                            fin = lines[add].find('@')
                        except IndexError:
                            prind = "第"+str(count)+"个文件生成完毕"
                            print(prind)
                            tag = False

                        if fin !=-1:
                            tag = False
                            at_line = add
        sample_count = 1


rw.close()
rf.close()

