import tkinter as tk
from tkinter import filedialog
import fitz  # PyMuPDF

def extract_text_image(pdf_path):
    text = ""
    images = []

    # Abrir o arquivo PDF
    document = fitz.open(pdf_path)

    # Extrair texto e imagens de cada página
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        
        # Extrair texto
        text += page.get_text()
        
        # Extrair imagens
        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = document.extract_image(xref)
            image_bytes = base_image["image"]
            images.append(image_bytes)

    return text, images

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        extracted_text, extracted_images = extract_text_image(file_path)
        print("Texto extraído:")
        print(extracted_text)
        print("Imagens extraídas:", len(extracted_images))
        
    # Validar se um conteudo existe dentro do PDF
    if "PDF" in extracted_text:
        print("blaosdia")

# Criar a janela principal
root = tk.Tk()
root.title("Extrair Texto e Imagens de PDF")

# Criar botão para buscar arquivo
browse_button = tk.Button(root, text="Buscar Arquivo PDF", command=browse_file)
browse_button.pack(pady=10)

# Executar o loop principal da interface gráfica
root.mainloop()
