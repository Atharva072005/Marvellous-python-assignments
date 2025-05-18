def main():
    n = int(input("enter the of elements "))
    numbers = []
    total = 0

    for i in range(n):
        num = int(input("enter number "))
        numbers.append(num)
        total += num

    
    print("Sum of numbers:", total)

if __name__ == "__main__":
    main()
