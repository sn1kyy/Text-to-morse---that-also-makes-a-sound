import time 
#adds delays b/w the morse codes
import platform
#access to OSs

# Morse code dictionary
morse_code_dict = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    "'": '.----.',
    '!': '-.-.--',
    '/': '-..-.',
    '(': '-.--.',
    ')': '-.--.-',
    '&': '.-...',
    ':': '---...',
    ';': '-.-.-.',
    '=': '-...-',
    '+': '.-.-.',
    '-': '-....-',
    '_': '..--.-',
    '"': '.-..-.',
    '$': '...-..-',
    '@': '.--.-.',
    ' ': '/'
}


def sound(duration):
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(1000, duration)
        #access to the basic sound library on windows
    else:
        import os
        os.system('printf"\a"')
        #executes "\a"(produces a beep) in shell/terminal


def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
        else:
            print("Given text/symbol can't be converted into morse code.")
    return morse_code


def morse_to_sound(morse_code):
    for symbol in morse_code:
        match symbol:
            case '.': 
                sound(100)
            case '-':
                sound(300)
            case ' ':
                time.sleep(0.3)
            case '/':
                time.sleep(0.7)
                #delays(short and long)
            

if __name__ == '__main__':
    text = input("Enter your text : ")

     # Convert text to Morse code
    morse = text_to_morse(text)
    print("Morse code : " + morse)

     # Convert Morse code to sound
    morse_to_sound(morse)
