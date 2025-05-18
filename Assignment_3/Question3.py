def main():
    n = int(input("enter the of elements "))
    numbers = []

    for i in range(n):
        num = int(input("enter number "))
        numbers.append(num)

    
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            max_num = num

    
    print("maximum number is", min_num)

if __name__ == "__main__":
    main()