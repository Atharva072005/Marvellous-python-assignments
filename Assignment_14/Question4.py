class Student:
    school_name = "xyz School"  

    def __init__(self, name, roll_no):
        self.name = name                  
        self.roll_no = roll_no            

    def display(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("School Name:", Student.school_name)  



s1 = Student("Atharva", 101)
s2 = Student("Sneha", 102)


s1.display()
s2.display()


Student.school_name = "marvellous School"

# Display again after school name change
print("After changing school name:")
s1.display()
s2.display()
