import tkinter as tk
from tkinter import messagebox, filedialog
import xml.etree.ElementTree as ET
from lxml import etree
from coder.coder import encode_to_morse
from decoder.decoder import decode_from_morse


def validate(xml_path, xsd_path) -> bool:
    xmlschema_doc = etree.parse(xsd_path)
    xmlschema = etree.XMLSchema(xmlschema_doc)
    xml_doc = etree.parse(xml_path)
    result = xmlschema.validate(xml_doc)
    return result


class XMLApp:
    def __init__(self, root):
        self.xml_content = ""
        self.message_to_encode = ""
        self.encoded_message = ""
        self.root = root
        self.root.title("XML Encoder/Decoder")

        self.input_frame = tk.Frame(root)
        self.input_frame.pack(pady=10)

        self.input_label = tk.Label(self.input_frame, text="Input Text:")
        self.input_label.pack(side=tk.TOP, padx=5)

        self.input_text_area = tk.Text(self.input_frame, wrap='word', height=15, width=40)
        self.input_text_area.pack(side=tk.LEFT, padx=5)

        self.output_frame = tk.Frame(root)
        self.output_frame.pack(pady=10)

        self.output_label = tk.Label(self.output_frame, text="Output/Encoded Text:")
        self.output_label.pack(side=tk.TOP, padx=5)

        self.output_text_area = tk.Text(self.output_frame, wrap='word', height=15, width=40)
        self.output_text_area.pack(side=tk.LEFT, padx=5)
        self.output_text_area.config(state="disabled")

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.load_button = tk.Button(self.button_frame, text="Load XML", command=self.load_xml)
        self.load_button.pack(side=tk.LEFT, padx=5)

        self.save_button = tk.Button(self.button_frame, text="Save", command=self.save_as_xml)
        self.save_button.pack(side=tk.LEFT, padx=5)

        self.encode_button = tk.Button(self.button_frame, text="Encode", command=self.encode_text)
        self.encode_button.pack(side=tk.LEFT, padx=5)

        self.decode_button = tk.Button(self.button_frame, text="Decode", command=self.decode_text)
        self.decode_button.pack(side=tk.LEFT, padx=5)

    def load_xml(self):
        xml_path = filedialog.askopenfilename(title="Select XML File", filetypes=[("XML files", "*.xml")])
        xsd_path = filedialog.askopenfilename(title="Select XSD File", filetypes=[("XSD files", "*.xsd")])
        if xml_path and validate(xml_path, xsd_path):
            try:
                tree = ET.parse(xml_path)
                root = tree.getroot()
                self.xml_content = ET.tostring(root, encoding='unicode')
                self.input_text_area.delete(1.0, tk.END)
                self.input_text_area.insert(tk.END, self.xml_content)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load XML file:\n{e}")


    def save_as_xml(self):
        output_text = self.output_text_area.get(1.0, tk.END).strip()
        if not output_text:
            messagebox.showwarning("Warning", "Input area is empty.")
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".xml",
                                                   filetypes=[("XML files", "*.xml")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(output_text)
            messagebox.showinfo("Success", "XML file saved successfully.")

    def encode_text(self):
        self.message_to_encode = self.input_text_area.get(1.0, tk.END).strip()

        if not self.message_to_encode:
            messagebox.showwarning("Warning", "No input text to encode.")
            return

        self.encoded_message = encode_to_morse(self.message_to_encode)
        self.output_text_area.config(state="normal")
        self.output_text_area.delete(1.0, tk.END)  # Clear previous output
        self.output_text_area.insert(tk.END, self.encoded_message)  # Show encoded content
        self.output_text_area.config(state="disabled")

    def decode_text(self):
        encoded_content = self.input_text_area.get(1.0, tk.END).strip()
        if not encoded_content:
            messagebox.showwarning("Warning", "No encoded content to decode.")
            return

        try:
            decoded = decode_from_morse(encoded_content)
            self.output_text_area.config(state="normal")
            self.output_text_area.delete(1.0, tk.END)
            self.output_text_area.insert(tk.END, decoded)
            self.output_text_area.config(state="disabled")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to decode content:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = XMLApp(root)
    root.mainloop()
