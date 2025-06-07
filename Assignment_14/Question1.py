def main():

    class Employee:
        def __init__(self, name, emp_id, salary):  
            self.name = name
            self.emp_id = emp_id
            self.salary = salary

        def display_details(self):                 
            print("Employee Details:")
            print("Name     :", self.name)
            print("Emp ID   :", self.emp_id)
            print("Salary   :", self.salary)


    def main():
        
        emp1 = Employee("Atharva", 101, 50000)
        emp2 = Employee("Pooja", 102, 60000)

        
        emp1.display_details()
        print()
        emp2.display_details()

    


if __name__ == "__main__": 
  main()
