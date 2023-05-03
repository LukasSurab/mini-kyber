import tkinter as tk
from tkinter import ttk
from tktooltip import ToolTip
from PIL import Image, ImageTk
import pickle
import tkinter.font as font

class FrameUTab:
    def __init__(self, notebook):
        self.frame = ttk.Frame(notebook)
        self.myFont = font.Font(size=20)
        self.u = None
        self.e1U = None
        self.AU = None
        self.rU = None
        self.mU = None
        self.vU = None

        self.sButton = None
        self.AButtonHover = None

        self.image1 = Image.open("uBig.png")
        self.test = ImageTk.PhotoImage(self.image1)
        self.label1 = ttk.Label(self.frame,image=self.test)
        self.label1.place(x = 30, y = 100)
        self.loadButton = ttk.Button(self.frame,text = "Load u/v/m",command=self.load_button_u)
        self.loadButton.place(x = 10, y = 630)
        self.loadButtonSK = ttk.Button(self.frame,text = "Load s",command=self.load_button_skU)
        self.loadButtonSK.place(x = 100, y = 630)
        self.resetButton = ttk.Button(self.frame,text='reset',command=self.reset_button)
        self.resetButton.place(x = 1000, y = 600)
    
    def load_button_u(self):
        with open("encryptionUData.pickle", "rb") as u_in:

            # Deserialize the object from the file
            u = pickle.load(u_in)
        self.u = u['u']
        self.e1U = u['e1']
        self.AU = u['A']
        self.rU = u['r']
        self.mU = u['m']
        self.vU = u['v']
        self.AButtonHover = tk.Button(self.frame,text = "A",state='disabled',background='lightblue')
        ToolTip(self.AButtonHover,msg=str(self.AU))
        self.AButtonHover.place(x = 526,y = 132,width=173, height=173)
        self.AButtonHover['font'] = self.myFont
        self.AButtonHover2 = tk.Button(self.frame,text = "A",state='disabled',background='lightblue')
        ToolTip(self.AButtonHover2,msg=str(self.AU))
        self.AButtonHover2.place(x = 526,y = 345,width=173, height=173)
        self.AButtonHover2['font'] = self.myFont
        self.rButtonHover = tk.Button(self.frame,text = "r",state='disabled',background='lightgreen')
        ToolTip(self.rButtonHover,msg=str(self.rU))
        self.rButtonHover.place(x = 340,y = 132,width=173, height=48)
        self.rButtonHover['font'] = self.myFont
        self.rButtonHover2 = tk.Button(self.frame,text = "r",state='disabled',background='lightgreen')
        ToolTip(self.rButtonHover2,msg=str(self.rU))
        self.rButtonHover2.place(x = 340,y = 345,width=173, height=48)
        self.rButtonHover2['font'] = self.myFont
        self.rButtonHover3 = tk.Button(self.frame,text = "r",state='disabled',background='lightgreen')
        ToolTip(self.rButtonHover3,msg=str(self.rU))
        self.rButtonHover3.place(x = 340,y = 132,width=173, height=48)
        self.rButtonHover3['font'] = self.myFont
        self.uButtonHover = tk.Button(self.frame,text = "u",state='disabled',background='red')
        ToolTip(self.uButtonHover,msg=str(self.u))
        self.uButtonHover.place(x = 40,y = 132,width=173, height=48)
        self.uButtonHover['font'] = self.myFont
        self.e1ButtonHover = tk.Button(self.frame,text = "e1",state='disabled',background='yellow')
        ToolTip(self.e1ButtonHover,msg=str(self.e1U))
        self.e1ButtonHover.place(x = 740,y = 132,width=173, height=48)
        self.e1ButtonHover['font'] = self.myFont
        self.vButtonHover = tk.Button(self.frame,text = "v",state='disabled',background='red')
        ToolTip(self.vButtonHover,msg=str(self.vU))
        self.vButtonHover.place(x = 897,y = 407,width=48, height=48)
        self.vButtonHover['font'] = self.myFont
        self.mButtonHover = tk.Button(self.frame,text = "m",state='disabled',background='lightgrey')
        ToolTip(self.mButtonHover,msg=str(self.mU))
        self.mButtonHover.place(x = 974,y = 407,width=48, height=48)
        self.mButtonHover['font'] = self.myFont
        self.loadButton['state'] = 'disabled'

    def load_button_skU(self):
        with open("keyGenSecretData.pickle", "rb") as s_in:

            # Deserialize the object from the file
            s = pickle.load(s_in)
        self.s = s['s']
        self.sButton = tk.Button(self.frame,text = "s",state='disabled',background='lightgreen')
        ToolTip(self.sButton,msg=str(self.s))
        self.sButton.place(x = 708,y = 345,width=48, height=173)
        self.sButton['font'] = self.myFont
        self.sButton1 = tk.Button(self.frame,text = "s",state='disabled',background='lightgreen')
        ToolTip(self.sButton1,msg=str(self.s))
        self.sButton1.place(x = 937,y = 132,width=48, height=173)
        self.sButton1['font'] = self.myFont
        self.sButton2 = tk.Button(self.frame,text = "s",state='disabled',background='lightgreen')
        ToolTip(self.sButton2,msg=str(self.s))
        self.sButton2.place(x = 222,y = 132,width=48, height=173)
        self.sButton2['font'] = self.myFont
        self.loadButtonSK['state'] = 'disabled'

    def reset_button(self):
        self.loadButton['state'] = 'enabled'
        self.loadButtonSK['state'] = 'enabled'
        if self.sButton is not None:
            self.sButton.destroy()
            self.sButton1.destroy()
            self.sButton2.destroy()
        if self.AButtonHover is not None:
            self.AButtonHover.destroy()
            self.AButtonHover2.destroy()
            self.uButtonHover.destroy()
            self.e1ButtonHover.destroy()
            self.vButtonHover.destroy()
            self.rButtonHover.destroy()
            self.rButtonHover2.destroy()
            self.rButtonHover3.destroy()
            self.mButtonHover.destroy()
