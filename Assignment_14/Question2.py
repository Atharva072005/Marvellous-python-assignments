class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        return self.length *self.width

    def compute_perimeter(self):
        return 2* (self.length + self.width)



def main():
    print("Enter length and width of the rectangle:")

    length = int(input("Length: "))
    width = int(input("Width: "))

    rect = Rectangle(length, width)


    print("Area is", rect.compute_area())
    print("Perimeter is ", rect.compute_perimeter())

if __name__ == "__main__":
    main()
