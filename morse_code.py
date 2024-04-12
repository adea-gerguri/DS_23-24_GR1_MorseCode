import time

morse_code_fjalori = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
                      'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
                      'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
                      'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                      'Y': '-.--', 'Z': '--..', ' ': ' '}

#me shtu nje metode qe merr textin si parameter e kthen si morse

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
