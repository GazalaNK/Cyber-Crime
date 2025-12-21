import base64
import string
string1=input("Enter the string:")
byte1=string1.encode('ascii')
byte2=base64.b64encode(byte1)
print("The encrypted string is:",byte2)
decrypt_byte=base64.b64decode(byte2)
decrypt_string=decrypt_byte.decode('ascii')
print("The decrypted string is:",decrypt_string)
