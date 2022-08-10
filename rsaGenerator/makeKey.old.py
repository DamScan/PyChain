from Crypto.PublicKey import RSA
import os

passPhrase = input("Enter a Passphrase : ")
path = input("Where would you like create key : ")
name = input("Give name to you key : ")
key = RSA.generate(2048)
encrypted_key = key.export_key(passphrase=passPhrase, pkcs=8, protection="scryptAndAES128-CBC")

if not os.path.exists(f"./{path}"):
    os.mkdir(os.path.join("../", path))
file_out = open(f"{path}/{name}.pem", "wb")
file_out.write(encrypted_key)
file_out.close()

encoded_key = open(f"{path}/{name}.pem", "rb").read()
key = RSA.import_key(encoded_key, passphrase=passPhrase)
file_out = open(f"{path}/{name}_pub.pem", "wb")
file_out.write(key.publickey().export_key())
file_out.close()
print(key.publickey().export_key())
