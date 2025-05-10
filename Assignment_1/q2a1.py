def chknum(number):
 if number % 2 == 0:
  print("even number")
 else:
  print("odd number")


def main():
 print("Enter a number: ")
 num = int(input())
 chknum(num)


if __name__ == "__main__":
    main()
