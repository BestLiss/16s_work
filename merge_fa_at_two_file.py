
##############双端合并
import os
import pandas as pd
metadata = pd.read_csv(r"./metadata.CSV",low_memory=False)
inputs = "merge/input/"
m = metadata.shape

count = 1

for i in range(0,m[0]):
    name = metadata.iloc[i,0]   #截取名字
    file_path1 = inputs + name + '_1'+'.fa'
    file_path2 = inputs + name + '_2'+'.fa'
    count += 1
    with open(file_path1,'r',encoding="utf-8") as rf1:  #正端文件
        lines1 = rf1.readlines()
        with open(file_path2, 'r', encoding="utf-8") as rf2:  # 反端文件
            lines2 = rf2.readlines()
        new_file_name = "merge/otuput" + name + '.fasta'
        with open(new_file_name,'w',encoding="utf-8") as rw :
            prin = "开始生成第"+str(count-1)+"个文件"
            print(prin)
            at_line = 0
            sample_count = 1


            # one = lines[0][15:16]
            # two = lines[2][15:16]

            # if one != two:   #判断是否为单端数据
            #     sig = True
            #     print(name+"为单端数据")
            for ri in range(0,len(lines1)):   #写入单个文件

                if ri == at_line:

                    l1 = lines1[ri]
                    l2 = lines2[ri]
                    if l1[l1.find('.') + 1:-1] == l2[l2.find('.') + 1:-1]:
                        tx = ">" + name + "." + str(sample_count) + '\n'
                        rw.write(tx)

                    sample_count += 1
                    tag = True

                    add = ri + 1



                    while(tag):

                        l1 = lines1[add - 1]
                        l2 = lines2[add - 1]
                        if l1[l1.find('.') + 1:-1] == l2[l2.find('.') + 1:-1]:
                            rw.write(lines1[add][0:-1] + lines2[add])

                        add += 1


                        fin = -1

                        try:
                            fin = lines1[add].find('>')

                        except IndexError:
                            prind = name+"生成完毕"
                            print(prind)
                            tag = False

                        if fin != -1:
                            tag = False
                            at_line = add



        rw.close()
    rf1.close()
    rf2.close()

