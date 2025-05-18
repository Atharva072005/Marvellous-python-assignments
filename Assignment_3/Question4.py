def main():
    n = int(input("Enter number of elements "))
    numbers = []

    print("Enter elements:")
    for i in range(n):
        num = int(input())
        numbers.append(num)

    search = int(input("Enter element to search"))

    
    count = 0
    for num in numbers:
        if num == search:
            count += 1

    print("Output:", count)

if __name__ == "__main__":
    main()
