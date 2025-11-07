import time
import os

Truth = "The man with a Golden Eye sees all."
Watcher_link = "www.TheLinkisntReadyYet.com"
Kealith_link = "https://www.youtube.com/watch?v=Q6v3KjTcIKA"
cat_link = "https://www.youtube.com/watch?v=IxX_QHay02M"

golden_seal_pass1 = False # shadow 
golden_seal_pass2 = False # coffin 
golden_seal_pass3 = False # dream
golden_seal_pass4 = False # dawn
complete = False
FoundWatcher = False
FoundKaelith = False
Found = False


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
    global complete
    global Found
    global FoundKaelith
    global FoundWatcher
    # clears terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    # Take input from the user
    print("Welcome to the Book of Alexander, select an option:" \
        "\n1. What is the Book of Alexander?" \
        "\n2. Encode Common language" \
        "\n3. Decode to Common language" \
        "\n4. View Dictionaries" \
        "\n5. Inspect Golden Seal?")
    
    if complete == True: 
        print("ERR0R EX1ST3NC3: The Golden Seal has been broken.")
        print("ERRPR0C3SS1NG: Further inspection may reveal more secrets.")
        print("ERRORRF3V34L1NG: There is more to uncover within the Book of Alexander.")
        print("ERR0R4SS1ST4NC3: Truth is required to access further secrets.")
        print("6. Seek Truth")
    if Found == True:
        print("7. Uncovered secrets")    
    
    print("Enter a number or enter 0 to close the book: ")
    user_input = input()

     # +++++++++++++++++++++++++++++++++++++++++++++++++++
    if user_input == '001':
        DevMode()  

    # ++++++++++++++++++++++++++++++++++++++++++++++++++

    if user_input == 'cat':
        print("You found the hidden cat link! Enjoy!\n", cat_link)
        print("Do you wish to return to the main menu? (Y/N): \n")
        if input().upper() == 'Y': AlexandersBook()
        else: return

    if user_input == '0':
        print("Closing the Book of Alexander. Goodbye!")
        return
    elif user_input == '1': # What is the Book of Alexander
        print("Alexander’s Book is a mysterious and ancient artifact said to contain forbidden knowledge and untold wisdom, gathered from countless realms and ages.")
        print("Bound in dark, weathered leather etched with glowing runes, the book hums with a quiet, otherworldly energy. Legends tell that it was written by Alexander,")
        print("a scholar who sought to understand the fabric of existence itself — but at a terrible cost. Within its pages lie truths that can grant immense power or bring ruin to those unprepared to comprehend them.")
        print("Many have sought the book, drawn by its promise of enlightenment, yet few have opened it and remained unchanged. Some say the book chooses its readers, revealing its secrets only to those deemed worthy.")

        print("Do you wish to return to the main menu? (Y/N): \n")
        if input().upper() == 'Y': AlexandersBook()
        else: return
        AlexandersBook()
    elif user_input == '2': # Cipher from Common
        Cipher()
    elif user_input == '3': # Dechiper to Common
        Decipher()
    elif user_input == '4': # View Dictionaries
        print("Common to Runes Dictionary: ", get_AlexandersBookDict('Runes','Runes'))
        print("Common to Dwarven Dictionary: ", get_AlexandersBookDict('Dwarven','Dwarven'), "\n")
        print("Do you wish to return to the main menu? (Y/N): \n")
        if input().upper() == 'Y': AlexandersBook()
        else: return
    elif user_input == '5': # Inspect Golden Seal
        print("The Golden seal glows with energy...")
        GoldenSeal()
    elif user_input == '6' and complete == True: # Seek Truth
        os.system('cls' if os.name == 'nt' else 'clear')
        print("ERROR: SEEK TRUTH SEQUENCE INITIATED...\n")
        tt = """ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR
                ERROR ER1OR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR
                ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR
                ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR
                ERROR ERROR ERROR ERROR ERROR ERR1R ERROR ERROR ERROR ERROR ERROR
                ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR
                ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR
                ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR
                ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR
                ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR
                ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR
                ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR
                ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR
                ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR
                ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR
                ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR
                ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR
                ERROR ERROR 2RROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR
                ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ER7OR ERROR
                ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR
                \n"""
        
        print(tt)
        print("Do you wish to return to the main menu? (Y/N): \n")
        if input().upper() == 'Y': AlexandersBook()
        else: return
    if user_input == '7' and Found == True: # Uncovered secrets
        os.system('cls' if os.name == 'nt' else 'clear')
        if FoundKaelith == True:
            print("You have already uncovered the secrets of Kaelith.\n")
            print(Kealith_link, "\n")
        if FoundWatcher == True:
            print("You have already uncovered the secrets of The Watcher.\n")
            print(Watcher_link, "\n")
        print("Do you wish to return to the main menu? (Y/N): \n")
        if input().upper() == 'Y': AlexandersBook()
    else:
        print("Invalid option selected. Try again\n")
        AlexandersBook()

