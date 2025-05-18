def sum_of_digits(number):
    total = 0
    number = abs(number)  
    while number > 0:
        digit = number % 10
        total += digit
        number = number // 10
    return total

def main():
    num = int(input("Enter a number: "))
    print("Sum of digits:", sum_of_digits(num))

if __name__ == "__main__":
    main()
