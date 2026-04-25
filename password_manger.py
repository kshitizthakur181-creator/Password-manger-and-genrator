import random
import string


# About Password
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
punctuations = string.punctuation


def genrate_password(character_used, length):
    password = "".join(random.choices(character_used, k=length))
    print(password)


def view_password():
    pass


def save_password(password):
    pass


# Main function
def main():

    length = int(input("Enter the Length for the password (8 - 16) : "))
    type_used = input(
        "Enter the words to be use [Lower case (low), Upper Case (up) , Digits (digits) , punctutaions (punc)] : "
    )
    type_used = type_used.split()
    
    character_used = ""
    
    for typies in type_used:
        if typies == "low":
            character_used += lowercase
        elif typies == "up":
            character_used += uppercase
        elif typies == "digits":
            character_used += digits
        elif typies == "punc":
            character_used += punctuations
        else:
            print(" ---Invalid word--- ")
            break
    genrate_password(character_used, length)


if __name__ == "__main__":
    main()
