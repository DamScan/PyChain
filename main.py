from rsaGenerator import manual


inputs = {
    'passPhrase': input("Enter a Passphrase : "),
    'path': input("Where would you like create key : "),
    'name': input("Give name to you key : "),
}
MG = manual.ManualGen(inputs)
MG.create()
# self._directory()
