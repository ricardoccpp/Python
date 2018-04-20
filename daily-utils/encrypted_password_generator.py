import getpass
from cryptography.fernet import Fernet

file_name = input('Nome do arquivo a ser gerado: ')
pswd = getpass.getpass('Senha a ser criptografada: ')

key = Fernet.generate_key()
cipher_suite = Fernet(key)
ciphered_text = cipher_suite.encrypt(bytes(pswd, 'utf-8'))
with open('key.bin', 'wb') as file_object: file_object.write(key)
with open(file_name + '.bin', 'wb') as file_object: file_object.write(ciphered_text)

print('Senha criptografada!!')
print('\nIMPORTANTE: Utilize a function decrypt_password do modulo decrypt_password.py para descriptografar a senha!')
print('\nATENCAO: Copie os arquivos abaixo para o diretorio do script que a senha sera utilizada: \nkey.bin \n%s' % (file_name + '.bin'))
