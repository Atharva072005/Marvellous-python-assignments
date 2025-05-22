def palindrome(str):
    for i in range(0, int(len(str) / 2)):



        if str[i] != str[len(str) - i - 1]:

            return False
    return True

def main():
  
    input = input("Enter a word ")


    result = palindrome(input)

   
    if result:
        print("word is palindrome.")
    else:
        print("Word is  not a palindrome.")


if __name__ == "__main__":
    main()
