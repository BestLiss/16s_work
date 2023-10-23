###相同的tax有相同的fa


id_path = './id.txt'
all_g_id_path =  './all_g_id.txt'
database_path = "../../../all_otus.sintax"

count = 1
sample_count = 1

id_lines = open(id_path, 'r', encoding="utf-8").readlines()
all_g_id = open(all_g_id_path,'r',encoding="utf-8").readlines()
database_lines = open(database_path, 'r', encoding='utf-8').readlines()


def run(star, end, tag):
    final_path = "./all_sintax.txt"

    with open(final_path, 'w', encoding="utf-8") as wf:

        for i in range(star, end):
            star += 1
            print('线程' + tag + ':  ' + str(star) + '/' + str(end))



            for j in range(0, len(all_g_id)):

                if  id_lines[i][0:-1] == all_g_id[j][0:-1]:

                    fa = database_lines[j]
                    # print(fa)
                    wf.write(fa)
                    break

        print("筛选完毕!")


run(0, len(id_lines), "1")
