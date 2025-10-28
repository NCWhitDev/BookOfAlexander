import time
import os

def Common_decoder(language, text):
    english_dict = get_AlexandersBookDict(language,'Common')
    text_array = list(text)
    decoded_text = ''
    for char in text_array:
        decoded_text += english_dict.get(char, '')
    if language == 'Dwarven':
        print("Decoded Dwarven Text: ", decoded_text)
        print("Do you wish to use this decoded text for further decoding? (Y/N): \n")
        if input().upper() == 'Y': AlexandersBook()
        else: return
        
    elif language == 'Runes':
        print("Decoded Runic Text: ", decoded_text)
        print("Do you wish to use this decoded text for further decoding? (Y/N): \n")
        if input().upper() == 'Y': AlexandersBook()
        else: return

# ========================================================================================================== Fantasy Language Encoders =====================================================================================================================
def Runic_encoder(Common_text):
    char_dict = get_AlexandersBookDict('Runes', 'Runes')
    char_array = list(Common_text.upper())
    runic_text = ''
    for char in char_array:
        runic_text += char_dict.get(char, '')
    print("Encoded Runic Text: ", runic_text)   
    print("Do you wish to use this decoded text for further decoding? (Y/N): \n")
    if input().upper() == 'Y': AlexandersBook()
    else: return


def Dwarven_encoder(Common_text):
    dwarven_dict = get_AlexandersBookDict('Dwarven', 'Dwarven')
    dwarven_array = list(Common_text.upper())
    decoded_text = ''
    for char in dwarven_array:
        decoded_text += dwarven_dict.get(char, '')
    print("Decoded Dwarven Text: ", decoded_text)
    print("Do you wish to use this decoded text for further decoding? (Y/N): \n")
    if input().upper() == 'Y': AlexandersBook()
    else: return

# ====================================================================================================== End of Fantasy Language Encoders ==================================================================================================================

def get_AlexandersBookDict(language, input_type):
    if input_type == 'Common':
        if language == 'Dwarven':
            # Dwarven to Common
            dictionary = {
                '𐑨' : 'A',
                '𐑩' : 'B',
                '𐑪' : 'C',
                '𐑫' : 'D',
                '𐑬' : 'E',
                '𐑭' : 'F',
                '𐑮' : 'G',
                '𐑯' : 'H',
                '𐑰' : 'I',
                '𐑱' : 'J',
                '𐑲' : 'K',
                '𐑳' : 'L',
                '𐑴' : 'M',
                '𐑵' : 'N',
                '𐑶' : 'O',
                '𐑷' : 'P',
                '𐑸' : 'Q',
                '𐑹' : 'R',
                '𐑺' : 'S',
                '𐑻' : 'T',
                '𐑼' : 'U',
                '𐑽' : 'V',
                '𐑾' : 'W',
                '𐑿' : 'X',
                '𐒀' : 'Y',
                '𐒁' : 'Z',
                ',': ',',
                '.': '.',
                ' ': ' ',
                '?': '?'
            }
        elif language == 'Runes':
            # Runes to Common
            dictionary = {
                'ᔑ': 'A',
                'ꖌ': 'B',   
                '⋮': 'C',
                '⎓': 'D',
                'リ': 'E',
                'ᓵ': 'F',
                '↸': 'G',
                'ꖎ': 'H',
                '⊣': 'I',
                'ℸ': 'J',
                '╎': 'K',
                '∷': 'L',
                'ᒷ': 'M',
                'ᒲ': 'N',
                't': 'O',
                '!': 'P',
                '⚍': 'Q',
                '+': 'R',
                'ʖ': 'S',
                'T': 'T',
                '∴': 'U',
                'x': 'V',
                'ᓭ': 'W',
                '⍑': 'X',
                'ノ': 'Y',
                '⍊': 'Z',
                ',': ',',
                '.': '.',
                ' ': ' ',
                '?': '?'
            }

    elif input_type == 'Runes':
        # Common to Runes
        dictionary = {
            'A': 'ᔑ',
            'B': 'ꖌ',   
            'C': '⋮',
            'D': '⎓',
            'E': 'リ',
            'F': 'ᓵ',
            'G': '↸',
            'H': 'ꖎ',
            'I': '⊣',
            'J': 'ℸ',
            'K': '╎',
            'L': '∷',
            'M': 'ᒷ',
            'N': 'ᒲ',
            'O': 't',
            'P': '!',
            'Q': '⚍',
            'R': '+',
            'S': 'ʖ',
            'T': 'T',
            'U': '∴',
            'V': 'x',
            'W': 'ᓭ',
            'X': '⍑',
            'Y': 'ノ',
            'Z': '⍊',
            ',': ',',
            '.': '.',
            ' ': ' ',
            '?': '?'
        }

    elif input_type == 'Dwarven':
        # Common to Dwarven
        dictionary = {
            'A': '𐑨',
            'B': '𐑩',   
            'C': '𐑪',
            'D': '𐑫',
            'E': '𐑬',
            'F': '𐑭',
            'G': '𐑮',
            'H': '𐑯',
            'I': '𐑰',
            'J': '𐑱',
            'K': '𐑲',
            'L': '𐑳',
            'M': '𐑴',
            'N': '𐑵',
            'O': '𐑶',
            'P': '𐑷',
            'Q': '𐑸',
            'R': '𐑹',
            'S': '𐑺',
            'T': '𐑻',
            'U': '𐑼',
            'V': '𐑽',
            'W': '𐑾',
            'X': '𐑿',
            'Y': '𐒀',
            'Z': '𐒁',
            ',': ',',
            '.': '.',
            ' ': ' ',
            '?': '?'
        }
    
    return dictionary

