def Pattern(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()

def main():
    n = int(input("Enter number of stars you want  "))
    Pattern(n)

if __name__ == "__main__":
    main()
