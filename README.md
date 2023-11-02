# 16s_unifiy
Identification of intestinal microbiota  biomarkers in centenarians based on machine learning
#### 一、 从NCBI下载样本fasta格式文件或在ENA下载fastq格式文件后解压

#### 二（可选）、 双端合并（NCBI的fasta文件双端序列都在一个文件中，若从NCBI上下载的fasta格式文件请执行此步骤）
1. 在代码执行目录创建merge/input和merge/output文件夹,并将待处理的文件放入merge/input 
2. python执行merge_fa_at_one_file.py
3. 将会在merge/otuput目录下输出结果 
4. cat merge/otuput/*.fa > ASV.fa
#### 二（可选）、合并ENA双端fastq数据文件（若从ENA上下载的fastq格式文件请执行此步骤）
1. 在代码执行目录创建toFasta/input、merge/input、merge/output文件夹，将metadata.CSV（第一列为样本编号）放入代码执行目录,并将待处理的文件放入toFasta/input
2. 运行fastq_to_fasta.py
3. 将会在merge/input生成文件fasta文件
4. 运行merge_fa_at_two_file.py
5. 将会在merge/output生成合并完成的文件
6. cat merge/otuput/*.fa > ASV.fa
#### 三、 格式化silva_16s_v123
1. [下载silva数据库:https://www.drive5.com/usearch/manual/sintax_downloads.html](https://www.drive5.com/usearch/manual/sintax_downloads.html)
2. 在代码执行目录创建re_silva/input文件夹,并将silva_16s_v123.fa放入re_silva/input \
3. 将会在re_silva/output目录下输出结果
#### 四、 使用vsearch鉴定物种
1. 创建conda环境:vsearch 安装并激活\
`conda creat -n vsearch -y python=2.7` \
`conda activate vsearch`
2. 使用vsearch进行物种注释,分类水平可信度大于0.6 \
`vsearch --sintax ASV.fa --db  ./rdp_16s_v16.fa --tabbedout ./otus_all.sintax --sintax_cutoff 0.6 `
#### 五、处理注释文件otus_all.sintax 
1. 去除空行 \
`awk '{if($2!="") print $0}' otus_all.sintax > handle/trim.txt`
2. 获取所有鉴定到g的注释行,输出第一列和第四列并将'\t'替换为',' \
`awk '/g:/&&!/s:/' handle/trim.txt > handle/g/g.txt`  \
`awk -F '\t' -v n=2 '{print $1,$4}'  handle/g/g.txt > handle/g/g_1_4.txt` \
`awk '/g:/' handle/g/g_1_4.txt > handle/g/g_1_4+.txt` \
`sed -i 's/\s/,/g' handle/g/g_1_4+.txt` 
3. 获得所有鉴定到s的注释行并去除s列 \
`awk '/s:/' handle/trim.txt > handle/s/s.txt` \
`awk -v n=2 '{print $1,$4}'  handle/s/s.txt >  handle/s/s_1_4.txt` \
`awk '/s:/' handle/s/s_1_4.txt > handle/s/s_1_4+.txt` \
`sed -i 's/\s/,/g' handle/s/s_1_4+.txt` \
`awk -F ',' -v n=6 '{print $1,$2,$3,$4,$5,$6}'  handle/s/s_1_4+.txt >  handle/s/s_1_4_delete_s.txt`
`sed -i 's/\s/,/g' handle/s/s_1_4_delete_s.txt` 
4. 合并被鉴定到s去除了s的注释 \
`cat handle/g/g_1_4+.txt handle/s/s_1_4_delete_s.txt > all_g.txt`
5. 将相同的注释排成相邻行
`sort -k2 -t\t all_g.txt > handle/sort.txt`
#### 六、序列统一化 \
1. 生成序列id \
`awk -F ',' -v n=1 '{print $1}'  handle/all_g.txt >  handle/g/id.txt`
2. 生成序列的注释文件 \
`awk -F ',' -v n=6 '{print $2,$3,$4,$5,$6,$7}'  handle/all_g.txt >  handle/g/tax.txt` \
`sed -i 's/\s/,/g' handle/g/tax.txt`
3. 查看id.txt总行数
`wc -l handle/g/id.txt`
4. 设置find_g_fa/config.py
`config.threads=进程数  congfig.divide_count=id.txt总行数%40  config.work_path=程序所在的目录`
5. 在handle/g/ 下创建select目录，在handle/g/select/ 下创建sub目录（用于存放输出文件），并将config.py,run.py,select_fasta_by_linux_[i].py(i=0~40)放入select目录,再把silva_re.fa放入handle的上一层目录。
6. 开始序列统一化
`python handle/g/select/run.py`
7. 合并序列统一化结果
`cat handle/g/select/sub/*.txt > handle/g/unified.fa`
#### 七、生成特征表
1. 对物种注释表去冗余：在handle/g/ 下创建otu目录
`paste handle/g/id.txt handle/g/tax.txt > handle/g/otu/tax_sig.txt` \
`sort -t\t -k2 -u handle/g/otu/tax_sig.txt  > handle/g/otu/tax_sig+.txt`
2. 生成id.txt,tax.txt文件
`awk -F '\t' -v n=1 '{print $1}'  handle/g/otu/tax_sig+.txt >  handle/g/otu/id.txt` \
`awk -F '\t' -v n=1 '{print $2}'  handle/g/otu/tax_sig+.txt >  handle/g/otu/tax.txt`
3. 从re_silva.fa中挑选出与tax.txt相同注释名的序列得到otus.fa
`python handle/g/otu/select_sig_otu.py`
4. 使用vsearch生成特征表:
`vsearch --usearch_global handle/g/filtered.fa --db handle/g/otu/otus.fa --otutabout handle/g/otu/otutab.txt --id 0.97 --threads 15`
5. 生成标准格式的otus.sintax,用于后续分析
`python handle/g/otu/restore_otus_sintax.py`

