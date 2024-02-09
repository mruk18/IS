# def encrypt_rail_fence(message, key):
#   fence = [['' for _ in range(len(message))] for _ in range(key)]
#   rail, direction = 0, 1

#   for i in range(len(message)):
#       fence[rail][i] = message[i]
#       rail += direction

#       if rail == key - 1 or rail == 0:
#           direction = -direction

#   encrypted_message = ''.join([''.join(row) for row in fence])
#   return encrypted_message

# def decrypt_rail_fence(ciphertext, key):
#   fence = [['' for _ in range(len(ciphertext))] for _ in range(key)]
#   rail, direction = 0, 1

#   for i in range(len(ciphertext)):
#       fence[rail][i] = 'X'  # Placeholder for the encrypted characters
#       rail += direction

#       if rail == key - 1 or rail == 0:
#           direction = -direction

#   index = 0
#   for i in range(key):
#       for j in range(len(ciphertext)):
#           if fence[i][j] == 'X':
#               fence[i][j] = ciphertext[index]
#               index += 1

#   rail, direction = 0, 1
#   decrypted_message = ''
#   for i in range(len(ciphertext)):
#       decrypted_message += fence[rail][i]
#       rail += direction

#       if rail == key - 1 or rail == 0:
#           direction = -direction

#   return decrypted_message

# # Example usage:
# message = "thankyouverymuch"
# key = 3

# encrypted_message = encrypt_rail_fence(message, key)
# print(f'Encrypted message: {encrypted_message}')

# decrypted_message = decrypt_rail_fence(encrypted_message, key)
# print(f'Decrypted message: {decrypted_message}')




def encrypt_rail_fence(message, key):
  # Remove spaces from the message
  message = message.replace(" ", "")

  fence = [['' for _ in range(len(message))] for _ in range(key)]
  rail, direction = 0, 1

  for i in range(len(message)):
      fence[rail][i] = message[i]
      rail += direction

      if rail == key - 1 or rail == 0:
          direction = -direction

  encrypted_message = ''.join([''.join(row) for row in fence])
  return encrypted_message

def decrypt_rail_fence(ciphertext, key):
  fence = [['' for _ in range(len(ciphertext))] for _ in range(key)]
  rail, direction = 0, 1

  for i in range(len(ciphertext)):
      fence[rail][i] = 'X'  # Placeholder for the encrypted characters
      rail += direction

      if rail == key - 1 or rail == 0:
          direction = -direction

  index = 0
  for i in range(key):
      for j in range(len(ciphertext)):
          if fence[i][j] == 'X':
              fence[i][j] = ciphertext[index]
              index += 1

  rail, direction = 0, 1
  decrypted_message = ''
  for i in range(len(ciphertext)):
      decrypted_message += fence[rail][i]
      rail += direction

      if rail == key - 1 or rail == 0:
          direction = -direction

  return decrypted_message

# Example usage:
message_with_spaces = "Thank you very much"
key = 3

encrypted_message = encrypt_rail_fence(message_with_spaces, key)
print(f'Encrypted message: {encrypted_message}')

decrypted_message = decrypt_rail_fence(encrypted_message, key)
print(f'Decrypted message: {decrypted_message}')
