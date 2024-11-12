import xml.etree.ElementTree as ET
from xml.dom import minidom

character_to_morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}

def encode_to_morse(to_encode):
    try:
        ET.fromstring(to_encode)
        root = ET.fromstring(to_encode)
        for sentence in root.findall('sentence'):
            for word in sentence.findall('word'):
                for character in word.findall('character'):
                    character.text = character_to_morse[character.text.upper()]
        return ET.tostring(root)
    except:
        return create_xml_message(to_encode)

def create_xml_message(sentences):
    message = ET.Element("message")

    for sentence_data in sentences:
        sentence = ET.SubElement(message, "sentence")

        for word_data in sentence_data:
            word = ET.SubElement(sentence, "word")

            for char in word_data:
                character = ET.SubElement(word, "character")
                character.text = character_to_morse[char.upper()]

    return minidom.parseString(ET.tostring(message, encoding="utf-8")).toprettyxml(indent="    ")