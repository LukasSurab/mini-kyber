import tkinter as tk
from tkinter import ttk
from tktooltip import ToolTip
from PIL import Image, ImageTk
from pickleTRYING import *
from keyGenGUI import *
from encGUI import *
import tkinter.font as font

class FrameVTab:
    def __init__(self, notebook):
        self.frame = ttk.Frame(notebook)
        self.v = None
        self.e2V = None
        self.tV = None
        self.mV = None
        self.sV = None
        self.rV = None

        self.sButton = None
        self.vButton = None
        self.AButtonHover = None

        self.myFont = font.Font(size=20)
        self.image1 = Image.open("vBig.png")
        self.test = ImageTk.PhotoImage(self.image1)
        self.label1 = ttk.Label(self.frame,image=self.test)
        self.label1.place(x = 120, y = -50)
        self.loadButtonv = ttk.Button(self.frame,text = "Load v",command=self.load_button_v)
        self.loadButtonv.place(x = 10, y = 630)
        self.loadButtonAE = ttk.Button(self.frame,text = "Load A/e",command=self.load_t_detailed_v)
        self.loadButtonAE.place(x = 100, y = 630)
        self.loadButtonsk = ttk.Button(self.frame,text = "Load s",command=self.load_button_skV)
        self.loadButtonsk.place(x = 190, y = 630)
        self.resetButton = ttk.Button(self.frame,text = "Reset",command=self.reset_button)
        self.resetButton.place(x = 1000, y = 600)
        self.errorButtonStill = tk.Button(self.frame,text = "E",state='disabled',background='yellow')
        ToolTip(self.errorButtonStill,msg="e + e2")
        self.errorButtonStill.place(x = 710,y = 523,width=48, height=48)
        self.errorButtonStill['font'] = self.myFont


    def load_button_v(self):
        with open("encryptionVData.pickle", "rb") as v_in:

            # Deserialize the object from the file
            v = pickle.load(v_in)
        self.v = v['v']
        self.e2V = v['e2']
        self.tV = v['t']
        self.mV = v['m']
        self.rV = v['r']

        self.rButtonHover = tk.Button(self.frame,text = "r",state='disabled',background='lightgreen')
        ToolTip(self.rButtonHover,msg=str(self.rV))
        self.rButtonHover.place(x = 248,y = 31,width=175, height=48)
        self.rButtonHover['font'] = self.myFont
        self.rButtonHover2 = tk.Button(self.frame,text = "r",state='disabled',background='lightgreen')
        ToolTip(self.rButtonHover2,msg=str(self.rV))
        self.rButtonHover2.place(x = 248,y = 246,width=175, height=48)
        self.rButtonHover2['font'] = self.myFont
        self.rButtonHover3 = tk.Button(self.frame,text = "r",state='disabled',background='lightgreen')
        ToolTip(self.rButtonHover3,msg=str(self.rV))
        self.rButtonHover3.place(x = 248,y = 460,width=175, height=48)
        self.rButtonHover3['font'] = self.myFont
        self.tButtonHover = tk.Button(self.frame,text = "t",state='disabled',background='lightblue')
        ToolTip(self.tButtonHover,msg=str(self.tV))
        self.tButtonHover.place(x = 430,y = 31,width=48, height=175)
        self.tButtonHover['font'] = self.myFont
        self.e2ButtonHover = tk.Button(self.frame,text = "e2",state='disabled',background='yellow')
        ToolTip(self.e2ButtonHover,msg=str(self.e2V))
        self.e2ButtonHover.place(x = 522,y = 94,width=48, height=48)
        self.e2ButtonHover['font'] = self.myFont
        self.e2ButtonHover2 = tk.Button(self.frame,text = "e2",state='disabled',background='yellow')
        ToolTip(self.e2ButtonHover2,msg=str(self.e2V))
        self.e2ButtonHover2.place(x = 817,y = 309,width=48, height=48)
        self.e2ButtonHover2['font'] = self.myFont
        self.mButtonHover = tk.Button(self.frame,text = "m",state='disabled',background='lightgrey')
        ToolTip(self.mButtonHover,msg=str(self.mV))
        self.mButtonHover.place(x = 611,y = 94,width=48, height=48)
        self.mButtonHover['font'] = self.myFont
        self.mButtonHover2 = tk.Button(self.frame,text = "m",state='disabled',background='lightgrey')
        ToolTip(self.mButtonHover2,msg=str(self.mV))
        self.mButtonHover2.place(x = 908,y = 309,width=48, height=48)
        self.mButtonHover2['font'] = self.myFont
        self.mButtonHover3 = tk.Button(self.frame,text = "m",state='disabled',background='lightgrey')
        ToolTip(self.mButtonHover3,msg=str(self.mV))
        self.mButtonHover3.place(x = 817,y = 523,width=48, height=48)
        self.mButtonHover3['font'] = self.myFont
        self.vButton = tk.Button(self.frame,text = "v",state='disabled',background='red')
        ToolTip(self.vButton,msg=str(self.v))
        self.vButton.place(x = 145,y = 94,width=48, height=48)
        self.vButton['font'] = self.myFont
        self.loadButtonv['state'] = 'disabled'
        

    def load_t_detailed_v(self):
        with open("keyGenData.pickle", "rb") as t_in:

            # Deserialize the object from the file
            t = pickle.load(t_in)
        self.A = t['A']
        self.eV = t['e']
        self.AButtonHover = tk.Button(self.frame,text = "A",state='disabled',background='lightblue')
        ToolTip(self.AButtonHover,msg=str(self.A))
        self.AButtonHover.place(x = 440,y = 246,width=175, height=175)
        self.AButtonHover['font'] = self.myFont
        self.AButtonHover2 = tk.Button(self.frame,text = "A",state='disabled',background='lightblue')
        ToolTip(self.AButtonHover2,msg=str(self.A))
        self.AButtonHover2.place(x = 440,y = 460,width=175, height=175)
        self.AButtonHover2['font'] = self.myFont
        self.eButtonHover = tk.Button(self.frame,text = "e",state='disabled',background='yellow')
        ToolTip(self.eButtonHover,msg=str(self.eV))
        self.eButtonHover.place(x = 710,y = 246,width=48, height=175)
        self.eButtonHover['font'] = self.myFont
        self.loadButtonAE['state'] = 'disabled'


    def load_button_skV(self):
        with open("keyGenSecretData.pickle", "rb") as s_in:

            # Deserialize the object from the file
            s = pickle.load(s_in)
        self.s = s['s']
        self.sButton = tk.Button(self.frame,text = "s",state='disabled',background='lightgreen')
        ToolTip(self.sButton,msg=str(self.s))
        self.sButton.place(x = 625,y = 460,width=48, height=175)
        self.sButton['font'] = self.myFont
        self.sButton2 = tk.Button(self.frame,text = "s",state='disabled',background='lightgreen')
        ToolTip(self.sButton2,msg=str(self.s))
        self.sButton2.place(x = 625,y = 245,width=48, height=175)
        self.sButton2['font'] = self.myFont
        self.loadButtonsk['state'] = 'disabled'

    def reset_button(self):
        self.loadButtonAE['state'] = 'enabled'
        self.loadButtonv['state'] = 'enabled'
        self.loadButtonsk['state'] = 'enabled'
        if self.vButton is not None:
            self.vButton.destroy()
            self.rButtonHover.destroy()
            self.rButtonHover2.destroy()
            self.rButtonHover3.destroy()
            self.tButtonHover.destroy()
            self.mButtonHover.destroy()
            self.mButtonHover2.destroy()
            self.mButtonHover3.destroy()
            self.e2ButtonHover.destroy()
            self.e2ButtonHover2.destroy()
        if self.AButtonHover is not None:
            self.AButtonHover.destroy()
            self.AButtonHover2.destroy()
            self.eButtonHover.destroy()
        if self.sButton is not None:
            self.sButton.destroy()
            self.sButton2.destroy()