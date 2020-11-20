import encryption

def testEncryption():
  # 1.
  key = encryption.readFile('key')

  # 2.
  plainText = encryption.readFile('plainText')
  cipherText = encryption.encrypt(plainText, key)

  # 3.
  cipherText = encryption.writeFile('cipherText', cipherText)
  cipherText = encryption.readFile('cipherText')

  # 4.
  cipherText = encryption.readFile('cipherText')
  decryptedText = encryption.decrypt (cipherText, key)

  # 5.
  decryptedText = encryption.writeFile('plainText1', decryptedText)
  decryptedText = encryption.readFile('plainText1')
  
testEncryption()