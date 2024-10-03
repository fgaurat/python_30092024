import csv
import sqlite3

def main():

    with sqlite3.connect(r"./tp08/employees_db.db") as con:

        with open(r'./tp08/MOCK_DATA.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            sql = """INSERT INTO employees_tbl(first_name,last_name,email,gender,ip_address)
                    VALUES(?,?,?,?,?)"""
            
            for row in reader:
                del row['id']
                data_to_insert = list(row.values())
                con.execute(sql,data_to_insert)

if __name__=='__main__':
    main()
