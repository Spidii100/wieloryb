import tkinter as tk
from tkinter import messagebox, filedialog
import base64
import xml.etree.ElementTree as ET
from xml.dom import minidom
import coder.coder
import decoder.decoder
from coder.coder import encode_to_morse


class XMLApp:
    def __init__(self, root):
        self.xml_content = ""
        self.message_to_encode = ""
        self.encoded_message = ""
        self.root = root
        self.root.title("XML Encoder/Decoder")

        # Frame for input text area
        self.input_frame = tk.Frame(root)
        self.input_frame.pack(pady=10)

        # Label for input text area
        self.input_label = tk.Label(self.input_frame, text="Input Text:")
        self.input_label.pack(side=tk.TOP, padx=5)

        # Text widget for inputting text to save as XML
        self.input_text_area = tk.Text(self.input_frame, wrap='word', height=15, width=40)
        self.input_text_area.pack(side=tk.LEFT, padx=5)

        # Frame for output text area
        self.output_frame = tk.Frame(root)
        self.output_frame.pack(pady=10)

        # Label for output text area
        self.output_label = tk.Label(self.output_frame, text="Output/Encoded Text:")
        self.output_label.pack(side=tk.TOP, padx=5)

        # Text widget for displaying encoded/decoded content
        self.output_text_area = tk.Text(self.output_frame, wrap='word', height=15, width=40)
        self.output_text_area.pack(side=tk.LEFT, padx=5)

        # Frame for buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        # Buttons for loading XML, saving, encoding, and decoding
        self.load_button = tk.Button(self.button_frame, text="Load XML", command=self.load_xml)
        self.load_button.pack(side=tk.LEFT, padx=5)

        self.save_button = tk.Button(self.button_frame, text="Save as XML", command=self.save_as_xml)
        self.save_button.pack(side=tk.LEFT, padx=5)

        self.encode_button = tk.Button(self.button_frame, text="Encode", command=self.encode_text)
        self.encode_button.pack(side=tk.LEFT, padx=5)

        self.decode_button = tk.Button(self.button_frame, text="Decode", command=self.decode_text)
        self.decode_button.pack(side=tk.LEFT, padx=5)

    def load_xml(self):
        # Load XML file and display its content in the input text area
        file_path = filedialog.askopenfilename(title="Select XML File", filetypes=[("XML files", "*.xml")])
        if file_path:
            try:
                tree = ET.parse(file_path)
                root = tree.getroot()
                self.xml_content = ET.tostring(root, encoding='unicode')
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load XML file:\n{e}")

    def save_as_xml(self):
        # Get the input text and save it as an XML file
        input_text = self.input_text_area.get(1.0, tk.END).strip()
        if not input_text:
            messagebox.showwarning("Warning", "Input area is empty.")
            return
        # Save to XML file
        file_path = filedialog.asksaveasfilename(defaultextension=".xml",
                                                   filetypes=[("XML files", "*.xml")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.xml_content)
            messagebox.showinfo("Success", "XML file saved successfully.")

    def encode_text(self):
        # Encode the current input text in Base64
        self.message_to_encode = self.input_text_area.get(1.0, tk.END).strip()
        if not self.message_to_encode:
            messagebox.showwarning("Warning", "No input text to encode.")
            return

        self.encoded_message = encode_to_morse(self.message_to_encode)
        self.output_text_area.delete(1.0, tk.END)  # Clear previous output
        self.output_text_area.insert(tk.END, self.encoded_message)  # Show encoded content

    def decode_text(self):
        # Decode the Base64 encoded content back to text
        encoded_content = self.output_text_area.get(1.0, tk.END).strip()
        if not encoded_content:
            messagebox.showwarning("Warning", "No encoded content to decode.")
            return

        try:
            decoded = base64.b64decode(encoded_content.encode()).decode()
            self.output_text_area.delete(1.0, tk.END)
            self.output_text_area.insert(tk.END, decoded)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to decode content:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = XMLApp(root)
    root.mainloop()
