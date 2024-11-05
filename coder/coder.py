import xml.etree.ElementTree as ET
from lxml import etree
from lxml.html import Element

XML_PATH = "xml/mors.xml"
XSD_PATH = "xsd/mors.xsd"

# Morse code dictionary
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


# Function to encode a sentence in Morse code
def encode_to_morse(sentence):
    sentence = sentence.upper()
    encoded_characters = []
    for char in sentence:
        code = character_to_morse.get(char, '')
        if code:
            encoded_characters.append(code)
    return " ".join(encoded_characters)


# Function to validate XML based on XSD schema
def validate(xml_path: str, xsd_path: str) -> bool:
    try:
        xsd_doc = etree.parse(xsd_path)
        xml_schema = etree.XMLSchema(xsd_doc)
        xml_doc = etree.parse(xml_path)
        result = xml_schema.validate(xml_doc)
        if result:
            print("The XML file is valid according to the XSD schema.")
        else:
            print("The XML file is not valid according to the XSD schema.")
        return result
    except etree.XMLSchemaParseError as e:
        print("XSD schema parsing error:", e)
    except etree.DocumentInvalid as e:
        print("XML document validation error:", e)
    except Exception as e:
        print("Unexpected error:", e)
    return False


# Function to create XML structure and validate it
def create_and_validate_xml(sentence, xml_path=XML_PATH, xsd_path=XSD_PATH):
    # Encode sentence in Morse code
    encoded_sentence = encode_to_morse(sentence)

    # Create root element "message"
    root = ET.Element("message")

    # Split sentence into "sentence" elements by period, question mark, and exclamation mark codes
    sentences = encoded_sentence.replace(" .-.-.- ", " <STOP> ").replace(" ..--.. ", " <STOP> ").replace(" -.-.-- ",
                                                                                                         " <STOP> ").split(
        " <STOP> ")

    # Process each sentence
    for sentence in sentences:
        sentence_elem = ET.SubElement(root, "sentence")

        # Split sentence into words by "/"
        words = sentence.split(" / ")

        # Process each word
        for word in words:
            word_elem = ET.SubElement(sentence_elem, "word")
            characters = word.split()  # Split word into characters by spaces
            for character in characters:
                character_elem = ET.SubElement(word_elem, "character")
                character_elem.text = character

    # Save XML structure to file
    tree = ET.ElementTree(root)
    tree.write(xml_path, encoding="utf-8", xml_declaration=True)
    print(f"XML file saved as {xml_path}")

    # Validate saved XML file
    is_valid = validate(xml_path, xsd_path)
    return xml_path