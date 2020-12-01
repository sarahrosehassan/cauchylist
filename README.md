# File Encryption 🔒
This project involves scrambling a file's binary code, so that only the people who can crack code with the key can open the original file.

# Opening the Original File
The file that will be encrypted is called plainText. When we open the plainText file, it is is a beautiful image of a wolf.
![1](https://user-images.githubusercontent.com/59797227/100775369-2d87fb80-33d1-11eb-8e50-79b740afe678.png)

This is the wolf file read in binary mode.
![2](https://user-images.githubusercontent.com/59797227/100775485-590ae600-33d1-11eb-94d7-306aae10a202.png)
I want to encrypt this file so that no one is allowed to see the wolf unless they have the key. 

# Encrypting the File
This is the"secret" key which means that in encrypted file, 24 = 0, 68 = 1, 153 = 3, 216 = 4  ...

This is called a permutation encryption scheme.

![3](https://user-images.githubusercontent.com/59797227/100775496-5ad4a980-33d1-11eb-988b-4dc24684842c.png)

With the power of coding, I mapped the plainText to the key, creating a Cipher Text.
The file is no longer a wolf, try cracking this code without the key!
![5](https://user-images.githubusercontent.com/59797227/100775506-5e683080-33d1-11eb-9fb5-f17f923a8330.png)

# Decrypting the File
Since I have the  "secret" key file, I can map the cipherText back to to the key and see the image again.
![6](https://user-images.githubusercontent.com/59797227/100775513-6031f400-33d1-11eb-8709-52b62801a4f9.png)
