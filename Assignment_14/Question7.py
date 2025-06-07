class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

    def display(self):
        print("Name  " + self.name)
        print("Age  ", self.age)
        print("Subject " + self.subject)
        print("Salary ", self.salary)

def main():
    t1 = Teacher("Atharva", 30, "Maths", 50000)
    t1.display()

if __name__ == "__main__":
    main()
