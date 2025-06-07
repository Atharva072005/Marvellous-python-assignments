class Calculator:
    def add(self, a, b):
        print("Addition : ", a + b)

    def subtract(self, a, b):
        print("Subtraction : ", a -  b)

    def multiply(self, a, b):
        print("Multiplication : ", a*b)

    def divide(self, a, b):
        if b != 0:
            print("Division  ", a / b)
        else:
            print("false divisor")

def main():
    a = int(input("give first number : "))
    b = int(input("give second number : "))

    calc = Calculator()

    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = int(input("Enter your choice (1-4) : "))

    if choice == 1:
        calc.add(a, b)
    elif choice == 2:
        calc.subtract(a, b)
    elif choice == 3:
        calc.multiply(a, b)
    elif choice == 4:
        calc.divide(a, b)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
