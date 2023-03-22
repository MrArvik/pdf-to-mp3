# try to use tkinter, (pdfplumber, PyPDF2 - > mb without it)
# should use gtts, tika (from tika import parser)
#signed in a new computer
from tkinter import *
from tkinter import ttk



window = Tk()

window.geometry('600x400')
window.resizable(True, True)
window.configure(background="#B53E3E")
window.attributes('-alpha',0.9)

window.title("PDF to mp3 converter")



window.mainloop()