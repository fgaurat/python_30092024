from glob import glob
from pprint import pprint
import os
import re
def main():
    # all_logs_files = glob('/Users/fgaurat/local_dev/formations/python_30092024/tp09/*.log')
    # for logs_file in all_logs_files:
    #     p = logs_file.split(os.sep)
    #     print(os.sep.join(p[-2:]))
    
    all_logs_files = glob('*.log')

    for logs_file in all_logs_files:
        with open(logs_file) as f:
            for line in f:
                clean_line = line.strip()
                # result_ip = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', clean_line)
                result_ip = re.findall(r'^(.+?)\s', clean_line)
                print(result_ip)

if __name__=='__main__':
    main()
