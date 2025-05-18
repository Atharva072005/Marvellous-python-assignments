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


filtered = list(filter(prime, Data))
print("filtered list is", filtered)


mapped = list(map(lambda x: x * 2, filtered))
print("mapped list is", mapped)

maximum = reduce(lambda x, y: x if x > y else y, mapped)
print("reduced list is", maximum)
