class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def start(self):
        print("Car is starting with key ignition")
        print("Check seatbelt")
        print("Engine is starting")

def main():
    v = Vehicle()
    v.start()

    c = Car()
    c.start()

if __name__ == "__main__":
    main()
