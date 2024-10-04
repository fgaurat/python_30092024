from glob import glob
from pprint import pprint
import os
import re
def main():
    # all_logs_files = glob('/Users/fgaurat/local_dev/formations/python_30092024/tp09/*.log')
    # for logs_file in all_logs_files:
    #     p = logs_file.split(os.sep)
    #     print(os.sep.join(p[-2:]))
    
    all_logs_files = glob(r'tp09/*.log')
    cpt=0
    for logs_file in all_logs_files:
        with open(logs_file) as f:
            for line in f:
                clean_line = line.strip()
                # result_ip = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', clean_line)
                # result_ip = re.findall(r'^(.+?)\s', clean_line)
                # print(result_ip)
                reg = r'\"\s404\s'
                # if re.match(reg,clean_line):
                result = re.search(reg,clean_line)
                if result:
                    cpt+=1
                    print(result ,clean_line)
    print(cpt)
if __name__=='__main__':
    main()
