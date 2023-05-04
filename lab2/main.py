from Employee import Employee
from Manager import Manager
import sys


class Main:

    def menu(self):

        while True:
            print("\n1.Add Employee")
            print("2.Add Manager")
            print("3.List All Employees")
            print("4.Fire Employee")
            print("5.Exit")

            op = input("\nPlease Enter The number of your desired Operation: ")

            if op == "1":
                self.add_employee()
            elif op == "2":
                self.add_manager()
            elif op == "3":
                self.get_employees()
            elif op == "4":
                self.fire_employee()
            elif op == "5":
                self.exit_()
            else:
                print("Invalid Operation, Try Again")

    def add_employee(self):
        try:
            print("Please Enter The Employee Data:")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            age = int(input("Age: "))
            department = input("Department: ")
            salary = float(input("Salary: "))
            Employee(first_name, last_name, age,
                     department, salary)
            print("An Employee has been Added Successfully")

        except:
            print('Something Went Wrong Could not Add Employee')

    def add_manager(self):
        try:
            print("Please Enter The Manager Data:")
            first_name = input("First Name: ")
            last_name = input("Last name: ")
            age = int(input("Age: "))
            department = input("Department: ")
            salary = float(input("Salary: "))
            managed_department = input("Managed Department: ")
            Manager(first_name, last_name, age,
                    department, salary, managed_department)
            print("A Manager has been Added Successfully")

        except:
            print('Something Went Wrong Could not Add Manager')

    def get_employees(self):
        try:
            Employee.get_employees()

        except:
            print('Something Went Wrong Could not List Employees')

    def fire_employee(self):
        try:
            employee_id = input("Please Enter The Employee ID : ")
            Employee.fire(int(employee_id))

        except:
            print('Something Went Wrong Could not Fire Employee')

    def exit_(self):
        print("Exit The program...")
        sys.exit()

app = Main()
app.menu()