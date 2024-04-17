import rsa
import os

# implement rsa encryption, decryption, signing and verifying
# generate public and private keys

def main():
    if (os.path.exists('keys/publicKey.pem') and os.path.exists('keys/privateKey.pem')):
        print('Keys already exist, do you want to overwrite them?')
        if (input('y/n: ') == 'y'):
            generateKeys()
    else:
        generateKeys()
    
    # read public key
    with open('keys/publcKey.pem', 'rb') as p:
        publicKey = rsa.PublicKey.load_pkcs1(p.read())
    
    # read private key
    with open('keys/privateKey.pem', 'rb') as p:
        privateKey = rsa.PrivateKey.load_pkcs1(p.read())

    # encrypt message
    print ('Enter message to encrypt: ')
    message = input()
    message = message.encode('utf-8')

    encryptedMessage = rsa.encrypt(message, publicKey)
    print('Encrypted message: ', encryptedMessage)

    # sign message
    signature = rsa.sign(message, privateKey, 'SHA-1')
    print('Signature: ', signature)

    # verify signature
    if (rsa.verify(message, signature, publicKey)):
        print('Signature is valid')
    else:
        print('Signature is invalid')

    # decrypt message
    decryptedMessage = rsa.decrypt(encryptedMessage, privateKey)
    print('Decrypted message: ', decryptedMessage.decode('utf-8'))

def generateKeys():
    # generate public and private keys
    # check if the key files exist, if not make them 
    if not os.path.exists('keys'):
        os.mkdir('keys')
    (public_key, private_key) = rsa.newkeys(2048)
    with open('keys/publcKey.pem', 'wb') as p:
        p.write(public_key.save_pkcs1('PEM'))
    with open('keys/privateKey.pem', 'wb') as p:
        p.write(private_key.save_pkcs1('PEM'))

if __name__ == '__main__':
    main()
