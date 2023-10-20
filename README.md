# 16s_work
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
#### 四、 
