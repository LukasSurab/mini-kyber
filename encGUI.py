import tkinter as tk
from tkinter import ttk
from tktooltip import ToolTip
from PIL import Image, ImageTk
from core import *
import tkinter.font as font
from tkinter import messagebox

class EncryptionTab:
    def __init__(self, notebook):
        self.frame = ttk.Frame(notebook)
        self.myFont = font.Font(size=20)

        self.infoButton = tk.Button(self.frame,text = "?",state='disabled')
        ToolTip(self.infoButton,msg = "Na zašifrovanie správy Mini-Kyber vyžaduje ako vstup public key pk, randimzer vector r a samotnú správu m, ktorú chceme zašifrovať.\n"
                + "Voliteľným parametrom je seed, podľa ktorý používa PRF.\n"
                + "Samotná funkcia encrypt vygeneruje dva náhodné šumy e_1 (vektor), e_2 (polynóm).\n"
                + "Následne transponuje maticu A a vypočíta u = A^T * r + e_1. u je teda vektor polynómov\n"
                + "Ďalej zmení správu na jej bitovú reprezentáciu a \"pozdvihne\" koeficienty.\n"
                +"Nakoniec transponuje t a vypočíta v = t^T * r + e2 + m. v je teda polynóm.\n"
                + "Výstupom šifrovania je zašifrovaná správa ako dvojica (u,v).")

        self.encrypted = false

        self.image2 = Image.open("encryptionFlow.png")
        self.test1 = ImageTk.PhotoImage(self.image2)
        self.label2 = ttk.Label(self.frame,image=self.test1)

        self.image1 = Image.open("encccS.png")
        self.test = ImageTk.PhotoImage(self.image1)
        self.label1 = ttk.Label(self.frame,image=self.test)
        
        self.loadPKButton = ttk.Button(self.frame,text = 'Load generated PK',command = self.button_LoadPublicKey,state = 'disabled')
        self.seedLabelRandomizer = ttk.Label(self.frame, text = 'seed for randomizer r')
        self.seedLabelRandomizerResult = ttk.Label(self.frame, text = 'randomizer r: ')
        self.encSeedRandomizerEntry = ttk.Entry(self.frame)
        self.encGenerateRButton = ttk.Button(self.frame,text = "Generate randomizer r",command = self.button_generateRandomizer)
        self.seedEncLabel = ttk.Label(self.frame, text = 'seed for encryption')
        self.seedEncEntry = ttk.Entry(self.frame,state='disabled')
        self.messageLabel = ttk.Label(self.frame, text = 'Message to encrypt')
        self.messageToEncEntry = ttk.Entry(self.frame,state='disabled')
        self.encButton = ttk.Button(self.frame,text = "Encrypt",command = self.button_Encrypt,state= 'disabled')
        self.encButtonLabel = ttk.Label(self.frame, text = 'Not yet encrypted')

        self.seedLabelRandomizer.place(x = 180,y = 10)
        self.encSeedRandomizerEntry.place(x = 180, y = 32)
        self.encGenerateRButton.place(x = 10, y = 30)
        self.seedLabelRandomizerResult.place(x = 10,y = 60)
        self.loadPKButton.place(x = 10, y = 150)
        self.seedEncLabel.place(x = 180,y = 200)
        self.seedEncEntry.place(x = 180, y = 222)
        self.messageLabel.place(x = 180,y = 250)
        self.messageToEncEntry.place(x = 180, y = 272)
        self.encButton.place(x = 10, y = 250)
        self.encButtonLabel.place(x = 10, y = 280)
        self.infoButton.place(x =350, y = 0)
        self.label2.place(x=450,y = 0)
        self.label1.place(x = 10, y = 345)

        self.r = None

        self.PKButton1 = None
        self.randomizerButton = None
        self.uButton = None


    def button_LoadPublicKey(self):
        with open("keyGenData.pickle", "rb") as f_in:

            # Deserialize the object from the file
            f = pickle.load(f_in)
        print(f)
        self.PKButton1 = tk.Button(self.frame,text = "A",state='disabled',background='lightblue')
        self.PKButton1['font'] = self.myFont
        self.PKButton1.place(x = 224,y = 390,width=117, height=117)
        self.tButton1 = tk.Button(self.frame,text = "t",state='disabled',background='lightblue')
        self.tButton1.place(x = 343,y = 390,width=33, height=117)
        self.tButton1['font'] = self.myFont
        self.a1 = f['A']
        self.t1 = f['t']
        aX1 = matrixXbartoX(self.a1)
        print(aX1)
        print(aX1[0])
        print(aX1[1])
        ToolTip(self.PKButton1, msg =str(aX1[0]) + "\n" + str(aX1[1]))
        ToolTip(self.tButton1, msg =str(smallRandomXbarToX(self.t1)))
        self.loadPKButton['state'] = 'disabled'
        self.encButton['state'] = 'enabled'
        self.seedEncEntry['state'] = 'enabled'
        self.messageToEncEntry['state'] = 'enabled'

    def button_generateRandomizer(self,seed = None):
        if self.encSeedRandomizerEntry.get() != '':
            seed = int (self.encSeedRandomizerEntry.get())
        else:
            seed = None
        print("seed:")
        print(seed)
        self.r = generate_small_randoms(seed)
        self.randomizerButton = tk.Button(self.frame,text = "r",state='disabled',background='lightgreen')
        self.seedLabelRandomizerResult['text'] = "Randomizer r was generated"
        ToolTip(self.randomizerButton,msg=str(smallRandomXbarToX(self.r)))
        self.randomizerButton.place(x = 90,y = 390,width=117, height=33)
        self.randomizerButton['font'] = self.myFont
        #if seed != None:
        self.encSeedRandomizerEntry.configure(state = 'disabled')
        self.encGenerateRButton['state'] = 'disabled'
        self.loadPKButton['state'] = 'enabled'

    def button_Encrypt(self,seed = None):
        if self.seedEncEntry.get() != '':
            seed = int (self.seedEncEntry.get())
        else:
            seed = None
        self.message = str(self.messageToEncEntry.get())
        print("seed:")
        print(seed)
        print("message")
        if self.message == "":
            messagebox.showerror('Python Error', 'Error: Missing message m!')
        else:
            self.u, self.v, self.e1, self.e2 = encrypt(self.a1,self.t1,poly_message(self.message),self.r,seed)
            self.messageButton = tk.Button(self.frame,text = "m",state='disabled',background='lightgrey')
            ToolTip(self.messageButton,msg=str(msgXbarToX(poly_message(self.message))))
            self.messageButton.place(x = 343,y = 584,width=33, height=33)
            self.messageButton['font'] = self.myFont
            self.error1Button = tk.Button(self.frame,text = "e1",state='disabled',background='yellow')
            ToolTip(self.error1Button,msg=str(smallRandomXbarToX(self.e1)))
            self.error1Button.place(x = 224,y = 529,width=117, height=33)
            self.error1Button['font'] = self.myFont
            self.error2Button = tk.Button(self.frame,text = "e2",state='disabled',background='yellow')
            ToolTip(self.error2Button,msg=str(msgXbarToX(self.e2)))
            self.error2Button.place(x = 343,y = 529,width=33, height=33)
            self.error2Button['font'] = self.myFont
            self.uButton = tk.Button(self.frame,text = "u",state='disabled',background='red')
            ToolTip(self.uButton,msg=str(smallRandomXbarToX(self.u)))
            self.uButton.place(x = 224,y = 636,width=117, height=33)
            self.uButton['font'] = self.myFont
            self.vButton = tk.Button(self.frame,text = "v",state='disabled',background='red')
            ToolTip(self.vButton,msg=str(msgXbarToX(self.v)))
            self.vButton.place(x = 343,y = 636,width=33, height=33)
            self.vButton['font'] = self.myFont

            self.encButtonLabel['text'] = "Encrypted: " + str(self.message)

            #if seed != None:
            self.seedEncEntry.configure(state = 'disabled')
            self.encButton['state'] = 'disabled'
            #if(str(self.messageToEncEntry.get()) != ""):
            self.messageToEncEntry.configure(state = 'disabled')
            self.encrypted = true
