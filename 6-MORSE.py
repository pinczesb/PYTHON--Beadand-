import string

DICT_Morse_UpperAndNumbers={'A': '.-', 'B': '-...', 'C': '-.-.','D': '-..', 'E': '.', 'F': '..-.','G': '--.', 'H': '....', 'I': '..','J': '.---', 'K': '-.-', 'L': '.-..','M': '--', 'N': '-.', 'O': '---','P': '.--.', 'Q': '--.-', 'R': '.-.','S': '...', 'T': '-', 'U': '..-','V': '...-', 'W': '.--', 'X': '-..-','Y': '-.--', 'Z': '--..','0': '-----', '1': '.----', '2': '..---','3': '...--', '4': '....-', '5': '.....','6': '-....', '7': '--...', '8': '---..','9': '----.',' ':'/'}
DICT_UpperAndNumbers_Morse = DICT_Morse_UpperAndNumbers([(value,key) for key,value in old_dict.items()])

def ConvertToMorse():
    str2=''
    str=input('String to convert: ')
    for ch in str:
        if ch not in string.punctuation:
            str2+=ch
    for ch2 in str2:
        print(DICT_Morse_UpperAndNumbers[ch2.upper()],'/',end='')

def ConverFromMorse():
    str2=''
    str=ConvertToMorse()
    for ch in str:
        str2+=ch
    for ch2 in str2:
        print(DICT_Morse_UpperAndNumbers[])


