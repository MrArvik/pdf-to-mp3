# try to use tkinter, (pdfplumber, PyPDF2 - > mb without it)
# should use gtts, tika (from tika import parser)
# signed in a new computer
# should try pyqt
#test

from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
from tkinter import filedialog as fd
import gtts
from tika import parser
import codecs


window = Tk()

window.title("PDF to mp3 converter")
window.geometry('600x400')
window.resizable(True, True)
window.configure(background="#B53E3E")
window.attributes('-alpha',0.9)

def select_file():
    filetypes = (
        ('pdf files', '*.pdf'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    fileinfo = fd.showinfo(
        title='Selected File',
        message=filename
    )

open_button = ttk.Button(
    window,
    text='Open a File',
    command=select_file
)

open_button.pack(expand=True)



#pdf_file = parser.from_file('225010558.pdf')
#tts = gtts.gTTS(pdf_file['content'], lang='ru')
#tts.save('audiotest1.mp3')





window.mainloop()