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
morseCodeReverse = {v: k for k, v in morseCode.items()} # Denne linje af kode tager morsekodedictionary og vender det om til vores nye morsecodereverse dict





# Denne funktion oversætter et enkelt bogstav (letter) med opslag i dictionay (code) hvis muligt
def translate(letter, code):
    if letter in code: # Her checker vi hvis bogstavet skrevet er in code som er morsekode dict
        return code[letter] # Her returner den Morsekode tegnet fra dict
    else:
        return "?" # Hvis bogstavet/tegnet ikke er inde i morsekode dict returner den valuen ?

print("Translate funktion") # Her danner vi overblik med at inddele hver funktion med en overskrift
print(translate('A',morseCode)) # Her får vi python til at printe vores funktion med letter A som returner morsekode versionen


# Denne funktion oversætter en vilkårlig tekststreng til morsekode
# '/' markerer nyt bogstav
# '//' markerer nyt ord
def encodeMessage(message, code):
    output="" # Da vi skal lave en helt besked kan vi ikke bruge return alene så vi bliver nød til at lave en tom variable som bliver en temporary besked holder som så kan returners senere
    for char in message: # Her checker vi hvert bogstav/tegn i beskenden(KENNEN)
        output+=translate(char,code) + "/" # Her adder vi med kommandoen += til at putte bogstavet igenmem morsekode dict og mellem hvert bogstav kommer der bindestreg
    return output # Når for in statementen er færdig så returner vi output variablen så hele beskeden kommer med

print("encodeMessage funktion") # Her danner vi overblik med at inddele hver funktion med en overskrift
print(encodeMessage("KENNEN",morseCode)) # Her får vi python til at printe vores funktion med beskeden KENNEN som returner morsekode versionen


# Denne funktion oversætter en korrekt formatteret morsebesked til bogstaver
# '/' markerer nyt bogstav
# '//' markerer nyt ord
def decodeMessage(message, code):
    Reverse_output = [] # Her laver vi en tom variabel
    words = message.split('//') # Her tager vi beskend(message) og splitter den
    for word in words: # Her laver vi en for in funktion
        # Her samler vi bogstaverne for hvert ord ved at slå morsekode op i code dictonary
        decoded_word = ''.join(code[morse] for morse in word.split('/') if morse in code) # Her laver variablen til vores reverse output hvor hvert bogstav går i gennem
        Reverse_output.append(decoded_word) # Her reference vi tilbage til vorees Reverse_output hvor den adder decoded_word et bogstav af gangen
    return ' '.join(Reverse_output) # Her returner vi valuen så vores print funktion kan printe den


print("decodeMessage funktion") # Her danner vi overblik med at inddele hver funktion med en overskrift
print(decodeMessage(".-//../.-/.-",morseCodeReverse)) # Her får vi python til at printe vores funktion med beskeden .-//../.-/.- som returner i normale bogstaver