def Decipher():
    print("What type of Conversion do you want to make?"
            "\n1. Runes to Common"
            "\n2. Dwarven to Common" 
            "\nEnter a number: ")
    
    decode_input = int(input())
    
    if decode_input == 1:
        Runes_to_decode = input("Enter the runes you want to decode: ")
        Common_decoder('Runes', Runes_to_decode)
    elif decode_input == 2:
        Dwarven_to_decode = input("Enter the Dwarven words you want to decode: ")
        Common_decoder('Dwarven', Dwarven_to_decode)
    else:
        print("Invalid option selected. Try again\n")
        Decipher()

def Cipher():
    text_to_encode = input("Enter the Common words you wish to convert: ")
    print("What type of Conversion do you want to make?" \
        "\n1. Common to Runes" \
        "\n2. Common to Dwarven" \
        "\nEnter a number: ")
    
    encode_input = int(input())
    if encode_input == 1:
        Runic_encoder(text_to_encode)
    elif encode_input == 2:
        Dwarven_encoder(text_to_encode)
    else:
        print("Invalid option selected. Try again\n")
        Cipher()

def AlexandersBook():
    # clears terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    # Take input from the user
    print("Welcome to the Book of Alexander, select an option:" \
        "\n1. What is the Book of Alexander?" \
        "\n2. Encode Common language" \
        "\n3. Decode to Common language" \
        "\n4. View Dictionaries" \
        "\nEnter a number or enter 0 to close the book: ")
    user_input = input()

    if user_input == '0':
        print("Closing the Book of Alexander. Goodbye!")
        return
    elif user_input == '1': # What is the Book of Alexander
        print("The Book of Alexander is a mystical book.\n")
        AlexandersBook()
    elif user_input == '2': # Cipher from Common
        Cipher()
    elif user_input == '3': # Dechiper to Common
        Decipher()
    elif user_input == '4': # View Dictionaries
        print("Common to Runes Dictionary: ", get_AlexandersBookDict('Runes','Runes'))
        print("Common to Dwarven Dictionary: ", get_AlexandersBookDict('Dwarven','Dwarven'), "\n")
        AlexandersBook()
    else:
        print("Invalid option selected. Try again\n")
        AlexandersBook()

if __name__ == "__main__":
    AlexandersBook()
