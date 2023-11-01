
def encode(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password = encoded_password + encoded_digit
    return encoded_password





def main():
    while True:
        print("Menu\n-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = input("Please enter an option: ")

        if choice == '1':
            password = input("Please enter your password to encode: ")
            encoded = encode(password)
            print("Your password has been encoded and stored!")
        elif choice == '2':
            if 'encoded' in locals():
                print(f"The encoded password is {encoded}, and the original password is {decode(encoded)}.")
            else:
                print("Please encode a password first.")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()






