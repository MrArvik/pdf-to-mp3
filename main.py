# try to use tkinter, (pdfplumber, PyPDF2 - > mb without it)
# should use gtts, tika (from tika import parser)
# signed in a new computer
# should try pyqt
#test




# importing tkinter and tkinter.ttk
# and all their functions and classes
from tkinter import *
from tkinter.ttk import *

# importing askopenfile function
# from class filedialog
from tkinter.filedialog import askopenfile


import PyPDF2
import gtts
from tika import parser
import os


window = Tk()

window.title("PDF to mp3 converter")
window.geometry('600x400')
window.resizable(True, True)
window.configure(background="#B53E3E")
window.attributes('-alpha',0.9)


def open_file():
    file = askopenfile(mode='rb', filetypes=[('PDF Files', '*.pdf')])
    if file is not None:
        content = file.name
        print(content)
        pdf_file = parser.from_file(str(content))
        tts = gtts.gTTS(pdf_file['content'], lang='ru')
        tts.save('audiotest1.mp3')

btn = Button(window, text="Open", command=lambda: open_file())
btn.pack(pady=20)

window.mainloop()
