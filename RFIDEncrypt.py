import pyAesCrypt
import os
import serial

'''
https://pypi.python.org/pypi/pyAesCrypt
'''
#TODO: build a python project (https://docs.travis-ci.com/user/languages/python/)
#TODO: add graphic interface (https://www.tutorialspoint.com/python/python_gui_programming.htm)

list_file=dict()
path="C:\\Users\lafac\Desktop\Test\\"

arduino = serial.Serial('COM3', 115200, timeout=.1) #change COM3 port with the one
														#where arduino is
while True:
    serial_data = arduino.readline()[:-2]  # the last bit gets rid of the new-line chars
    if serial_data:
        password = serial_data[:30]
        print("RFID code acquired!") #TODO fix the multiple RFID detect!!!


        for root, dirs, files in os.walk(path):
            for filename in files:
                list_file[filename]="plaintext"

        # encryption/decryption buffer size - 64K
        bufferSize = 64 * 1024

        for file in list_file.items(): #TODO: write a better code with functions
            plaintext=path+file[0]
            if file[1] == "plaintext":
                if os.path.isfile(plaintext): #must use this check due to the multiple RFID inputs
                    print("Encrypting: "+str(plaintext))
                    ciphertext=str(str(plaintext)+".aes")
                    # encrypt
                    pyAesCrypt.encryptFile(plaintext, ciphertext, str(password), bufferSize)
                    os.remove(plaintext)
                    list_file[file[0]]="encrypted"
            else:
                print("Decrypting: " + str(plaintext))
                try:
                    ciphertext = str(str(plaintext) + ".aes")
                    if os.path.isfile(ciphertext): #must use this check due to the multiple RFID inputs
                        # decrypt
                        pyAesCrypt.decryptFile(ciphertext, plaintext, str(password), bufferSize)
                        os.remove(ciphertext)
                        list_file[file[0]] = "plaintext" #TODO automatically detect encrypted files
                except:
                    print("Error while decrypting, wrong password or file corrupted!")








