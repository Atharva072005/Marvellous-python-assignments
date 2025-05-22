def main():
    print("no of inputs  ")
    size = int(input())

    
    data = []

    print("Enter the values ")
    for i in range(size):
        no = int(input())
        data.append(no)

    
   
    mdata = list(map(lambda x: x * 2, data))
    print("Doubled values are ")
    for value in mdata:
        print(value)

if __name__ == "__main__":
    main()
