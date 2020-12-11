# This is a game of secret words, called Caesar Cipher.
# Written by: Thu Aung
# Written on: Dec 10, 2020

print("Welcome to Caesar Cipher.\n")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher(ori_text, shift_amount, shift_dir):
  # Create an empty string for final text.
  final_text = ''

  if shift_dir == 'decode':
    # For decoding, final_position will be subtracted from position.
    shift_amount *= -1

  for char in ori_text:
    # Check if the char is in alphabet.
    if char in alphabet:
      # Get position of char.
      position = alphabet.index(char)
      # Get new_pos by adding shift_amount.
      new_position = position + shift_amount
      # Add char at new_pos to final_text.
      final_text += alphabet[new_position]

    # If char is not in alphabet, it won't be changed.
    else:
      final_text += char

  print(f"The {shift_dir}d text is '{final_text}'.")

game_on = True
while game_on:
  # Get text to be changed.
  text = input("Please enter the text.\n")
  # Get how many pos a user wants to shift.
  shift = int(input("How many position do you want to shift?\n"))
  # Get direction of shift.
  direction = input("Please choose to encode or decode.\n")

  # Just in case, a user enters numbers greater than numbers of alphabets.
  shift = shift % 26
  caesar_cipher(ori_text = text, shift_amount = shift, shift_dir = direction)

  choice = input("Wanna play again? Yes or No:\n").lower()
  if choice == 'no':
    print("Thanks for playing this game.\nBye.")
    game_on = False