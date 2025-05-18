def Pattern(n):
    for i in range(n, 0, -1):
        print("* " * i)

def main():
    num = int(input("Enter number: "))
    print("Output:")
    Pattern(num)

if __name__ == "__main__":
    main()
