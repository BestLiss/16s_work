# 16s_unifiy
Identification of intestinal microbiota  biomarkers in centenarians based on machine learning  \
#### 一、 从NCBI下载样本fasta格式文件后解压
#### 二、 对数据重新编号并合并成一个文件
1. 在代码执行目录创建re_id/input文件夹,并将待处理的文件放入re_id/input \
2. python执行single_re_id_i.py \
3. 将会在re_id/otuput目录下输出结果 \
4. cat re_id/otuput/*.fa > ASV.fa
#### 三、 格式化silva_16s_v123 \
1. [下载silva数据库:https://www.drive5.com/usearch/manual/sintax_downloads.html](https://www.drive5.com/usearch/manual/sintax_downloads.html)
2. 在代码执行目录创建re_silva/input文件夹,并将silva_16s_v123.fa放入re_silva/input \
3. 将会在re_silva/output目录下输出结果
#### 四、 使用vsearch鉴定物种
1. 创建conda环境:vsearch 安装并激活\
`conda creat -n vsearch -y python=2.7` \
`conda activate vsearch` \
2. 使用vsearch进行物种注释,分类水平可信度大于0.6
`vsearch --sintax ASV.fa --db  ./rdp_16s_v16.fa --tabbedout ./otus_all.sintax --sintax_cutoff 0.6 `
#### 五、处理注释文件otus_all.sintax \
1. 去除空行 \
`awk '{if($2!="") print $0}' otus_all.sintax > handle/trim.txt`
1. 获取所有鉴定到g的注释行
`awk '/g:/&&!/s:/' handle/trim.txt > handle/g/g.txt` \
2. 

