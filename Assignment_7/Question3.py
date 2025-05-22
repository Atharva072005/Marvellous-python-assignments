def main():
    print("Enter no in the list")
    size = int(input())

    data = []

    print("Enter list values")
    for i in range(size):
        no = int(input())
        data.append(no)

   
    fdata = list(filter(lambda x: x % 2 == 0, data))

    print("Even numbers are ")
    for value in fdata:
        print(value)

if __name__ == "__main__":
    main()
