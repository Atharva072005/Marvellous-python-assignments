from Marvellousnum import Prime

if __name__ == "__main__":
    count = int(input("enter the no in list "))
    numbers = []

    print("enter the nos in list")
    for i in range(count):
        number = int(input())
        numbers.append(number)

    prime_sum = 0
    for num in numbers:
        if Prime(num):
            prime_sum += num

    print("Sum of prime numbers is:", prime_sum)
