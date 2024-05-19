import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2

def merge_pdfs(pdf_list, output_path):
    pdf_writer = PyPDF2.PdfWriter()

    for pdf in pdf_list:
        pdf_reader = PyPDF2.PdfReader(pdf)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

    with open(output_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

def select_files():
    filetypes = [("PDF files", "*.pdf")]
    filenames = filedialog.askopenfilenames(title="Select PDF files", filetypes=filetypes)
    if filenames:
        pdf_list.set(filenames)
        update_num_selected(len(filenames))  # Atualiza o número de PDFs selecionados

def save_file():
    filename = filedialog.asksaveasfilename(title="Save Merged PDF", defaultextension=".pdf",
                                            filetypes=[("PDF files", "*.pdf")])
    return filename

def merge_files():
    pdf_files = pdf_list.get()
    if not pdf_files:
        messagebox.showerror("Error", "No PDF files selected")
        return

    output_file = save_file()
    if output_file:
        merge_pdfs(pdf_files, output_file)
        messagebox.showinfo("Success", f"PDFs merged successfully into {output_file}")

def update_num_selected(num_selected):
    num_selected_label.config(text=f"Selected PDFs: {num_selected}")

app = tk.Tk()
app.title("PDF Merger")
app.iconbitmap(r'C:\Users\vinic\Documents\Python Scripts\pdf merge\icon\ipdf.ico')  # Substitua 'your_icon.ico' pelo caminho do seu arquivo de ícone

# Defina o tamanho da janela
app.geometry("300x110")

pdf_list = tk.Variable()

frame = tk.Frame(app)
frame.pack(padx=10, pady=12)

select_button = tk.Button(frame, text="Select PDFs", command=select_files)
select_button.grid(row=0, column=0, padx=1)

merge_button = tk.Button(frame, text="Merge PDFs", command=merge_files)
merge_button.grid(row=0, column=1, padx=5)

# Cria um novo frame para conter o label e coloca-o abaixo dos botões
bottom_frame = tk.Frame(app)
bottom_frame.pack(pady=5)

# Label para exibir o número de PDFs selecionados
num_selected_label = tk.Label(bottom_frame, text="Selected PDFs: 0")
num_selected_label.pack()

app.mainloop()
