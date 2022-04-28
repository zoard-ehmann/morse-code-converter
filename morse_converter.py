from morse_loader import MorseLoader


class MorseConverter():

    def __init__(self):
        self.morse_table = MorseLoader().data

    def morse_encode(self, inp):
        morse_code = ""

        for char in inp.upper():
            if char.isspace():
                morse_code += '/'
            else:
                morse_code += self.morse_table[char]
            morse_code += ' '

        return morse_code

    def morse_decode(self, inp):
        plain_text = ""

        for char in inp.split():
            if char == '/':
                plain_text += ' '
            else:
                for letter, code in self.morse_table.items():
                    if code == char:
                        plain_text += letter
                        break
        
        return plain_text
