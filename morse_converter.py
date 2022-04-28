import re

from morse_loader import MorseLoader


class MorseConverter():

    def __init__(self):
        """Responsible for encoding and decoding morse characters.
        """
        self.morse_table = MorseLoader().data
        self.morse_re = re.compile('^[\-\.]+$')

    def morse_encode(self, inp:str) -> str:
        """Encodes plain text into morse code.

        Args:
            inp (str): Plain text input.

        Returns:
            str: Morse code equialent of plain text input.
        """
        morse_code = ""

        for char in inp.upper():
            if char.isspace():
                morse_code += '/'
            else:
                try:
                    morse_code += self.morse_table[char]
                except KeyError:
                    return f'!!! Invalid input: {char} !!!'
            morse_code += ' '

        return morse_code

    def morse_decode(self, inp:str) -> str:
        """Decodes morse code into plain text.

        Args:
            inp (str): Morse code input.

        Returns:
            str: Plain text equialent of morse code input.
        """
        plain_text = ""

        for char in inp.split():
            if char == '/':
                plain_text += ' '
            elif self.morse_re.match(char):
                for letter, code in self.morse_table.items():
                    if code == char:
                        plain_text += letter
                        break
            else:
                return f'!!! Invalid input: {char} !!!'
        
        return plain_text
