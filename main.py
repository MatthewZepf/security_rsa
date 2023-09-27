import rsa
import os
# feel free to include any other imports you need, if rsa is not working, make sure you have it pip installed
# documentation for rsa can be found here: https://stuvel.eu/python-rsa-doc/usage.html

def main():
    """Generates public and private keys, if they already exist, ask the user if they want to overwrite them.
    Take a message from the user, encrypt it, sign it, verify the signature, and decrypt the message.
    """
    generateKeys()

    # read keys from the files you stored them in generateKeys and store them as variables
    # hint: use open() with 'rb' as the second argument to read the keys to a file


    # get message from user and encode it with utf-8

    # encrypt message with public key and print it

    # sign message with SHA-1 and print it
    
    # verify signature

    # decrypt message
    

def generateKeys():
    """ Generate public and private keys 
    Check if the key directory exists, if not make one (use os.mkdir())
    Open respective key file and write the key to it (there is a method for this in the rsa library)
    """
    # hint: use open() with 'wb' as the second argument to write the keys to a file
    # feel free to experiment with different lengths of bits for the key 

if __name__ == '__main__':
    main()
