class Employee:
    def __init__(self):
        self.name = "Atharva"           
        self._department = "IT"       
        self.__salary = 50000       

    def show(self):
        print("Name: " + self.name)
        print("Department: " + self._department)
        print("Salary:", self.__salary)

def main():
    emp = Employee()
    emp.show()

    print("public variable:", emp.name)
    print(" protected variable:", emp._department)
    print(" private variable:", emp._Employee__salary)

if __name__ == "__main__":
    main()
