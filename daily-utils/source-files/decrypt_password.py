from cryptography.fernet import Fernet
import os

def decrypt_password(file_name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    str_dir = str(dir_path) + '\\'
    with open(str_dir + 'key.bin', 'rb') as file_object:
        for line in file_object:
            key = line
    cipher_suite = Fernet(key)
    with open(str_dir + file_name, 'rb') as file_object:
        for line in file_object:
            encryptedpwd = line
    uncipher_text = (cipher_suite.decrypt(encryptedpwd))
    plain_text_encryptedpassword = bytes(uncipher_text).decode("utf-8") #convert to string
    return plain_text_encryptedpassword
