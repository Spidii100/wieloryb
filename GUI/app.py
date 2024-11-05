import tkinter as tk
from tkinter import messagebox, filedialog
import xml.etree.ElementTree as ET
import base64


class XMLApp:
    def __init__(self, root):
        self.root = root
        self.root.title("XML Reader/Encoder/Decoder")

        # Text widget to display XML content
        self.text_area = tk.Text(root, wrap='word', height=20, width=80)
        self.text_area.pack(pady=10)

        # Buttons
        self.load_button = tk.Button(root, text="Load XML", command=self.load_xml)
        self.load_button.pack(pady=5)

        self.encode_button = tk.Button(root, text="Encode", command=self.encode_xml)
        self.encode_button.pack(pady=5)

        self.decode_button = tk.Button(root, text="Decode", command=self.decode_xml)
        self.decode_button.pack(pady=5)

    def load_xml(self):
        # Load XML file and display its content
        file_path = filedialog.askopenfilename(title="Select XML File", filetypes=[("XML files", "*.xml")])
        if file_path:
            try:
                tree = ET.parse(file_path)
                root = tree.getroot()
                xml_str = ET.tostring(root, encoding='unicode')
                self.text_area.delete(1.0, tk.END)  # Clear previous text
                self.text_area.insert(tk.END, xml_str)  # Insert XML content
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load XML file:\n{e}")

    def encode_xml(self):
        # Encode the current XML content in Base64
        xml_content = self.text_area.get(1.0, tk.END).strip()
        if not xml_content:
            messagebox.showwarning("Warning", "No XML content to encode.")
            return
        encoded = base64.b64encode(xml_content.encode()).decode()
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, encoded)

    def decode_xml(self):
        # Decode the Base64 encoded content back to XML
        encoded_content = self.text_area.get(1.0, tk.END).strip()
        if not encoded_content:
            messagebox.showwarning("Warning", "No encoded content to decode.")
            return
        try:
            decoded = base64.b64decode(encoded_content.encode()).decode()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, decoded)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to decode content:\n{e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = XMLApp(root)
    root.mainloop()
