import time

morse_code_fjalori = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
                      'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                      'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
                      'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                      'Y': '-.--', 'Z': '--..', ' ': ' '}
#sync

#me shtu nje metode qe merr textin si parameter e kthen si morse
morse_to_char_fjalori = {char_morse: char_alfabet for char_alfabet, char_morse in morse_code_fjalori.items()}

def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in morse_code_fjalori:
            morse_code += morse_code_fjalori[char] + ' ' #me provu qetu me hek space per console.beep() se spi bon beep komplet
    return morse_code
  
#me shtu nje metode qe merr morse_code si parameter e kthen si text
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

#console beep metoda per me kthy si output me sound, textin e encodum
#tu e importu nje librari per sound
