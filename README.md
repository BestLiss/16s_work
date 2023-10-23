# 16s_unifiy
Identification of intestinal microbiota  biomarkers in centenarians based on machine learning
#### 一、 从NCBI下载样本fasta格式文件后解压
#### 二、 对数据重新编号并合并成一个文件
1. 在代码执行目录创建re_id/input文件夹,并将待处理的文件放入re_id/input 
2. python执行single_re_id_i.py 
3. 将会在re_id/otuput目录下输出结果 
4. cat re_id/otuput/*.fa > ASV.fa
#### 三、 格式化silva_16s_v123
1. [下载silva数据库:https://www.drive5.com/usearch/manual/sintax_downloads.html](https://www.drive5.com/usearch/manual/sintax_downloads.html)
2. 在代码执行目录创建re_silva/input文件夹,并将silva_16s_v123.fa放入re_silva/input \
3. 将会在re_silva/output目录下输出结果
#### 四、 使用vsearch鉴定物种
1. 创建conda环境:vsearch 安装并激活\
`conda creat -n vsearch -y python=2.7` \
`conda activate vsearch`
2. 使用vsearch进行物种注释,分类水平可信度大于0.6
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
#### 六、序列统一化 \
1. 生成序列id \
`awk -F ',' -v n=1 '{print $1}'  all_g.txt >  handle/g/id.txt`
2. 生成序列的注释文件 \
`awk -F ',' -v n=6 '{print $2,$3,$4,$5,$6,$7}'  all_g.txt >  handle/g/tax.txt` \
`sed -i 's/\s/,/g' handle/g/tax.txt`
3. 查看id.txt总行数
`wc -l handle/g/id.txt`
4. 设置find_g_fa/config.py
`config.threads=进程数  congfig.divide_count=id.txt总行数%40  config.work_path=程序所在的目录`
5. 


