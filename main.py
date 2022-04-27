from morse_loader import MorseLoader


morse_table = MorseLoader().data

plain_text = input('Enter the plain text: ').upper()

morse_code = ""
for char in plain_text:
    morse_code = ' '.join([morse_code, morse_table[char]])

print(f'Morse code: {morse_code}')