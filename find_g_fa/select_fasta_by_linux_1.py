##############
import os
import run,config
path = "../"+config.work_path
os.chdir(path)


ref_path = "../id.txt"


ref_lines = open(ref_path, 'r', encoding='utf-8').readlines()

sub = (len(ref_lines) - config.divide_count) / config.threads

# print(str(int(sub)))
run.run(0, int(sub), '1')

