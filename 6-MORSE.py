import string

DICT_Morse_UpperAndNumbers={'A': '.-', 'B': '-...', 'C': '-.-.','D': '-..', 'E': '.', 'F': '..-.','G': '--.', 'H': '....', 'I': '..','J': '.---', 'K': '-.-', 'L': '.-..','M': '--', 'N': '-.', 'O': '---','P': '.--.', 'Q': '--.-', 'R': '.-.','S': '...', 'T': '-', 'U': '..-','V': '...-', 'W': '.--', 'X': '-..-','Y': '-.--', 'Z': '--..','0': '-----', '1': '.----', '2': '..---','3': '...--', '4': '....-', '5': '.....','6': '-....', '7': '--...', '8': '---..','9': '----.',' ':'/'}
DICT_UpperAndNumbers_Morse={v:k for k, v in DICT_Morse_UpperAndNumbers.items()}

str=input('String to convert: ')

def ConvertToMorse(str):
    outfile=open('C:\\Users\Bence\Desktop\python\python.txt','w')
    str2=''
    for ch in str:
        if ch not in string.punctuation:
            str2+=ch
    for ch2 in str2:
        print(DICT_Morse_UpperAndNumbers[ch2.upper()], '/', end='')
        print(DICT_Morse_UpperAndNumbers[ch2.upper()],'/',end='',file=outfile)
    outfile.close()

ConvertToMorse(str)
