import tkinter as tk
from tkinter import ttk
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
        i = 1
        while (i < 5):
            self.notebook.tab(i, state = 'disabled')
            i += 1
        
        self.resetButtonKeyGen = ttk.Button(self.tab1.frame,text = "reset",command = self.button_resetKeyGen)
        self.resetButtonKeyGen.place(x = 1000,y= 600)
        self.resetButtonEnc = ttk.Button(self.tab2.frame,text = "reset",command = self.button_resetEnc)
        self.resetButtonEnc.place(x = 1000,y= 600)
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

    def button_resetKeyGen(self):
        self.button_resetEnc()
        self.tab2a.reset_button()
        self.tab2b.reset_button()
        self.tab3.button_reset()
        self.tab1.s = None
        self.tab1.e = None
        self.tab1.a = None
        self.tab1.t = None
        self.tab1.generatedKeys = false
        i = 1
        while (i < 5):
            self.notebook.tab(i, state = 'disabled')
            i += 1
        
        self.tab1.errorELabel['text'] = "error e is not generated"
        self.tab1.secretSLabel['text'] = "secret s is not generated"
        self.tab1.PKALabel['text'] = "publicKey A is not generated"
        self.tab1.PKtLabel['text'] = "publicKey t is not generated"
        self.tab1.generateSButton['state'] = 'enabled'
        self.tab1.entrySSeed['state'] = 'enabled'
        self.tab1.PKgeneateEButton['state'] = 'disabled'
        self.tab1.enrtryErrorSeed['state'] = 'disabled'
        self.tab1.PKGenButton['state'] = 'disabled'
        self.tab1.entryPublicKeySeed['state'] = "disabled"

        if self.tab1.sButton is not None:
            self.tab1.sButton.destroy()
            self.tab1.sButton = None
        if self.tab1.tButton is not None:
            self.tab1.tButton.destroy()
            self.tab1.tButton = None
        if self.tab1.errorButton is not None:
            self.tab1.errorButton.destroy()
            self.tab1.errorButton = None
        if self.tab1.PKButton is not None:
            self.tab1.PKButton.destroy()
            self.tab1.PKButton = None

    def button_resetEnc(self):
        self.tab2a.reset_button()
        self.tab2b.reset_button()
        self.tab3.button_reset()
        self.tab2.r = None
        self.tab2.encrypted = false
        i = 2
        while (i < 5):
            self.notebook.tab(i, state = 'disabled')
            i += 1

        self.tab2.encGenerateRButton['state'] = 'enabled'
        self.tab2.loadPKButton['state'] = 'disabled'
        self.tab2.encButton['state'] = 'disabled'
        self.tab2.encSeedRandomizerEntry['state'] = 'enabled'
        self.tab2.seedEncEntry['state'] = 'disabled'
        self.tab2.messageToEncEntry['state'] = 'disabled'
        if self.tab2.PKButton1 is not None:
            self.tab2.PKButton1.destroy()
            self.tab2.tButton1.destroy()
        if self.tab2.randomizerButton is not None:
            self.tab2.randomizerButton.destroy()
        if self.tab2.uButton is not None:
            self.tab2.uButton.destroy()
            self.tab2.vButton.destroy()
            self.tab2.messageButton.destroy()
            self.tab2.error1Button.destroy()
            self.tab2.error2Button.destroy()

    def button_next_keyGen(self):
        if self.tab1.generatedKeys is true:
            self.notebook.tab(1, state = 'normal')
            self.notebook.select(self.tab2.frame)
        else:
            messagebox.showerror('Python Error', 'Error: Keys not yet generated!')

    def button_next_enc(self):
        if self.tab2.encrypted is true:
            i = 2
            while (i < 5):
                self.notebook.tab(i, state = 'normal')
                i += 1
            self.notebook.select(self.tab2a.frame)
        else:
            messagebox.showerror('Python Error', 'Error: Nothing yet encrypted!')


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
