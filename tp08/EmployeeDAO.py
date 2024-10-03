import sqlite3
from Employee import Employee
from typing import List

class EmployeeDAO:
    def __init__(self,db_file) -> None:
        self.__con = sqlite3.connect(db_file)

    def __del__(self):
        self.__con.close()

    def find_all(self):
        # all_employees = []
        sql = "SELECT * FROM employees_tbl"
        cur = self.__con.cursor()
        res = cur.execute(sql)
        for data in res.fetchall():
            e = Employee(*data)
            yield e
            # all_employees.append(e)
        
        # return all_employees
