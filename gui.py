import tkinter as tk
from tkinter import ttk
from pickleTRYING import *
from keyGenGUI import *
from encGUI import *
from uTabGUI import *
from vTabGUI import *
from decGUI import *




class MiniKyber:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('1280x720')
        self.window.title("Mini Kyber")
        self.window.minsize(1200,720)
        self.window.maxsize(1200,720)
        self.notebook = ttk.Notebook(self.window,width=1200, height=720)

        self.tab1 = KeyGenerationTab(self.notebook)
        self.tab2a = FrameUTab(self.notebook)
        self.tab2b = FrameVTab(self.notebook)
        self.tab2 = EncryptionTab(self.notebook)
        self.tab3 = DecryptionTab(self.notebook)
        
        self.notebook.add(self.tab1.frame, text='KeyGen')
        self.notebook.add(self.tab2.frame, text='Encryption')
        self.notebook.add(self.tab2a.frame, text='What is u?')
        self.notebook.add(self.tab2b.frame, text='What is v?')
        self.notebook.add(self.tab3.frame, text='Decryption')
        
        self.nextButtonKeyGen = ttk.Button(self.tab1.frame,text = ">",command = self.button_next_keyGen)
        self.nextButtonKeyGen.place(x = 1050, y = 650)
        self.nextButtonEnc = ttk.Button(self.tab2.frame,text = ">",command = self.button_next_enc)
        self.nextButtonEnc.place(x = 1050, y = 650)
        self.prevButtonEnc = ttk.Button(self.tab2.frame,text = "<",command = self.button_prev_enc)
        self.prevButtonEnc.place(x = 950, y = 650)
        self.nextButtonEncU = ttk.Button(self.tab2a.frame,text = ">",command = self.button_next_encU)
        self.nextButtonEncU.place(x = 1050, y = 650)
        self.prevButtonEnc = ttk.Button(self.tab2a.frame,text = "<",command = self.button_prev_encU)
        self.prevButtonEnc.place(x = 950, y = 650)
        self.nextButtonEncV = ttk.Button(self.tab2b.frame,text = ">",command = self.button_next_encV)
        self.nextButtonEncV.place(x = 1050, y = 650)
        self.prevButtonEnc = ttk.Button(self.tab2b.frame,text = "<",command = self.button_prev_encV)
        self.prevButtonEnc.place(x = 950, y = 650)
        self.prevButtonEnc = ttk.Button(self.tab3.frame,text = "<",command = self.button_prev_dec)
        self.prevButtonEnc.place(x = 950, y = 650)

        self.notebook.pack(expand=1, fill='both')

        self.window.mainloop()

    def button_next_keyGen(self):
        self.notebook.select(self.tab2.frame)

    def button_next_enc(self):
        self.notebook.select(self.tab2a.frame)
        

    def button_next_encU(self):
        self.notebook.select(self.tab2b.frame)
        
    
    def button_next_encV(self):
        self.notebook.select(self.tab3.frame)

    def button_prev_dec(self):
        self.notebook.select(self.tab2b.frame)

    def button_prev_enc(self):
        self.notebook.select(self.tab1.frame)
        

    def button_prev_encU(self):
        self.notebook.select(self.tab2.frame)
        
    
    def button_prev_encV(self):
        self.notebook.select(self.tab2a.frame)

mk = MiniKyber()
