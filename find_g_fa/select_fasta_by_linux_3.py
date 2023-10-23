##############
import os
import run,config
path = "../"+config.work_path
os.chdir(path)

ref_path = "../id.txt"


ref_lines = open(ref_path, 'r', encoding='utf-8').readlines()

sub = (len(ref_lines) - config.divide_count) / config.threads

# print(str(int(sub)))
run.run(int(sub)*2,int(sub)*3,'3')

# t2 = threading.Thread(target=run,args=(int(sub)+1,int(sub)*2,'2'))
# t3 = threading.Thread(target=run,args=(int(sub)*2+1,int(sub)*3,'3'))
# t4 = threading.Thread(target=run,args=(int(sub)*3+1,int(sub)*4,'4'))
# t5 = threading.Thread(target=run,args=(int(sub)*4+1,int(sub)*5,'5'))
# t6 = threading.Thread(target=run,args=(int(sub)*5+1,int(sub)*6,'6'))
# t7 = threading.Thread(target=run,args=(int(sub)*6+1,int(sub)*7,'7'))
# t8 = threading.Thread(target=run,args=(int(sub)*7+1,int(sub)*8+1,'8'))
# t1.start()


