# Caesar Ciphere

def encrypt():
    msgList = []
    i = 0

    skips = input("Places to shift: ")
    msg = input("Plaintext: ").upper()

    size = len(msg)
    msgList[0:] = msg
    msgEncrypt = ""

    while i < size:
        temp = msgList[i]
        if temp.__eq__(" "):
            temp = " "
        else:
            temp = ord(temp) + int(skips)

            if temp > 90:
                temp = temp - 90
                # print(temp)
                temp = 65 + (temp - 1)
                msgList[i] = chr(temp)
            else:
                msgList[i] = chr(temp)
        i = i + 1

    for character in msgList:
        msgEncrypt += character

    # print(msgEncrypt)
    file = open("msg.txt", 'w')
    file.write(msgEncrypt)
    file.closed

    print("Save to text file.")


def decrypt():
    file = open("msg.txt", 'r')
    lines = file.readlines()

    skips = input("Place to shift: ")

    i = 0
    msgList = []
    # skips = lines[0]
    msgEncrypt = lines[0]

    msgList[0:] = msgEncrypt

    while i < len(lines[0]):

        temp = msgList[i]

        if temp.__eq__(" "):
            temp = " "
        else:
            temp = ord(temp) - int(skips)

            if temp < 65:
                temp = temp + (27 - 1)
                msgList[i] = chr(temp)
            else:
                msgList[i] = chr(temp)
        i = i + 1

    msgDecrypt = ""
    for character in msgList:
        msgDecrypt += character

    print("Decrypt: " + msgDecrypt)


if __name__ == '__main__':
    print("1 - Encrypt")
    print("2 - Decrypt")

    choose = input("> ")

    if choose.__eq__("1"):

        encrypt()

    elif choose.__eq__("2"):

        decrypt()

    else:
        print("Error: Invalid input")
