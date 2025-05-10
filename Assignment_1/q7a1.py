def divisible(num):
 if num % 5 == 0:
  return True
 else:
  return False


def main():
 print("Enter a number: ")
 num = int(input())
 result = divisible(num)
 print("Result:", result)


if __name__ == "__main__":
    main()
