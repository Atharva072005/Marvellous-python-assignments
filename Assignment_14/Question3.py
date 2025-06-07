
def main():

    class Book:
        def __init__(self, title, price):
            self.title = title      
            self.__price = price   

        
        def getPrice(self):
            return self.__price

            def setPrice(self, new_price):
            if new_price > 0:
                self.__price = new_price
            else:
                print("Invalid price! Must be positive.")

        
        def display(self):
            print("Title:", self.title)
            print("Price:", self.__price)



    b1 = Book("Python Programming", 450)


    b1.display()


    print("Price", b1.getPrice())


    b1.setPrice(500)
    print("Updated Price ", b1.getPrice())


    b1.setPrice(-100)


if __name__ == "__main__":
    main()