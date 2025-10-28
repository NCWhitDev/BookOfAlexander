import time
import os

Truth = "Infinity isnt without its flaws, undeying, unyeilding. We were chosen. To extingush shadows, to defy our fate. To bring it forth, shattered it may be. For you, This is a game, yet here you still play, but not as players...as pawns."
Watcher_link = ""
Kealith_link = ""

golden_seal_pass1 = False # shadow 
golden_seal_pass2 = False # coffin 
golden_seal_pass3 = False # dream
golden_seal_pass4 = False # dawn
complete = 0

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
    global golden_seal_pass1
    global golden_seal_pass2
    global golden_seal_pass3
    # clears terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    # Take input from the user
    print("Welcome to the Book of Alexander, select an option:" \
        "\n1. What is the Book of Alexander?" \
        "\n2. Encode Common language" \
        "\n3. Decode to Common language" \
        "\n4. View Dictionaries" \
        "\n5. Inspect Golden Seal?" \
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
    elif user_input == '5':
        print("The Golden seal glows with energy...")
        GoldenSeal(0)
    elif user_input == '1127':
        GoldenSeal(1127)
    else:
        print("Invalid option selected. Try again\n")
        AlexandersBook()

def GoldenSeal(secretCode):
    global golden_seal_pass1
    global golden_seal_pass2
    global golden_seal_pass3
    global Kealith_link
    global Watcher_link
    

    # Start of seal mechanism.
    challenge_1 = "\nThe Golden seal sits still...awaiting a phrase. "
    for word in challenge_1:
            print(word, end='', flush=True)
            time.sleep(0.07)

    if golden_seal_pass1 == False:
        userInput = input()
        if userInput.lower() != 'shadow':
            print("\nThe seal denys you.")
            time.sleep(5)
            AlexandersBook()
    golden_seal_pass1 = True # Save phrase
    # ===========================================================================

    
    challenge_2 = "\nThe Golden seal begins to faintly glow...It awaits the next phrase. "
    for word in challenge_2:
            print(word, end='', flush=True)
            time.sleep(0.07)

    if golden_seal_pass2 == False:
        userInput = input()
        if userInput.lower() != 'coffin':
            print("\nYou're past actions have been saved. The seal denys you any further. ")
            time.sleep(5)
            AlexandersBook()
    golden_seal_pass2 = True # Save phrase
    # ===========================================================================

    
    challenge_3 = "\nThe Golden seal glows brighter...It awaits the next phrase. "
    for word in challenge_3:
            print(word, end='', flush=True)
            time.sleep(0.07)

    if golden_seal_pass3 == False:
        userInput = input()
        if userInput.lower() != 'dream':
            print("\nYou're past actions have been saved. The seal denys you any further.")
            time.sleep(5)
            AlexandersBook()
    golden_seal_pass3 = True # Save phrase
    # ===========================================================================

    
    challenge_4 = "\nThe Golden seal flows with energy outwards, you can feel holy radiance flow over you.\n Healing your old wounds, making you feel stronger. It awaits the final phrase. "
    for word in challenge_4:
            print(word, end='', flush=True)
            time.sleep(0.07)
    userInput = input()

    if userInput.lower() != 'dawn':
        print("\nYou are so close...Try again.")
        time.sleep(5)
        AlexandersBook()
    golden_seal_pass4 = True # Save phrase
    # ===========================================================================

    if golden_seal_pass1 and golden_seal_pass2 and golden_seal_pass3 and golden_seal_pass4 == True: complete = 1
    if complete == 1:
        time.sleep(5)
        Kaelith = "\nLet Shadow fade away, May his Coffin be beared, May today be a Dream, Let the Dawn light my way. \n"
        for word in Kaelith:
            print(word, end='', flush=True)
            time.sleep(0.07)
        print(Kealith_link)
        return


    # =======================================================
    # Secret start of seal mechanism
    if secretCode == 1127:
        enc1 = "A Watchful Eye looms over you..."
        for word in enc1:
            print(word, end='', flush=True)
            time.sleep(0.07)

        time.sleep(3)

        enc2 = "\nIf you are truly here on purpose, recite the phrase of truth."
        for word in enc2:
            print(word, end='', flush=True)
            time.sleep(0.07)

        userInput = input("\nRecite the Truth.\n") # Hint: Print Truth in Py console
        if userInput == Truth:
            words1 = "The truth unveild. There isnt much time..."
            for word in words1:
                print(word, end='', flush=True)
                time.sleep(0.07)
            print("\n\nSomething beyond what you can see...")
            print("Is unlocking it...")

            time.sleep(7)
            print("Warning!!! Illusion matter diagnostics are failing...")
            time.sleep(7)
            print('Warning!!! Perception of self is increasing!!!')
            print('Recommend running SystemRESET() IMMEDIATELY!!!')
            time.sleep(10)
            print("Attempting to run SystemRESET() Standby...")
            warnings = "Error "
            for _ in range(200):
                print(warnings)
            
            # I found you.
            print("\n")
            print(Watcher_link)


if __name__ == "__main__":
    AlexandersBook()
