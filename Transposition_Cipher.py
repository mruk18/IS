def encrypt(message, key):
  # Remove spaces and convert message to uppercase
  message = message.replace(" ", "").upper()

  # Calculate the number of columns based on the key length
  num_columns = len(key)

  # Calculate the number of rows needed
  num_rows = -(-len(message) // num_columns)

  # Add padding to the message if needed
  message += "X" * (num_rows * num_columns - len(message))

  # Create a matrix to store the message
  matrix = [list(message[i:i+num_columns]) for i in range(0, len(message), num_columns)]

  # Rearrange the columns based on the key
  encrypted_message = ""
  for col in key:
      encrypted_message += "".join(matrix[row][int(col)-1] for row in range(num_rows))

  return encrypted_message

def decrypt(message, key):
  # Calculate the number of columns based on the key length
  num_columns = len(key)

  # Calculate the number of rows needed
  num_rows = -(-len(message) // num_columns)

  # Create a matrix to store the message
  matrix = [['' for _ in range(num_columns)] for _ in range(num_rows)]

  # Fill the matrix with the encrypted message
  index = 0
  for col in key:
      for row in range(num_rows):
          matrix[row][int(col)-1] = message[index]
          index += 1

  # Reconstruct the decrypted message
  decrypted_message = "".join(matrix[row][col] for row in range(num_rows) for col in range(num_columns))

  return decrypted_message

# Example usage
plaintext = "Kill Corona Virus at tewlve am tomorrow"
key = "4312567"

# Encrypt the message
encrypted_text = encrypt(plaintext, key)
print("Encrypted:", encrypted_text)

# Decrypt the message
decrypted_text = decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)
