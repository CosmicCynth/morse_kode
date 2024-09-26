import MorseCodePy
import requests


# Dictionary til oversættelse fra bogstaver til morsekode
morseCode = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X":"-..-",
    "Y": "-.--",
    "Z": "--.."
}

# Dictionary til oversættelse fra morsekode til bogstaver. Tomt oversættes til mellemrum.
morseCodeReverse = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z"
}





# Denne funktion oversætter et enkelt bogstav (letter) med opslag i dictionay (code) hvis muligt
def translate(letter, code):
    if letter in code:
        return code[letter]
    else:
        return "?"

print("Translate funktion")
print(translate('A',morseCode))


# Denne funktion oversætter en vilkårlig tekststreng til morsekode
# '/' markerer nyt bogstav
# '//' markerer nyt ord

def encodeMessage(message, code):
    output=""
    for char in message:
        output+=translate(char,code) + "/"
    return output

print("encodeMessage funktion")
print(encodeMessage("KENNEN",morseCode))


# Denne funktion oversætter en korrekt formatteret morsebesked til bogstaver
# '/' markerer nyt bogstav
# '//' markerer nyt ord
def decodeMessage(message, code):
    Reverse_output = []
    words = message.split('//')
    for word in words:
        # Her samler vi bogstaverne for hvert ord ved at slå morsekode op i 'code'-ordbogen
        decoded_word = ''.join(code[morse] for morse in word.split('/') if morse in code)
        Reverse_output.append(decoded_word)
    return ' '.join(Reverse_output)




print("decodeMessage funktion")
print(decodeMessage(".-//..",morseCodeReverse))
