# Parent Class 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


# Parent Class 2
class Employee:
    def __init__(self, employee_id, salary):
        self.employee_id = employee_id
        self.salary = salary

    def display_employee_info(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ₹{self.salary}")

    def give_raise(self, amount):
        self.salary += amount
        print(f"Salary increased by ₹{amount}")


# Child Class (Multiple Inheritance)
class Manager(Person, Employee):
    def __init__(self, name, age, employee_id, salary, department):
        # Calling constructors of both parent classes
        Person.__init__(self, name, age)
        Employee.__init__(self, employee_id, salary)

        # Additional property
        self.department = department

    # Additional behavior
    def display_manager_info(self):
        print("\nManager Details")
        print("----------------")
        self.display_person_info()
        self.display_employee_info()
        print(f"Department: {self.department}")

    def conduct_meeting(self):
        print(f"{self.name} is conducting a meeting for {self.department} department.")


# Example Usage
manager1 = Manager("Rahul Sharma", 35, "M101", 75000, "IT")

manager1.display_manager_info()
manager1.conduct_meeting()
manager1.give_raise(5000)
manager1.display_manager_info()
