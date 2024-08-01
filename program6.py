import tkinter as tk
from tkinter import messagebox, simpledialog

# Employee dictionary
Employee = {}

# Functions for employee operations
def create_employee():
    n = simpledialog.askinteger("Input", "Enter the number of employees:")
    for i in range(n):
        EmpId = simpledialog.askinteger("Input", f"Enter the Employee ID for Employee {i + 1}:")
        EmpName = simpledialog.askstring("Input", "Enter the employee name:")
        EmpDOB = simpledialog.askstring("Input", "Enter the DOB:")
        Designation = simpledialog.askstring("Input", "Enter the designation:")
        
        Employee[EmpId] = [EmpName, EmpDOB, Designation]
    messagebox.showinfo("Info", "Employees created successfully")

def add_employee():
    EmpId = simpledialog.askinteger("Input", "Enter the Employee ID:")
    EmpName = simpledialog.askstring("Input", "Enter the employee name:")
    EmpDOB = simpledialog.askstring("Input", "Enter the DOB:")
    Designation = simpledialog.askstring("Input", "Enter the designation:")
    
    Employee[EmpId] = [EmpName, EmpDOB, Designation]
    messagebox.showinfo("Info", "Employee added successfully")

def search_employee():
    EId = simpledialog.askinteger("Input", "Enter the employee ID to display:")
    emp_details = Employee.get(EId, None)
    if emp_details:
        messagebox.showinfo("Employee Details", f"Employee ID: {EId}\nName: {emp_details[0]}\nDOB: {emp_details[1]}\nDesignation: {emp_details[2]}")
    else:
        messagebox.showwarning("Not Found", "Employee not found")

def delete_employee():
    EId = simpledialog.askinteger("Input", "Enter the employee ID to delete:")
    emp_details = Employee.pop(EId, None)
    if emp_details:
        messagebox.showinfo("Info", "Employee deleted successfully")
    else:
        messagebox.showwarning("Not Found", "Employee not found")

def display_employees():
    if not Employee:
        messagebox.showinfo("Info", "No employee details found to print")
    else:
        employees = "\n".join([f"ID: {EmpId}, Name: {details[0]}, DOB: {details[1]}, Designation: {details[2]}" for EmpId, details in Employee.items()])
        messagebox.showinfo("Employee List", employees)

# Create main window
root = tk.Tk()
root.title("Employee Database")

# Create and place buttons
tk.Button(root, text="Create Employee", command=create_employee).pack(fill=tk.X)
tk.Button(root, text="Add New Employee", command=add_employee).pack(fill=tk.X)
tk.Button(root, text="Search Employee", command=search_employee).pack(fill=tk.X)
tk.Button(root, text="Delete Employee", command=delete_employee).pack(fill=tk.X)
tk.Button(root, text="Display Employees", command=display_employees).pack(fill=tk.X)

# Start the Tkinter event loop
root.mainloop()


