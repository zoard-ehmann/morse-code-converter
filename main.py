from morse_converter import MorseConverter


mc = MorseConverter()


def show_info():
    print('\n***********************************************************************************************************************')
    print('')
    print('Plain Text - case insensitive, allowed characters: latin letters, numbers, punctuation characters, whitespaces')
    print('Plain Text Example - "This is a sample text 4 the converter, does this makes sense?"')
    print('Morse Code - space delimited (between letters), allowed characters: dot (.) = dih, dash (-) = dah, slash (/) = space')
    print('Morse Code Example - "... .- -- / .---- ..--- ...-- / .-.-.- -.-.-- ..--.."')
    print('')
    print('***********************************************************************************************************************\n')


show_info()

while True:
    route = input(f'Select action:\n0: Help\n1: Plain Text -> Morse Code\n2: Morse Code -> Plain Text\n9: Stop\nChoice: ')

    if route == '0':
        show_info()
        continue
    elif route == '1':
        result = mc.morse_encode(input('Plain Text: '))
    elif route == '2':
        result = mc.morse_decode(input('Morse Code: '))
    elif route == '9':
        break
    else:
        print('\n!!! Invalid action !!!\n')
        continue

    print(f'\nResult: {result}\n')