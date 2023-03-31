# XOR Cipher

def encrypt():
    key = input("Key: ").upper()
    msg = input("Plaintext: ").upper()

    encryptHex = ""
    keyItr = 0

    for i in range(len(msg)):
        temp = ord(msg[i]) ^ ord(key[keyItr])
        encryptHex += hex(temp)[2:].zfill(2)
        keyItr += 1

        if keyItr >= len(key):
            keyItr = 0

    file = open("msg2.txt", 'w')
    file.write(format(encryptHex))
    file.closed

    print("Save to text file.")


def decrypt():
    file = open("msg2.txt", 'r')
    line = file.readlines()
    file.closed

    msgEncrypt = line[0]
    key = input("Key: ")

    hexToUni = ""
    for i in range(0, len(msgEncrypt), 2):
        hexToUni += bytes.fromhex(msgEncrypt[i:i + 2]).decode('utf-8')

    msgDecrypt = ""
    keyItr = 0
    for i in range(len(hexToUni)):
        temp = ord(hexToUni[i]) ^ ord(key[keyItr])
        msgDecrypt += chr(temp)
        keyItr += 1

        if keyItr >= len(key):
            keyItr = 0

    msgDecrypt = msgDecrypt.upper()
    print("Decrypt: {}".format(msgDecrypt))


if __name__ == '__main__':

    print("1 - Encrypt")
    print("2 - Decrypt")

    choice = input("> ")

    if choice.__eq__("1"):

        encrypt()

    elif choice.__eq__("2"):

        decrypt()

    else:
        print("Error: Invalid input.")
