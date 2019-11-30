def encrypt(string, shift):
  cipher = ''
  for char in string: 
    if char == ' ':
      cipher = cipher + char
    elif  char.isupper():
      cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
    else:
      cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
  return cipher

def decrypt(string, shift):
  cipher = ''
  for char in string: 
    if char == ' ':
      cipher = cipher + char
    elif  char.isupper():
      cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
    else:
      cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
  return cipher

text = input("\nEnter message to encrypt: ")
s = int(input("Enter key: "))
print("\nEncrypted message: ", encrypt(text, s))

text = input("\nEnter message to decrypt: ")
s = int(input("Use negative number for the key to decrypt: "))
print("\nDerypted message: ", decrypt(text, s))
