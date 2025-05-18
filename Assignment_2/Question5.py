def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def main():
    num = int(input("Enter number: "))
    if is_prime(num):
        print("Output: It is Prime Number")
    else:
        print("Output: It is Not a Prime Number")

if __name__ == "__main__":
    main()
