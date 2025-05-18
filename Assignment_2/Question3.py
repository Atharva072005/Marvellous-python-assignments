def factorial(num):
    temp = 1
    for i in range(1, num + 1):
        temp *= i
    return temp

def main():
    num = int(input("Enter number: "))
    result = factorial(num)
    print("Factorial:", result)

if __name__ == "__main__":
    main()
