import string

DICT_Morse_UpperAndNumbers={'A': '.-', 'B': '-...', 'C': '-.-.','D': '-..', 'E': '.', 'F': '..-.','G': '--.', 'H': '....', 'I': '..','J': '.---', 'K': '-.-', 'L': '.-..','M': '--', 'N': '-.', 'O': '---','P': '.--.', 'Q': '--.-', 'R': '.-.','S': '...', 'T': '-', 'U': '..-','V': '...-', 'W': '.--', 'X': '-..-','Y': '-.--', 'Z': '--..','0': '-----', '1': '.----', '2': '..---','3': '...--', '4': '....-', '5': '.....','6': '-....', '7': '--...', '8': '---..','9': '----.',' ':'_','':''}
DICT_UpperAndNumbers_Morse={v:k for k, v in DICT_Morse_UpperAndNumbers.items()}
def ConvertToMorse():
    str = input('String to convert: ')
    outfile=open('python.txt','w')
    str2=''
    for ch in str:
        if ch not in string.punctuation:
            str2+=ch
    for ch2 in str2:
        #print(DICT_Morse_UpperAndNumbers[ch2.upper()],end='')
        print(DICT_Morse_UpperAndNumbers[ch2.upper()],'|',end='',file=outfile)
    outfile.close()

ConvertToMorse()

def ConvertFromMorse():
    str=''
    infile=open('python.txt','r')
    for ch in infile:
        str+=ch
        str=str.replace(' ','')
        print(str)
        L=str.split('|')
        #print(L)
        for ch2 in L:
            print(DICT_UpperAndNumbers_Morse[ch2],end='')
    infile.close()

ConvertFromMorse()