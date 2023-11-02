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
1. 去除空行并输出关键信息行 \
`awk '{if($2!="") print $0}' otus_all.sintax > handle/trim.txt` \
`awk -v n=2 '{print $1,$4}'  handle/trim.txt >  handle/to_1_4.txt`
3. 获取所有鉴定到g和s的注释行,并排序 \
`grep -E 'g:|s:' handle/to_1_4.txt > handle/select.txt`  \
`sort -t\t -k2  handle/select.txt  > handle/g/g.txt`
4. 生成id,tax文件,去除s水平列 \
`sed -i 's/\s/,/g' handle/g/g.txt` \
`awk -F ',' -v n=1 '{print $1}'  handle/g/g.txt >  handle/g/id.txt` \
`awk -F ',' -v n=6 '{print $2,$3,$4,$5,$6,$7}'  handle/g/g.txt >  handle/g/tax.txt` \
`sed -i 's/\s/,/g' handle/g/tax.txt`
#### 六、序列统一化 \
1. 查看id.txt总行数
`wc -l handle/g/id.txt`
2. 设置find_g_fa/config.py \
`config.threads=进程数  congfig.divide_count=id.txt总行数%40  config.work_path=程序所在的目录`
3. 在handle/g/ 下创建select目录，在handle/g/select/ 下创建sub目录（用于存放输出文件），并将config.py,run.py,select_fasta_by_linux_[i].py(i=0~40)放入select目录,再把silva_re.fa放入handle的上一层目录。
4. 开始序列统一化(将当前目录cd到handle/g/select目录) \
`for ((i=1;i<=40;i++)); do nohup python -u select_fasta_by_linux_$i.py > log$i>&1 & done`
5. 合并序列统一化结果
`cat handle/g/select/sub/*.txt > handle/g/filtered.fa`
#### 七、生成特征表
1. 对物种注释表去冗余：在handle/g/ 下创建otu目录
`paste handle/g/id.txt handle/g/tax.txt > handle/g/temp.txt` \
`sort -t\t -k2 -u handle/g/temp.txt  > handle/g/otu/uni.txt`
2. 生成id.txt,tax.txt文件
`awk -F '\t' -v n=1 '{print $1}'  handle/g/otu/uni.txt >  handle/g/otu/id.txt` \
`awk -F '\t' -v n=1 '{print $2}'  handle/g/otu/uni.txt >  handle/g/otu/tax.txt`
3. 从re_silva.fa中挑选出与tax.txt相同注释名的序列得到otus.fa(将当前目录cd到handle/g/select/otu目录) \
`python select_sig_otu.py`
4. 使用vsearch生成特征表: \
`vsearch --usearch_global handle/g/filtered.fa --db handle/g/otu/otus.fa --otutabout handle/g/otu/otutab.txt --id 0.97 --threads 15`
5. 生成标准格式的otus.sintax,用于后续分析 \
`python restore_otus_sintax.py`

