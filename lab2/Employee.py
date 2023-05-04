from MySQL_Handler import DBHandler

class Employee:

    db_connection = DBHandler("localhost", "root", "password", "db_name")
    all_employees = []

    def __init__(self, first_name, last_name, age, department, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department
        self.salary = salary
        self.id = None
        self.all_employees = []
        Employee.db_connection.create_table()
        self.id = Employee.db_connection.insert_employee(self)
        Employee.all_employees.append(self)

t

    @staticmethod
    def fire(employee_id):
        employee = None
        for e in Employee.all_employees:
            if e.id == employee_id:
                employee = e
                break
        if employee:
            Employee.all_employees.remove(employee)
            Employee.db_connection.delete_employee([employee_id])
            print(f"An Employee With id {employee_id} is Fired!")
        else:
            print(f"There is No Employee With id {employee_id}")

    def show(self):
        employee_table = PrettyTable()
        employee_table.field_names = ["ID", "First Name",
                                      "Last Name", "Age", "Department", "Salary"]
        employee_table.add_row(
            [self.id, self.first_name, self.last_name, self.age, self.department, self.salary])
        print("Employee Data")
        print(employee_table)

    @staticmethod
    def get_employees():
        employees = Employee.db_connection.get_all_employees()
        table = PrettyTable()
        table.field_names = ["ID", "First Name",
                             "Last Name", "Age", "Department", "Salary", "Managed Department"]
        for employee in employees:
            if employee[6] != 'NULL' : 
                salary = 'Confidential' 
            else: 
                salary = employee[5]

            table.add_row([employee[0], employee[1], employee[2],
                          employee[3], employee[4], salary, employee[6]])
        print(table)