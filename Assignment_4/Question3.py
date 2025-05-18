
from functools import reduce

def main():
    
    print("Enter number of elements : ")
    size = int(input())

    Data = list()

    print("Enter the values")
    for i in range(size):
        no = int(input())
    Data.append(no)

    print("Entered elements are : ")
    for value in Data:
     print(value)
    
    fData = list(filter(lambda x: x >= 70 and x <= 90, Data))
    print("filtered list is ", fData)

    
    mData = list(map(lambda x: x + 10, fData))
    print("mapped list is", mData)

    rData = reduce(lambda x, y: x * y, mData)
    print("reduced list is", rData)


    if __name__ == "__main__":
        main()
