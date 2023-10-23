###相同的tax有相同的fa

ref_path = "../id.txt"
tax_path = '../tax.txt'
database_path = "../../../silva_re.fa"

count = 1
sample_count = 1

ref_lines = open(ref_path, 'r', encoding='utf-8').readlines()
tax_lines = open(tax_path, 'r', encoding='utf-8').readlines()

database_lines = open(database_path, 'r', encoding='utf-8').readlines()


def run(star, end, tag):
    final_path = "./sub/sub" + tag + ".txt"

    with open(final_path, 'w', encoding="utf-8") as wf:
        same_fa = ''
        first_id = 1
        for i in range(star, end):
            star += 1
            print('线程' + tag + ':  ' + str(star) + '/' + str(end))

            if first_id == 1:

                for j in range(0, len(database_lines), 2):
                    try:

                        if database_lines[j][1:-1].find(tax_lines[i][0:-1]) != -1:
                            fa = ">"+ref_lines[i]
                            fa += database_lines[j + 1]
                            wf.write(fa)
                            same_fa = database_lines[j + 1]
                            break
                    except:
                        print("未找到")



            else:
                txt_s = '>' + ref_lines[i] + same_fa
                wf.write(txt_s)
            try:
                if tax_lines[i] == tax_lines[i + 1]:
                    first_id = 0
                else:
                    first_id = 1
            except:
                print("筛选完毕")
