from Crypto.PublicKey import RSA

secret_code = "PyChain"
key = RSA.generate(2048)
encrypted_key = key.export_key(passphrase=secret_code, pkcs=8, protection="scryptAndAES128-CBC")

file_out = open("key/genesisPrivate.pem", "wb")
file_out.write(encrypted_key)
file_out.close()

encoded_key = open("key/genesisPrivate.pem", "rb").read()
key = RSA.import_key(encoded_key, passphrase=secret_code)
file_out = open("key/genesisPublic.pem", "wb")
file_out.write(key.publickey().export_key())
file_out.close()
print(key.publickey().export_key())
