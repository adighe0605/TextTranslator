import os
def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        os.system("pip install " + package)


import_or_install('googletrans')
import_or_install('tkinter')
import_or_install('pyperclip')
import_or_install('deep_translator')
import_or_install('gettext')
import_or_install('docx2txt')

from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from googletrans import Translator
from googletrans import LANGUAGES
import pyperclip
import gettext
from deep_translator import GoogleTranslator
import docx2txt
from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry('1080x400')
root.resizable(0, 0)
root.title("Text Translator                                                                                                                                                                                                   -- Built by Akshay Dighe")
root.config(bg='#DEDEDE')

# INPUT AND OUTPUT TEXT WIDGET
Label(root, text="Enter Text", font='arial 10 bold', bg='#DEDEDE').place(x=30, y=65)
Input_text = Text(root, font='arial 10', height=11, wrap=WORD, padx=5, pady=5, width=60)
Input_text.place(x=30, y=100)

Label(root, text="Output", font='arial 10 bold', bg='#DEDEDE').place(x=600, y=65)
Output_text = Text(root, font='arial 10', height=11, wrap=WORD, padx=5, pady=5, width=60)
Output_text.place(x=600, y=100)

##################
language = list(LANGUAGES.values())

src_lang = ttk.Combobox(root, values=language, width=22, font='arial 10')
src_lang.place(x=30, y=30)
src_lang.set('Select Input Language')

dest_lang = ttk.Combobox(root, values=language, width=22, font='arial 10')
dest_lang.place(x=600, y=30)
dest_lang.set('Select Output Language')


########################################  Define functions #######
def Translate():
    try:
        #translator = Translator()
        to_translate = Input_text.get(1.0,END)

        translated = GoogleTranslator(source=src_lang.get(), target=dest_lang.get()).translate(to_translate)
        Output_text.delete(1.0, END)
        Output_text.insert(END, translated)
        pyperclip.copy(translated)

    except Exception as e:
        tkinter.messagebox.showwarning("Can't proceed with translation",e)

def detectLang():
    to_translate = Input_text.get(1.0, END)
    print(to_translate)
    print(Translator.detect(to_translate))

def refresh():
    translator = Translator()
    translated = ''
    Input_text.delete(1.0, END)
    Output_text.delete(1.0, END)
    Input_text.insert(END, translated)
    Output_text.insert(END, translated)

def copytoclipboard():
    pyperclip.copy(Output_text)
    spam = pyperclip.paste()
    #label4 = tk.Label(root, text='Copied to Clipboard!', bg='#7D7D7D', fg='white')
    #label4.config(font=('arial', 9, 'bold'))
    #canvas1.create_window(430, 320, window=label4)

##########  DetectLang Button ########
detectlang_btn = Button(root, text='Detect Lang', font='arial 10 bold', pady=5, command=detectLang, bg='#D04A02',
                       fg='white',
                       activebackground='#D04A02')
#detectlang_btn.place(x=490, y=140)

##########  Translate Button ########
trans_btn = Button(root, text='Translate', font='arial 10 bold', pady=5, command=Translate, bg='#D04A02',
                       fg='white',
                       activebackground='#D04A02')
trans_btn.place(x=495, y=170)

##########  Clear Translate Button ########

trans_btn = Button(root, text='Clear Translation', font='arial 10 bold', pady=5, command=refresh, bg='#D04A02', fg='white',
                   activebackground='#D04A02')
trans_btn.place(x=140, y=320)

##########  Copy to clipboard Button ########
trans_btn = Button(root, text='Copy to Clipboard', font='arial 10 bold', pady=5, command=copytoclipboard, bg='#D04A02',fg='white',
                   activebackground='#D04A02')
trans_btn.place(x=720, y=320)

root.mainloop()

