import random
import string


#About Password
lowercase = string.ascii_lowercase 
uppercase = string.ascii_uppercase
digits = string.digits
punctuations = string.punctuation
character_used = None
def genrate_password():
    pass


def view_password():
    pass

def save_password():
    pass




# Main function 
def main():
    length = int(input("Enter the Length for the password  : "))
    type_used =input("Enter the words to be use [Lower case (low), Upper Case (up) , Digits (digits) , punctutaions (punc)] : ")
    type_used = type_used.split()
    print(type_used)
    
if __name__ == "__main__" :
    main()