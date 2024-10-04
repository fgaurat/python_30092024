from EmployeeDAO import EmployeeDAO
import configparser
import argparse

def main():

    parser = argparse.ArgumentParser(prog='Read Employees',
                    description='What the program does',
                    epilog='Text at the bottom of help')
    parser.add_argument('config_file',help="The config file.")
    args = parser.parse_args()

    print(args.config_file)

    config = configparser.ConfigParser()
    config.read(args.config_file)
    print()
    dao = EmployeeDAO(config['DATABASE']['db_file'])
    all_employees = dao.find_all()
    # all = list(all_employees)
    # print(all[3])
    # all = list(all_employees)
    # print(all)
    print(50*'-')
    for employee in all_employees:
        print(employee)
    
if __name__=='__main__':
    main()
