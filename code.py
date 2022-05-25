import base64
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import hashlib

text_file = open("tekst1.txt", "rb")

text_file = text_file.read()

output = hashlib.sha3_256()
output.update(text_file)

print(output.digest())

def toBase64(string):
    return base64.b64encode(string)
def generate_keys():
    modulus_length = 256*4
    private_key = RSA.generate(modulus_length, Random.new().read)
    public_key = private_key.publickey()
    return private_key, public_key

pri, pub = generate_keys()

text_file_2 = open("tekst2.txt", "rb")
text_file_2 = text_file_2.read()

output_2 = hashlib.sha3_256()
output_2.update(text_file_2)

print(output_2.digest())

cipher = PKCS1_OAEP.new(pub)
M = cipher.encrypt(text_file)
print(M, "\n")

cipher = PKCS1_OAEP.new(pri)
m = cipher.decrypt(M)
print(m, "\n")
    
""" Convert hash to hexigest string """
    
hex_dig = output.hexdigest()
print(hex_dig)
hex_dig2 = output_2.hexdigest()
print(hex_dig2)

""" VALIDATION """
if hex_dig == hex_dig2:
    print("It's ok")
    cipher = PKCS1_OAEP.new(pri)
    m = cipher.decrypt(M)
    
    print(m, "\n")
else:
    print("error!")

