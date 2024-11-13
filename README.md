# **MorseMasterXML**
`MMX MorseMasterXML`
# Table of Contents
1. [About](#About)
2. [Technologies](#technologies)
3. [Project structure](#project-structure)
4. [Getting Started](#getting-started)
5. [Usage](#usage)
6. [Administration](#administration)
7. [Contacts](#contacts)
# About
MorseMasterXML (MMX) is a Python-based encoder and decoder tool for Morse code that integrates XML validation to ensure structured data processing. The project allows users to input or load an XML file, validate its format, and convert the text within to or from Morse code
# Technologies
- **Python 3.11**: Main programming language.
- **Tkinter**: For GUI-based user interaction, including file dialogs, message boxes, and user input areas.
- **xml.etree.ElementTree**: For parsing and constructing XML elements.
- **lxml**: Provides advanced XML validation capabilities using etree for more reliable structure checking.
- **Custom Morse Encoder/Decoder**: based on a python dictionaries, efficient lookup and translation to/from Morse code.
# Project structure
```
/
├── coder # Encoder to morse code.
│   └── coder.py
├── decoder # Decoder from morse code.
│   └── decoder.py
├── gui # Main entry point
│   └── app.py
├── resources # Examples of xml and xsd file structure
│   ├── example.xml
│   └── example.xsd
├── requirements.txt
├── LICENSE
└── README.md
```
# Getting started
## Prerequisites
- **Python 3.11**: Install from [Python's official website](https://www.python.org/)
- **Required Libraries**: Install with `pip install -r requirements.txt`
## Development environment setup
1. **Clone the Repository**:
```bash
    git clone https://github.com/Spidii100/wieloryb.git
    cd wieloryb
```
2. **Install Dependecies**:
```bash
    pip install -r requirements.txt
```
3. **Verify Setup**:
```bash
    python gui/app.py
```
*If there is a problem with dependecies from coder/decoder then use this instead:
```bash
    python -m gui.app
```
## Installation
1. **Download Repository**: Clone or download from the repository.
2. **Install with Docker (optional)**:
    - Build the image:
      ```bash
      docker build -t wieloryb .
      ```
    - Run the container:
      ```bash
      docker run -p 5000:5000 wieloryb
      ```
# Usage
`MorseMaster is a tool that converts text to Morse code and vice versa. In encoding mode, it translates letters, numbers, and punctuation from text into Morse code symbols (dots and dashes). In decoding mode, it interprets Morse code input, converting it back to readable text in the form of xml file.`

**Basic Steps**:
1. **Load XML File**: Click Load XML to open an XML file with structured data.
2. **Validate XML**: On loading, the file's structure is validated.
3. **Encode/Decode**: Use the Encode button to convert text to Morse or Decode to reverse Morse to readable text.
# Administration
- **Running the App**: Run python main.py to start the GUI application.
- **Stopping**: Close the GUI window.
- **Backups**: Important XML files and settings should be backed up in the resources directory.
# Contacts
- **kwjay** - kwjay1002@gmail.com
- **Spidii100**
- **matis05**
- **nikpan1**
- **karmeloova**