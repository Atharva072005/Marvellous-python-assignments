def print_factors_and_sum(num):
    temp = 0
    print("Factors:", end=" ")
    for i in range(1, num):
        if num % i == 0:
            print(i, end=" ")
            temp += i
    print("\nSum of factors:",  temp)

def main():
    num = int(input("Enter number: "))
    print_factors_and_sum(num)

if __name__ == "__main__":
    main()
