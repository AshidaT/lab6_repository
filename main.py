def encode(password):
# defines function 'encode', taking in 'password' as parameter
    encoded_password = ""
# stores encoded passkey in an empty string
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password = encoded_password + encoded_digit
# changes each numeral in 'password' by adding/moving it up 3 places
    return encoded_password
# returns the encoded_password


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
# defines main with a continuous loop and asks user for an input

        if choice == '1':
            password = input("Please enter your password to encode: ")
            encoded = encode(password)
            print("Your password has been encoded and stored!")
        # prompts user to enter a password to be encoded

        elif choice == '2':
            print(f"The encoded password is {encoded}, and the original password is {decode(encoded)}.")
        # checks if encoded is within the local scope, if it is, prints both encoded and decoded pass

        elif choice == '3':
            break

        else:
            print("Invalid choice. Please enter a valid option.")
        # prints Goodbye to terminate the program, break exits the loop


if __name__ == "__main__":
    main()





