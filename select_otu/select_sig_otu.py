###相同的tax有相同的fa

ref_path = "./tax.txt"
id_path = './id.txt'
database_path = "../../../silva_re.fa"

count = 1
sample_count = 1

ref_lines = open(ref_path, 'r', encoding='utf-8').readlines()
id_lines = open(id_path, 'r', encoding="utf-8").readlines()

database_lines = open(database_path, 'r', encoding='utf-8').readlines()


def run(star, end, tag):
    final_path = "./otus.fa"

    with open(final_path, 'w', encoding="utf-8") as wf:

        for i in range(star, end):
            star += 1
            print('线程' + tag + ':  ' + str(star) + '/' + str(end))

            for j in range(0, len(database_lines), 2):
                try:
                    if database_lines[j][1:-1].find(ref_lines[i][0:-1]) != -1:

                        fa = ">" + id_lines[i]
                        fa += database_lines[j + 1]
                        wf.write(fa)
                        break
                except:
                    print("未找到")




        print("筛选完毕!")


run(0, len(ref_lines), "1")
