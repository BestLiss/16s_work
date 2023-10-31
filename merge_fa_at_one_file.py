##############双端合并
import os

path = "merge/input/"

file_name_list = os.listdir(path)
count = 1

for i in file_name_list:
    name = i[0:i.find('.')]   #截取名字
    file_path = path+i
    count += 1
    with open(file_path,'r',encoding="utf-8") as rf:  #某一文件文件
        lines = rf.readlines()
        new_file_name = "merge/otuput/" + name + '.fasta'
        with open(new_file_name,'w',encoding="utf-8") as rw :
            prin = "开始生成第"+str(count-1)+"个文件"
            print(prin)
            at_line = 0
            sample_count = 1
            sig = False

            one = lines[0][15:16]
            two = lines[2][15:16]

            if one != two:   #判断是否为单端数据
                sig = True
                print(name+"为单端数据")
            for ri in range(0,len(lines)):   #写入单个文件

                if ri == at_line:
                    if lines[at_line].find('length=0') == -1 : #不打印空行
                        tx = ">" + name+ "." + str(sample_count) + '\n'
                        rw.write(tx)
                    sample_count += 1
                    tag = True

                    add = ri + 1



                    while(tag):
                        if sig :
                            if lines[add-1].find('length=0') == -1 :  #不打印空行
                                rw.write(lines[add])
                            add += 1
                        else:
                            fa = lines[add][0:-1]+lines[add+2][0:-1]+'\n'  #正端切40，反端切37
                            # fa = lines[add][0:-1] + lines[add + 2]
                            rw.write(fa)

                            add += 3

                        fin = -1

                        try:
                            fin = lines[add].find('@')

                        except IndexError:
                            prind = name+"生成完毕"
                            print(prind)
                            tag = False

                        if fin != -1:
                            tag = False
                            at_line = add
            sample_count = 0


        rw.close()
    rf.close()

