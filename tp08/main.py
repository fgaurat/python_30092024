from EmployeeDAO import EmployeeDAO

def main():
    dao = EmployeeDAO(r"./tp08/employees_db.db")
    all_employees = dao.find_all()
    # all = list(all_employees)
    # print(all[3])
    all = list(all_employees)
    print(all)
    print(50*'-')
    for employee in all_employees:
        print(employee)
    
if __name__=='__main__':
    main()
