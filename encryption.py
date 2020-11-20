def encrypt(plainText, key):
    key = tuple(key)
    plainText = tuple(plainText)
    cipherTextList = []
    for plainTextCharacter in plainText:
        cipherTextList.append(key.index(plainTextCharacter)) # map plainText to key
    cipherText = tuple(cipherTextList)
    return cipherText

def decrypt (cipherText, key):
    key = tuple(key)
    cipherText = tuple(cipherText)
    decryptedTextList = []
    for cipherTextCharacter in cipherText:
        decryptedTextList.append(key[cipherTextCharacter]) # map cipherText to key
    decryptedText = tuple(decryptedTextList)
    return decryptedText

def readFile(fileName):
  openFileInBinaryMode = open(fileName, 'rb').read()
  return openFileInBinaryMode

def writeFile(fileName, content):
  content = bytes(content)
  newBinaryFile = open(fileName, "wb")
  newBinaryFile.write(content)
  newBinaryFile.close()
  return newBinaryFile
