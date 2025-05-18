def main():
    n = int(input("enter the of elements "))
    numbers = []

    for i in range(n):
        num = int(input("enter number "))
        numbers.append(num)

    
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num

    
    print("maximum number is", max_num)

if __name__ == "__main__":
    main()
