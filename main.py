
def encode(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password = encoded_password + encoded_digit
    return encoded_password


def decode(encoded_password):
    decoded_password = ""
    for char in encoded_password:
        if (int(char) - 3) <= -1:
            decoded_password += str((int(char) -3)+10)
        else:
            decoded_password += str(int(char) - 3)
    return decoded_password
# Decodes by subtracting 3 from each digit, if result is negative, 10 is added. Result then added to decoded_password.


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
            print(f"The encoded password is {encoded}, and the original password is {decode(encoded)}.")

        elif choice == '3':
            break

        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()






