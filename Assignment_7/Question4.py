from functools import reduce  

def main():
    print("enter the list input ")
    size = int(input())

    data = []

    print("enter the elements in the list")
    for i in range(size):
        no = int(input())
        data.append(no)

    
    rdata = reduce(lambda x, y: x * y, data)

    print("Product of all numbers is:", rdata)

if __name__ == "__main__":
    main()
