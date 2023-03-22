# try to use tkinter, (pdfplumber, PyPDF2 - > mb without it)
# should use gtts, tika (from tika import parser)
# signed in a new computer
# should try pyqt

from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile
import gtts
from tika import parser
import codecs


window = Tk()

window.title("PDF to mp3 converter")

window.geometry('600x400')
window.resizable(True, True)
window.configure(background="#B53E3E")
window.attributes('-alpha',0.9)


pdf_file = parser.from_file('225010558.pdf')
tts = gtts.gTTS(pdf_file['content'], lang='ru')
tts.save('audiotest1.mp3')





window.mainloop()