import tkinter as tk
from tkinter import ttk
from tktooltip import ToolTip
from PIL import Image, ImageTk
from core import *
import tkinter.font as font

class DecryptionTab:
    def __init__(self, notebook):
        self.frame = ttk.Frame(notebook)

        self.myFont = font.Font(size=20)

        self.s = None
        self.u = None
        self.v = None

        self.m_nLabel = None

        self.messageButtonS = None
        self.messageButtonM = None
        self.uButtonHover = None


        self.image1 = Image.open("decc.png")
        self.test = ImageTk.PhotoImage(self.image1)
        self.label1 = ttk.Label(self.frame,image=self.test)

        self.image2 = Image.open("decryptionFlow.png")
        self.test1 = ImageTk.PhotoImage(self.image2)
        self.label2 = ttk.Label(self.frame,image=self.test1)

        self.resetButton = ttk.Button(self.frame,text = "reset",command = self.button_reset)


        self.loadCipherTextButton = ttk.Button(self.frame, text = 'Load Ciphertext',command = self.button_LoadCipherText)
        self.loadSecretKeyButton = ttk.Button(self.frame, text = 'Load Secret Key', command = self.button_LoadSecretKey,state = 'disabled')
        self.decButton = ttk.Button(self.frame, text = 'Decrypt',command = self.button_Decrypt,state = 'disabled')

        self.infoButton = tk.Button(self.frame,text = "?",state='disabled')
        ToolTip(self.infoButton,msg = "Na dešifrovanie správy Mini-Kyber vyžaduje ako vstup zašifrovanú správu ako dvojicu (u,v) a secret key sk == s.\n"
                + "Ako prvá časť dešifrovania sa vypočíta zašumený výsledok m_n = v - s^T * u = e^T * r + e_2 + m + s^T * e_1\n"
                + "Na tento výsledok sa následne použije dekódovacia funckia a teda dostaneme m = decode(m_n).\n"
                + "Dekódovacia funckia funguje tak, že všetky bity porovná či sú bližšie ku q/2 alebo ku N, resp 0.\n"
                +"Bity následne zaokrúhli na hodnoty buď q/2 ak sú bližšie ku q/2, alebo na 0 v ostatných prípadoch.\n"
                +"Výsledkom bude správa m s pozdvihnutými koeficientami.\n"
                +"Nakoniec použije funkciu copmress, ktorá nám vráti správu do jej bitovej hodnoty, z ktorej získame výslednú dešifrovanú správu.")

        self.loadCipherTextButton.place(x = 0,y = 30)
        self.loadSecretKeyButton.place(x = 0, y = 150)
        self.decButton.place(x = 0, y = 270)
        self.infoButton.place(x = 350, y = 0)
        self.label1.place(x = 10, y = 400)
        self.label2.place(x=600,y = 0)
        self.resetButton.place(x = 1000,y= 600)

    def button_LoadCipherText(self):
        with open("CipherTextData.pickle", "rb") as uv_in:

            # Deserialize the object from the file
            uv = pickle.load(uv_in)
        self.u = uv['u']
        self.v = uv['v']
        self.uButtonHover = tk.Button(self.frame,text = "u",state='disabled',background='red')
        ToolTip(self.uButtonHover,msg=str(self.u))
        self.uButtonHover.place(x = 148,y = 465,width=175, height=48)
        self.uButtonHover['font'] = self.myFont
        self.vButtonHover = tk.Button(self.frame,text = "v",state='disabled',background='red')
        ToolTip(self.vButtonHover,msg=str(self.v))
        self.vButtonHover.place(x = 64,y = 526,width=48, height=48)
        self.vButtonHover['font'] = self.myFont
        self.loadCipherTextButton['state'] = 'disabled'
        self.loadSecretKeyButton['state'] = 'enabled'


    def button_LoadSecretKey(self):
        with open("keyGenSecretData.pickle", "rb") as s_in:

            # Deserialize the object from the file
            s = pickle.load(s_in)
        self.s = s['s']
        self.messageButtonS = tk.Button(self.frame,text = "s",state='disabled',background='lightgreen')
        ToolTip(self.messageButtonS,msg=str(s['s_T']))
        self.messageButtonS.place(x = 330,y = 465,width=48, height=175)
        self.messageButtonS['font'] = self.myFont
        self.loadSecretKeyButton['state'] = 'disabled'
        self.decButton['state'] = 'enabled'

    def button_Decrypt(self):
        self.decrypted = decrypt(self.u,self.v,self.s)
        self.messageButtonM = tk.Button(self.frame,text = "m",state='disabled',background='lightgrey')
        ToolTip(self.messageButtonM,msg=self.decrypted['msg'])
        self.messageButtonM.place(x = 437,y = 526,width=48, height=48)
        self.messageButtonM['font'] = self.myFont
        self.decButton['state'] = 'disabled'
        with open("result.pickle", "rb") as res_in:

            # Deserialize the object from the file
            res = pickle.load(res_in)
        print(res)
        if self.m_nLabel is not None:
            self.m_nLabel.destroy()
            self.m_nLabelCoeffs.destroy()
            self.m_nLabelCoeffsDecode.destroy()
            self.m_nLabelResultBit.destroy()
            self.m_nLabelResultChar.destroy()
        self.m_nLabel = ttk.Label(self.frame,text = str(msgXbarToX(res['m_n'])))
        self.m_nLabel.place(x = 100, y =200)
        self.m_nLabelCoeffs = ttk.Label(self.frame,text = "Coefficients of the message: " + str(res['m_nSplit']))
        self.m_nLabelCoeffs.place(x = 100, y =230)
        self.m_nLabelCoeffsDecode = ttk.Label(self.frame,text = "Coefficients after decoding: " + str(res['coefficients']))
        self.m_nLabelCoeffsDecode.place(x = 100, y =260)
        self.m_nLabelResultBit = ttk.Label(self.frame,text = "Result after compression: " + str(res['m_nSplitDsc']))
        self.m_nLabelResultBit.place(x = 100, y =290)
        self.m_nLabelResultChar = ttk.Label(self.frame,text = "Bit representation to ASCII: " + str(res['result']['msg']))
        self.m_nLabelResultChar.place(x = 100, y =320)

    def button_reset(self):
        self.s = None
        self.u = None
        self.v = None

        if self.messageButtonS is not None:
            self.messageButtonS.destroy()
        if self.messageButtonM is not None:
            self.messageButtonM.destroy()
            self.m_nLabel.destroy()
            self.m_nLabelCoeffs.destroy()
            self.m_nLabelCoeffsDecode.destroy()
            self.m_nLabelResultBit.destroy()
            self.m_nLabelResultChar.destroy()
        if self.uButtonHover is not None:
            self.uButtonHover.destroy()
            self.vButtonHover.destroy()
        self.loadCipherTextButton['state'] = 'enabled'
        self.loadSecretKeyButton['state'] = 'disabled'
        self.decButton['state'] = 'disabled'
