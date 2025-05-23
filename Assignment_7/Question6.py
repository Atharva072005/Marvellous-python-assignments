def prime(num):
    if n < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def prime_numbers(no):
    
    fdata = list(filter(prime, no))
    return fdata


def main():
   
    size = int(input("enter no of elements in list  "))
    data = []

    print("Enter number of elements")
    for i in range(size):
        num = int(input(size))
        data.append(num)

    prime_list = (data)

    print("Prime numbers in the list are:")
    print(prime_list)

if __name__ == "__main__":
    main()
