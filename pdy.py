import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2
import os

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

app = tk.Tk()
app.title("PDF Merger")

pdf_list = tk.Variable()

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

select_button = tk.Button(frame, text="Select PDFs", command=select_files)
select_button.pack(side=tk.LEFT)

merge_button = tk.Button(frame, text="Merge PDFs", command=merge_files)
merge_button.pack(side=tk.LEFT, padx=5)

app.mainloop()
