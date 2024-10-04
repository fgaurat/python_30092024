import tkinter as tk
from tkinter import ttk
from EmployeeDAO import EmployeeDAO  # Make sure to adjust the import according to your project structure

class EmployeeApp:
    def __init__(self, root, db_file):
        """Initialize the main application window."""
        self.root = root
        self.root.title("Employee List")
        
        self.employee_dao = EmployeeDAO(db_file)
        
        # Create Treeview for displaying employees
        self.tree = ttk.Treeview(self.root, columns=("ID", "FirstName", "LastName", "Email"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("FirstName", text="FirstName")
        self.tree.heading("LastName", text="LastName")
        self.tree.heading("Email", text="Email")
        
        # Set the column widths
        self.tree.column("ID", width=50)
        self.tree.column("FirstName", width=150)
        self.tree.column("LastName", width=100)
        self.tree.column("Email", width=100)
        
        self.tree.pack(expand=True, fill="both")
        
        # Load employees into the Treeview
        self.load_employees()

    def load_employees(self):
        """Load employees from the database and insert them into the Treeview."""
        for employee in self.employee_dao.find_all():
            self.tree.insert("", "end", values=(employee.id, employee.first_name, employee.last_name, employee.email))

if __name__ == "__main__":
    # Replace 'your_database.db' with the path to your SQLite database
    db_file = 'employees_db.db'
    
    root = tk.Tk()
    app = EmployeeApp(root, db_file)
    root.mainloop()