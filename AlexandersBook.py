

def Runic_encoder(reg_text):
    char_dict = get_AlexandersBookDict('Runes')
    char_array = list(reg_text.upper())
    runic_text = ''
    for char in char_array:
        runic_text += char_dict.get(char, '')
    
    print("Encoded Runic Text: ", runic_text)

def Runic_decoder(runic_text):
    english_dict = get_AlexandersBookDict('Common')
    runic_array = list(runic_text)
    decoded_text = ''
    for rune in runic_array:
        decoded_text += english_dict.get(rune, '')
    print("Decoded Text: ", decoded_text)

def get_AlexandersBookDict(input_type):
    if input_type == 'Common':
        dictionary = {
            'ᚨ': 'A',
            'ᛒ': 'B',   
            'ᚲ': 'C',
            'ᛞ': 'D',
            'ᛖ': 'E',
            'ᚠ': 'F',
            'ᚷ': 'G',
            'ᚺ': 'H',
            'ᛁ': 'I',
            'ᛃ': 'J',
            'ᚲ': 'K',
            'ᛚ': 'L',
            'ᛗ': 'M',
            'ᚾ': 'N',
            'ᛟ': 'O',
            'ᛈ': 'P',
            'ᛩ': 'Q',
            'ᚱ': 'R',
            'ᛋ': 'S',
            'ᛏ': 'T',
            'ᚢ': 'U',
            'ᚡ': 'V',
            'ᚹ': 'W',
            'ᛪ': 'X',
            'ᛇ': 'Y',
            'ᛉ': 'Z',
            ' ': ' '
        }
    elif input_type == 'Runes':
        dictionary = {
            'A': 'ᚨ',
            'B': 'ᛒ',   
            'C': 'ᚲ',
            'D': 'ᛞ',
            'E': 'ᛖ',
            'F': 'ᚠ',
            'G': 'ᚷ',
            'H': 'ᚺ',
            'I': 'ᛁ',
            'J': 'ᛃ',
            'K': 'ᚲ',
            'L': 'ᛚ',
            'M': 'ᛗ',
            'N': 'ᚾ',
            'O': 'ᛟ',
            'P': 'ᛈ',
            'Q': 'ᛩ',
            'R': 'ᚱ',
            'S': 'ᛋ',
            'T': 'ᛏ',
            'U': 'ᚢ',
            'V': 'ᚡ',
            'W': 'ᚹ',
            'X': 'ᛪ',
            'Y': 'ᛇ',
            'Z': 'ᛉ',
            ' ': ' '
        }

    return dictionary


def AlexandersBook():
    # Take input from the user
    user_input = input("Welcome to the Book of Alexander, select an option:\n1. Encode your language to runes\n2. Decode a set of runes\nEnter 1 or 2: ")
    if user_input == '1':
        text_to_encode = input("Enter the text you want to encode: ")
        Runic_encoder(text_to_encode)
        
    elif user_input == '2':
        Runes_to_decode = input("Enter the runes you want to decode: ")
        Runic_decoder(Runes_to_decode)
    else:
        print("Invalid option selected. Try again\n")
        AlexandersBook()

if __name__ == "__main__":
    AlexandersBook()
