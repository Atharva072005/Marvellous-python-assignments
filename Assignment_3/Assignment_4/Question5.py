from functools import reduce


def prime(n):
    if n < 2:
        return False
    
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


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


fData= list(filter(prime, Data))
print("filtered list is", fData)


mData = list(map(lambda x: x * 2, fData))
print("mapped list is", mData)

rData = reduce(lambda x, y: x if x > y else y, mData)
print("reduced list is", rData)
