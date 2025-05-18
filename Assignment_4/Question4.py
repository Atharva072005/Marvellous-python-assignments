
from functools import reduce


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
fData = list(filter(lambda x: x % 2 == 0, Data))
print(" filtered list ", fData)


mData = list(map(lambda x: x ** 2, fData))
print("mapped list ", mData)


rData = reduce(lambda x, y: x + y, mData)
print("REduced list is ", rData)
