import encryption

def testEncryption():
  key = encryption.readFile('key')

  plainText = encryption.readFile('plainText')
  cipherText = encryption.encrypt(plainText, key)

  cipherText = encryption.writeFile('cipherText', cipherText)
  cipherText = encryption.readFile('cipherText')

  cipherText = encryption.readFile('cipherText')
  decryptedText = encryption.decrypt (cipherText, key)

  decryptedText = encryption.writeFile('plainText1', decryptedText)
  decryptedText = encryption.readFile('plainText1')
  
testEncryption()