def GoldenSeal():
    global golden_seal_pass1
    global golden_seal_pass2
    global golden_seal_pass3
    global Kealith_link
    global Watcher_link
    global complete
    global FoundKaelith
    global Found
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # If seal is already complete, trigger secret code path.
    if complete == True:
        os.system('cls' if os.name == 'nt' else 'clear')
        task = "The Golden Seal has already been broken. There may be more secrets hidden within...\n" \
                "However, you feel a strange presence watching you...\n"
        for word in task:
            print(word, end='', flush=True)
            time.sleep(0.07)
        print("ERROR: UNAUTHORIZED PRESENCE DETECTED...\n")
        userInput = input("ERROR: Sequence requires initialized code to proceed? \n")
        if userInput == '1127':
            TheWatcherPath()
        else:
            print("The presence fades away...")
            time.sleep(5)
            AlexandersBook()
    # ===========================================================================

    if complete == False:
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
            c1 = ""
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
            c2 = ""
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
            c3 = ""
        golden_seal_pass3 = True # Save phrase
        # ===========================================================================
    
        challenge_4 = "\nThe Golden seal flows with energy outwards, you can feel holy radiance flow over you.\nHealing your old wounds, making you feel stronger. It awaits the final phrase. "
        for word in challenge_4:
                print(word, end='', flush=True)
                time.sleep(0.07)
        userInput = input()
        if userInput.lower() != 'dawn':
            print("\n Come what may, you will prevail. Try again.")
            time.sleep(5)
            AlexandersBook()
        golden_seal_pass4 = True # Save phrase
        # ===========================================================================

        if golden_seal_pass1 and golden_seal_pass2 and golden_seal_pass3 and golden_seal_pass4 == True: complete = True
        if complete == True:
            time.sleep(5)
            os.system('cls' if os.name == 'nt' else 'clear')
            Kaelith = "\nMay Shadow fade away, May his Coffin be beared, May today be a Dream, May the Dawn light my way. \n"
            for word in Kaelith:
                print(word, end='', flush=True)
                time.sleep(0.07)
            print(Kealith_link, "\n")
            Found = True
            FoundKaelith = True
            print("\nThe seal has been broken. You may now proceed further should you choose to.\n")
            print("Do you wish to return to the main menu? (Y/N): \n")
            if input().upper() == 'Y': AlexandersBook()
            else: return

def TheWatcherPath():
    global Truth
    global FoundWatcher
    os.system('cls' if os.name == 'nt' else 'clear')
    
    enc1 = "A Watchful Eye looms over you..."
    for word in enc1:
        print(word, end='', flush=True)
        time.sleep(0.07)
    
    time.sleep(3)

    enc2 = "\nIf you are truly here on purpose, recite the phrase of truth."
    for word in enc2:
        print(word, end='', flush=True)
        time.sleep(0.07)

    userInput = input("\nRecite the Truth.\n") # Hint: Print the Truth in console
    if userInput.lower() == Truth.lower():
        words1 = "The truth unveild. There isnt much time..."
        for word in words1:
            print(word, end='', flush=True)
            time.sleep(0.07)
        print("\n\nSomething beyond what you can see...")
        print("Is unlocking it...")

        time.sleep(7)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Warning!!! Illusion matter diagnostics are failing...")
        time.sleep(7)
        print('Warning!!! Perception of self is increasing!!!')
        print('Recommend running SystemRESET() IMMEDIATELY!!!')
        time.sleep(10)
        print("Attempting to run SystemRESET() Standby...")
        time.sleep(5)
        print("SystemRESET() Failed. Illusion matter integrity compromised.")
        time.sleep(5)
        print("WARNING!!! EXISTENCE STABILITY AT 0.7%")
        time.sleep(5)
        print("FINAL WARNING!!! RECOMMEND IMMEDIATE EXIT FROM PROGRAM!!!")
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
        warnings = "Error "
        for _ in range(200):
            print(warnings)
        
        # I found you.
        print("\n")
        print("ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR")
        print(Watcher_link)
        print("ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR ERROR\n")
        print("Do you wish to return to the main menu? (Y/N): \n")
        FoundWatcher = True
        if input().upper() == 'Y': AlexandersBook()
        else: return
    
def DevMode():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Cheat code accepted. Bypassing Golden Seal...\n")
    global golden_seal_pass1
    global golden_seal_pass2
    global golden_seal_pass3
    global Kealith_link
    global Watcher_link
    global complete
    global FoundKaelith
    global FoundWatcher
    global Found
    print("Welcome Connor! You have entered Dev Mode.\n")
    print("Here are the list of cheats :)\n")
    print("1. Break Golden Seal ", str(complete))
    print("2. Find The Watcher ", str(FoundWatcher))
    print("Enter 0 to exit Dev Mode.\n")
    userInput = input("Enter a number to activate a cheat: \n")
    
    # Break Golden Seal cheat + Kaelith unlock
    if userInput == '1':
        if complete == True:
            print("Golden Seal is already broken.\n")
            time.sleep(3)
            DevMode()
        else:
            print("Breaking Golden Seal...\n")
            golden_seal_pass1 = True
            golden_seal_pass2 = True
            golden_seal_pass3 = True
            golden_seal_pass4 = True
            complete = True
            time.sleep(7)
            DevMode()
    
    # The Watcher cheat
    elif userInput == '2':
        if FoundWatcher == True:
            print("The Watcher is already found.\n")
            time.sleep(3)
            DevMode()
        else:
            print("Finding The Watcher...\n")
            FoundWatcher = True
            Found = True
            time.sleep(7)
            DevMode()
    elif userInput == '0':
        print("Exiting Dev Mode...\n")
        time.sleep(3)
        AlexandersBook() 

if __name__ == "__main__":
    AlexandersBook()
