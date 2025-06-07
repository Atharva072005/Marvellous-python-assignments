class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

def main():
    p1 = Product("Pen", 10)
    p2 = Product("Pencil", 10)
    p3 = Product("Eraser", 5)

    if p1 == p2:
        print("p1 and p2 have same price")
    else:
        print("p1 and p2 have different price")

    if p1 == p3:
        print("p1 and p3 have same price")
    else:
        print("p1 and p3 have different price")

if __name__ == "__main__":
    main()
