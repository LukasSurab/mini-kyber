import tkinter as tk
from tkinter import ttk
from tktooltip import ToolTip
from PIL import Image, ImageTk
from core import *
import tkinter.font as font
from tkinter import messagebox
from helperFunctions import *

class KeyGenerationTab:
    def __init__(self, notebook):
        self.frame = ttk.Frame(notebook)

        self.infoButton = tk.Button(self.frame,text = "?",state='disabled')
        ToolTip(self.infoButton,msg = "KeyGen pozostáva z generovania kľúčov s a pk.\nVšetky koeficienty polynómov sú mod q = 137, q - prvočíslo.\nPre q musí platiť (q - 1) = 2^n * p.\nPolynómy sú z okruhu f = x^8 + 1.\n1)Secret Key s je generovaný ako vektor malých polynómov.\nV našom modeli tvoria s DVA polynómy.\n2)Public Key pk sa skladá z dvoch častí.\n a) Matice náhodných polnómov A.\n b) t = A*s + e, kde e je náhodný malý šum.")

        #pic
        self.image1 = Image.open("keyggg.png")
        self.test = ImageTk.PhotoImage(self.image1)
        self.label1 = ttk.Label(self.frame,image=self.test)

        self.generatedKeys = false
        
        self.image2 = Image.open("keygenFix.png")
        self.test1 = ImageTk.PhotoImage(self.image2)
        self.label2 = ttk.Label(self.frame,image=self.test1)

        self.s = None
        self.e = None
        self.a = None
        self.t = None
        self.sButton = None
        self.tButton = None
        self.errorButton = None
        self.PKButton = None
        self.myFont = font.Font(size=20)

        #self.resetButton = ttk.Button(self.frame,text = "reset",command = self.button_reset)

        self.seedLabelS = ttk.Label(self.frame, text = 'seed for Secret Key')
        self.entrySSeed = ttk.Entry(self.frame)
        self.generateSButton = ttk.Button(self.frame,text = "Generate secret s", command = self.button_generateSecret)
        self.secretSLabel = ttk.Label(self.frame,text = "Secret s is not generated")
        ToolTip(self.generateSButton, msg = 'vygeneruje Secret Key s')


        self.seedLabelError = ttk.Label(self.frame, text = 'seed for error e')
        self.enrtryErrorSeed = ttk.Entry(self.frame,state = 'disabled')
        self.PKgeneateEButton = ttk.Button(self.frame,text = "Generate error e",command = self.button_generateError, state = 'disabled')
        self.errorELabel = ttk.Label(self.frame,text = "error e is not generated")

        self.seedPublicKey = ttk.Label(self.frame, text = 'seed for PK')
        self.entryPublicKeySeed = ttk.Entry(self.frame,state= 'disabled')
        self.PKGenButton = ttk.Button(self.frame,text = "Generate Public Key",command = self.button_generatePK, state = 'disabled')
        self.PKALabel = ttk.Label(self.frame,text = "publicKey A is not generated")
        self.PKtLabel = ttk.Label(self.frame,text = "publicKey t is not generated")

        self.seedLabelS.place(x = 170, y = 10)
        self.entrySSeed.place(x = 170, y = 32)
        self.generateSButton.place(x= 10, y = 30)
        self.secretSLabel.place(x= 10, y = 60)

        self.seedLabelError.place(x = 170, y = 230)
        self.enrtryErrorSeed.place(x = 170, y = 252)
        self.PKgeneateEButton.place(x=10, y = 250)
        self.errorELabel.place(x= 10, y = 280)
        
        self.seedPublicKey.place(x = 170, y = 330)
        self.entryPublicKeySeed.place(x = 170, y = 352)
        self.PKGenButton.place(x= 10, y = 350)
        self.PKALabel.place(x= 10, y = 440)
        self.PKtLabel.place(x= 10, y = 530)
        
        self.label1.place(x=350,y = 210)
        self.infoButton.place(x = 350, y = 0)
        self.label2.place(x=730,y = 10)

        #self.resetButton.place(x = 1000,y= 600)

    def button_generateSecret(self):
        if self.entrySSeed.get() != '':
            seed = int (self.entrySSeed.get())
        else:
            seed = None
        print(seed)
        self.s = generate_secret_key(seed)
        self.sButton = tk.Button(self.frame,text = "s",state='disabled',background='lightgreen')
        ToolTip(self.sButton,msg=str(smallRandomXbarToX(self.s)))
        self.secretSLabel['text'] = "secret s was generated"
        self.sButton.place(x = 533,y = 246,width=30, height=106)
        self.sButton['font'] = self.myFont
        #if seed != None:
        self.entrySSeed.configure(state = 'disabled')
        self.generateSButton['state'] = "disabled"
        self.PKgeneateEButton['state'] = "enabled"
        self.enrtryErrorSeed['state'] = "enabled" 


    def button_generatePK(self,seed = None):
        if self.entryPublicKeySeed.get() != '':
            seed = int (self.entryPublicKeySeed.get())
        else:
            seed = None
        print(seed)
        if self.s is not None and self.e is not None:
            self.PKButton = tk.Button(self.frame,text = "A",state='disabled',background='lightblue')
            self.PKButton['font'] = self.myFont
            self.PKButton.place(x = 419,y = 246,width=106, height=106)
            self.tButton = tk.Button(self.frame,text = "t",state='disabled',background='lightblue')
            self.tButton.place(x = 652,y = 246,width=30, height=106)
            self.tButton['font'] = self.myFont
            self.a,self.t = generate_public_key(self.s,self.e,seed)
            aX = matrixXbartoX(self.a)
            print(aX)
            print(aX[0])
            print(aX[1])
            ToolTip(self.PKButton, msg =str(aX[0]) + "\n" + str(aX[1]))
            ToolTip(self.tButton, msg =str(smallRandomXbarToX(self.t)))
            self.PKALabel['text'] = "matrix A was generated"
            self.PKtLabel['text'] = "public key part t was generated"
            #if seed != None:
            self.PKGenButton['state'] = "disabled"
            self.entryPublicKeySeed.configure(state = 'disabled')
        else:
            messagebox.showerror('Python Error', 'Error: Missing secret s/error e!')
        print('a button was pressed')
        self.generatedKeys = true

    def button_generateError(self,seed = None):
        if self.enrtryErrorSeed.get() != '':
            seed = int (self.enrtryErrorSeed.get())
        else:
            seed = None
        print(seed)
        self.e = generate_keyGen_error(seed)
        self.errorButton = tk.Button(self.frame,text = "e",state='disabled',background='yellow')
        self.errorELabel['text'] = "error e was generated"
        ToolTip(self.errorButton,msg=str(smallRandomXbarToX(self.e)))
        self.errorButton.place(x = 585,y = 246,width=30, height=106)
        self.errorButton['font'] = self.myFont
        #if seed != None:
        self.enrtryErrorSeed.configure(state = 'disabled')
        self.PKgeneateEButton['state'] = "disabled"    
        self.enrtryErrorSeed['state'] = 'disabled'
        self.PKGenButton['state'] = "enabled"
        self.entryPublicKeySeed['state'] = "enabled" 
