def welcome():
    """
     This Displays the welcome message for the Caesar Cipher program.
    """
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text using Caesar Cipher.")

def enter_message():
    """
    This Gets user input for mode (encrypt or decrypt) and the message to be processed.

    And returns a tuple containing the selected mode ('e' or 'd'), the input message in uppercase, and the shift value.
    """
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()
        if mode in ['e', 'd']:
            break
        else:
            print("Invalid Mode")

    while True:
        message = input("What message would you like to {}:".format("encrypt" if mode == 'e' else "decrypt"))
        shift = input("What is the shift number: ")

        if shift.isdigit():
            return mode, message.upper(), int(shift)
        else:
            print("Invalid Shift")

def encrypt(message, shift):
    """
     This Encrypts a given message using the Caesar Cipher algorithm.
    and returns the encrypted message.
    """
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(message, shift):
    """
    Decrypt a given message using the Caesar Cipher algorithm.
    
    And returns the decrypted message.
    """
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            decrypted_char = chr((ord(char) - 65 - shift) % 26 + 65)
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message

def process_file(filename, mode, shift):
    """
    this Process messages from a file based on the specified mode and shift.
    
    Arguments:
        filename : The name of the file containing messages.
        mode : The mode for processing messages, 'e' for encrypt, 'd' for decrypt.
        shift : The shift value for the Caesar Cipher algorithm.
    and returns a list of processed messages.
    """
    messages = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                if mode == 'e':
                    messages.append(encrypt(line.strip(), shift))
                elif mode == 'd':
                    messages.append(decrypt(line.strip(), shift))
    except FileNotFoundError:
        print("File not found.")
    return messages

def write_messages(messages):
    """
    This Writes a list of messages to a file named 'results.txt'.
    Arguments:
        messages : A list of messages to be written to the file.
    """
    with open('results_2417737.txt', 'w') as file:
        for message in messages:
            file.write(message + '\n')
    print("Output written to results_2417737.txt")

def message_or_file():
    """
    This Gets user input for mode, source (file or console), and message or filename.
    and returns a tuple containing the selected mode ('e' or 'd'), the input message in uppercase,
               the filename (if source is 'f'), the shift value, and the source ('f' or 'c').
    """
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()
        if mode in ['e', 'd']:
            break
        else:
            print("Invalid Mode")

    while True:
        source = input("Would you like to read from a file (f) or the console (c)? ").lower()
        if source in ['f', 'c']:
            break
        else:
            print("Invalid Input")

    message = None
    filename = None

    if source == 'c':
        message = input("What message would you like to {}:".format("encrypt" if mode == 'e' else "decrypt")).upper()
    elif source == 'f':
        while True:
            filename = input("Enter a filename: ")
            try:
                with open(filename, 'r'):
                    pass
                break
            except FileNotFoundError:
                print("Invalid Filename")

    shift = input("What is the shift number: ")

    return mode, message, filename, int(shift), source

def main():
    """
    this runs the main program loop for the Caesar Cipher application.
    """
    welcome()

    while True:
        mode, message, filename, shift, source = message_or_file()

        if filename:
            messages = process_file(filename, mode, shift)
        else:
            messages = [encrypt(message, shift)] if mode == 'e' else [decrypt(message, shift)]

        if source == 'f':
            write_messages(messages)
        else:
            for msg in messages:
                print(msg)

        another_message = input("Would you like to encrypt or decrypt another message? (y/n): ").lower()
        if another_message != 'y':
            print("Thanks for using the program, goodbye!")
            break

if __name__ == "__main__":
    main()
