import time
import winsound

morse_code_fjalori = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
                      'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                      'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
                      'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                      'Y': '-.--', 'Z': '--..', ' ': ' '}

morse_to_char_fjalori = {char_morse: char_alfabet for char_alfabet, char_morse in morse_code_fjalori.items()}

#encode metoda
def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in morse_code_fjalori:
            morse_code += morse_code_fjalori[char] + ' '
    return morse_code
  
#decode metoda
def morse_to_text(morse_code):
    words = morse_code.split('  ')
    text = ''
    for word in words:
        letters = word.split(' ')
        for letter in letters:
            if letter in morse_to_char_fjalori:
                text += morse_to_char_fjalori[letter]
        text += ' '
    return text

#metoda per beeps, e implementume me librarin winsound
def console_beep(text):
    for char in text.upper():
        if char == ' ':
            time.sleep(2)
        else:
            morse_char = morse_code_fjalori.get(char, '')
            for symbol in morse_char:
                if symbol == '.':
                    winsound.Beep(600, 300)
                if symbol == '-':
                    winsound.Beep(600, 600)
                time.sleep(0.1)

#input text ose morse, varesisht tani per encode dhe decode
inputi = input("Jep inputin ne tekst ose ne morse:")

if '.' in inputi or '-' in inputi:
    decoded_text = morse_to_text(inputi)
    print("Morse code: ", inputi)
    print("Teksti: ", decoded_text)
else:
    decoded_text = text_to_morse(inputi)
    print("Teksti: ", inputi)
    print("Morse code: ", decoded_text)

console_beep(inputi)