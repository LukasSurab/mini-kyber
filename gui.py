import tkinter as tk
from tkinter import ttk
from tktooltip import ToolTip
from PIL import Image, ImageTk
from pickleTRYING import *
import tkinter.font as font
from tkinter import messagebox



class MiniKyber:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('1280x720')
        self.window.title("Mini Kyber")
        self.window.minsize(1200,720)
        self.window.maxsize(1200,720)
        self.notebook = ttk.Notebook(self.window,width=1200, height=720)
        
        #TODO obrazky interaktivne

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

class KeyGenerationTab:
    def __init__(self, notebook):
        self.frame = ttk.Frame(notebook)

        self.infoButton = tk.Button(self.frame,text = "?",state='disabled')
        ToolTip(self.infoButton,msg = "KeyGen pozostáva z generovania kľúčov s a pk.\nVšetky koeficienty polynómov sú mod q = 137, q - prvočíslo.\nPre q musí platiť (q - 1) = 2^n * p.\nPolynómy sú z okruhu f = x^8 + 1.\n1)Secret Key s je generovaný ako vektor malých polynómov.\nV našom modeli tvoria s DVA polynómy.\n2)Public Key pk sa skladá z dvoch častí.\n a) Matice náhodných polnómov A.\n b) t = A*s + e, kde e je náhodný malý šum.")

        #pic
        self.image1 = Image.open("keyggg.png")
        self.test = ImageTk.PhotoImage(self.image1)
        self.label1 = ttk.Label(self.frame,image=self.test)

        
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

        self.resetButton = ttk.Button(self.frame,text = "reset",command = self.button_reset)

        self.seedLabelS = ttk.Label(self.frame, text = 'seed for Secret Key')
        self.entrySSeed = ttk.Entry(self.frame)
        self.generateSButton = ttk.Button(self.frame,text = "Generate secret s", command = self.button_generateSecret)
        self.secretSLabel = ttk.Label(self.frame,text = "Secret s is not generated")
        ToolTip(self.generateSButton, msg = 'vygeneruje Secret Key s')


        self.seedLabelError = ttk.Label(self.frame, text = 'seed for error e')
        self.enrtryErrorSeed = ttk.Entry(self.frame)
        self.PKgeneateEButton = ttk.Button(self.frame,text = "Generate error e",command = self.button_generateError)
        self.errorELabel = ttk.Label(self.frame,text = "error e is not generated")

        self.seedPublicKey = ttk.Label(self.frame, text = 'seed for PK')
        self.entryPublicKeySeed = ttk.Entry(self.frame)
        self.PKGenButton = ttk.Button(self.frame,text = "Generate Public Key",command = self.button_generatePK)
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

        self.resetButton.place(x = 1000,y= 600)

    def button_generateSecret(self):
        if self.entrySSeed.get() != '':
            seed = int (self.entrySSeed.get())
        else:
            seed = None
        print(seed)
        self.s = generate_secret_key(seed)
        self.sButton = tk.Button(self.frame,text = "s",state='disabled',background='lightgreen')
        ToolTip(self.sButton,msg=str(self.s))
        self.secretSLabel['text'] = "secret s was generated"
        self.sButton.place(x = 533,y = 246,width=30, height=106)
        self.sButton['font'] = self.myFont
        if seed != None:
            self.entrySSeed.configure(state = 'disabled')
        print('a button was pressed')


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
            ToolTip(self.PKButton, msg = "matrix A: " + str(aX[0]) + "\n" + str(aX[1]))
            ToolTip(self.tButton, msg = "t: " + str(self.t))
            self.PKALabel['text'] = "matrix A was generated"
            self.PKtLabel['text'] = "public key part t was generated"
            if seed != None:
                self.entryPublicKeySeed.configure(state = 'disabled')
        else:
            messagebox.showerror('Python Error', 'Error: Missing secret s/error e!')
        print('a button was pressed')

    def button_generateError(self,seed = None):
        if self.enrtryErrorSeed.get() != '':
            seed = int (self.enrtryErrorSeed.get())
        else:
            seed = None
        print(seed)
        self.e = generate_keyGen_error(seed)
        self.errorButton = tk.Button(self.frame,text = "e",state='disabled',background='yellow')
        self.errorELabel['text'] = "error e was generated"
        ToolTip(self.errorButton,msg=str(self.e))
        self.errorButton.place(x = 585,y = 246,width=30, height=106)
        self.errorButton['font'] = self.myFont
        if seed != None:
            self.enrtryErrorSeed.configure(state = 'disabled')
        print('a button was pressed')    

    def button_reset(self):
        self.s = None
        self.e = None
        self.a = None
        self.t = None
        
        self.errorELabel['text'] = "error e is not generated"
        self.secretSLabel['text'] = "secret s is not generated"
        self.PKALabel['text'] = "publicKey A is not generated"
        self.PKtLabel['text'] = "publicKey t is not generated"

        if self.sButton is not None:
            self.sButton.destroy()
            self.sButton = None
        if self.tButton is not None:
            self.tButton.destroy()
            self.tButton = None
        if self.errorButton is not None:
            self.errorButton.destroy()
            self.errorButton = None
        if self.PKButton is not None:
            self.PKButton.destroy()
            self.PKButton = None

class EncryptionTab:
    def __init__(self, notebook):
        self.sada = False
        self.frame = ttk.Frame(notebook)
        self.myFont = font.Font(size=20)

        self.infoButton = tk.Button(self.frame,text = "?",state='disabled')
        ToolTip(self.infoButton,msg = "Na zašifrovanie správy Mini-Kyber vyžaduje ako vstup public key pk, randimzer vector r a samotnú správu m, ktorú chceme zašifrovať.\n"
                + "Voliteľným parametrom je seed, podľa ktorý používa PRF.\n"
                + "Samotná funkcia encrypt vygeneruje dva náhodné šumy e_1 (vektor), e_2 (polynóm).\n"
                + "Následne transponuje maticu A a vypočíta u = A^T * r + e_1.\n"
                + "Ďalej zmení správu na jej bitovú reprezentáciu a \"pozdvihne\" koeficienty.\n"
                +"Nakoniec transponuje t a vypočíta v = t^T * r + e2 + m.\n"
                + "Výstupom šifrovania je zašifrovaná správa ako dvojica (u,v).")

        
        self.image2 = Image.open("encryptionFlow.png")
        self.test1 = ImageTk.PhotoImage(self.image2)
        self.label2 = ttk.Label(self.frame,image=self.test1)

        self.image1 = Image.open("encccS.png")
        self.test = ImageTk.PhotoImage(self.image1)
        self.label1 = ttk.Label(self.frame,image=self.test)
        
        self.loadPKButton = ttk.Button(self.frame,text = 'Load generated PK',command = self.button_LoadPublicKey)
        self.seedLabelRandomizer = ttk.Label(self.frame, text = 'seed for randomizer r')
        self.seedLabelRandomizerResult = ttk.Label(self.frame, text = 'randomizer r: ')
        self.encSeedRandomizerEntry = ttk.Entry(self.frame)
        self.encGenerateRButton = ttk.Button(self.frame,text = "Generate randomizer r",command = self.button_generateRandomizer)
        self.seedEncLabel = ttk.Label(self.frame, text = 'seed for encryption')
        self.seedEncEntry = ttk.Entry(self.frame)
        self.messageLabel = ttk.Label(self.frame, text = 'Message to encrypt')
        self.messageToEncEntry = ttk.Entry(self.frame)
        self.encButton = ttk.Button(self.frame,text = "Encrypt",command = self.button_Encrypt)
        self.resetButton = ttk.Button(self.frame,text = "reset",command = self.button_reset)

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
        self.infoButton.place(x =350, y = 0)
        self.label2.place(x=450,y = 0)
        self.label1.place(x = 10, y = 345)
        self.resetButton.place(x = 1000,y= 600)
    """
    def button_infoButtonChangePics(self):
        print('a button was pressed')
        if self.sada is True:
            self.test1 = ImageTk.PhotoImage(file='encccS.png')
            self.label1.place(x = 10, y = 345)
            self.label1['image'] = self.test1
            #self.label1.image = self.test1

            self.test2 = ImageTk.PhotoImage(file='encryptionFlow.png')
            self.label2.place(x=400,y = 0)
            self.label2['image'] = self.test2
            #self.label2.image = self.test2

            self.sada = False
        else:
            self.test1 = ImageTk.PhotoImage(file='uuuuu.png')
            self.label1.place(x=10,y = 400)
            self.label1['image'] = self.test1
            #self.label1.image = self.test1

            self.test2 = ImageTk.PhotoImage(file='vvvvv1.png')
            self.label2.place(x=450,y = -50)
            self.label2['image'] = self.test2
            #self.label2.image = self.test2

            self.sada = True
    """
    def button_reset(self):
        print('a button was pressed')


    def button_LoadPublicKey(self):
        print('a button was pressed')
        with open("keyGenData.pickle", "rb") as f_in:

            # Deserialize the object from the file
            f = pickle.load(f_in)
        print(f)
        self.PKButton1 = tk.Button(self.frame,text = "A",state='disabled',background='lightblue')
        self.PKButton1['font'] = self.myFont
        self.PKButton1.place(x = 226,y = 390,width=117, height=117)
        self.tButton1 = tk.Button(self.frame,text = "t",state='disabled',background='lightblue')
        self.tButton1.place(x = 343,y = 390,width=33, height=117)
        self.tButton1['font'] = self.myFont
        self.a1 = f['A']
        self.t1 = f['t']
        aX1 = matrixXbartoX(self.a1)
        print(aX1)
        print(aX1[0])
        print(aX1[1])
        ToolTip(self.PKButton1, msg = "matrix A: " + str(aX1[0]) + "\n" + str(aX1[1]))
        ToolTip(self.tButton1, msg = "t: " + str(self.t1))

    def button_generateRandomizer(self,seed = None):
        if self.encSeedRandomizerEntry.get() != '':
            seed = int (self.encSeedRandomizerEntry.get())
        else:
            seed = None
        print(seed)
        self.r = generate_small_randoms(seed)
        self.randomizerButton = tk.Button(self.frame,text = "r",state='disabled',background='lightgreen')
        self.seedLabelRandomizerResult['text'] = "Randomizer r was generated"
        ToolTip(self.randomizerButton,msg=str(self.r))
        self.randomizerButton.place(x = 90,y = 390,width=117, height=33)
        self.randomizerButton['font'] = self.myFont
        if seed != None:
            self.encSeedRandomizerEntry.configure(state = 'disabled')
        print('a button was pressed')

    def button_Encrypt(self,seed = None):
        if self.seedEncEntry.get() != '':
            seed = int (self.seedEncEntry.get())
        else:
            seed = None
        self.message = str(self.messageToEncEntry.get())
        print(seed)
        print(self.message)
        self.u, self.v, self.e1, self.e2 = encrypt(self.a1,self.t1,poly_message(self.message),self.r,seed)
        self.messageButton = tk.Button(self.frame,text = "m",state='disabled',background='lightgrey')
        ToolTip(self.messageButton,msg=str(self.message))
        self.messageButton.place(x = 343,y = 583,width=33, height=33)
        self.messageButton['font'] = self.myFont
        self.error1Button = tk.Button(self.frame,text = "e1",state='disabled',background='yellow')
        ToolTip(self.error1Button,msg=str(self.e1))
        self.error1Button.place(x = 223,y = 528,width=117, height=33)
        self.error1Button['font'] = self.myFont
        self.error2Button = tk.Button(self.frame,text = "e2",state='disabled',background='yellow')
        ToolTip(self.error2Button,msg=str(self.e2))
        self.error2Button.place(x = 343,y = 528,width=33, height=33)
        self.error2Button['font'] = self.myFont
        self.uButton = tk.Button(self.frame,text = "u",state='disabled',background='red')
        ToolTip(self.uButton,msg=str(self.u))
        self.uButton.place(x = 223,y = 635,width=117, height=33)
        self.uButton['font'] = self.myFont
        self.vButton = tk.Button(self.frame,text = "v",state='disabled',background='red')
        ToolTip(self.vButton,msg=str(self.v))
        self.vButton.place(x = 343,y = 635,width=33, height=33)
        self.vButton['font'] = self.myFont

        if seed != None:
            self.seedEncEntry.configure(state = 'disabled')
        if(str(self.messageToEncEntry.get()) != ""):
            self.messageToEncEntry.configure(state = 'disabled')
        print('a button was pressed')

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
        self.image1 = Image.open("uBig.png")
        self.test = ImageTk.PhotoImage(self.image1)
        self.label1 = ttk.Label(self.frame,image=self.test)
        self.label1.place(x = 30, y = 100)
        self.loadButton = ttk.Button(self.frame,text = "Load u/v/m",command=self.load_button_u)
        self.loadButton.place(x = 10, y = 630)
        self.loadButton = ttk.Button(self.frame,text = "Load s",command=self.load_button_skU)
        self.loadButton.place(x = 100, y = 630)
    
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
        self.rButtonHover4 = tk.Button(self.frame,text = "r",state='disabled',background='lightgreen')
        ToolTip(self.rButtonHover4,msg=str(self.rU))
        self.rButtonHover4.place(x = 340,y = 345,width=173, height=48)
        self.rButtonHover4['font'] = self.myFont
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

    def load_button_skU(self):
        with open("keyGenSecretDataTransposed.pickle", "rb") as s_in:

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

    def reset_button(self):
        print("pressed")

class FrameVTab:
    def __init__(self, notebook):
        self.frame = ttk.Frame(notebook)
        self.v = None
        self.e2V = None
        self.tV = None
        self.mV = None
        self.sV = None
        self.rV = None
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

    def reset_button(self):
        print("pressed")

class DecryptionTab:
    def __init__(self, notebook):
        self.frame = ttk.Frame(notebook)

        self.myFont = font.Font(size=20)

        self.s = None
        self.u = None
        self.v = None

        self.image1 = Image.open("decc.png")
        self.test = ImageTk.PhotoImage(self.image1)
        self.label1 = ttk.Label(self.frame,image=self.test)

        self.image2 = Image.open("decryptionFlow.png")
        self.test1 = ImageTk.PhotoImage(self.image2)
        self.label2 = ttk.Label(self.frame,image=self.test1)

        self.resetButton = ttk.Button(self.frame,text = "reset",command = self.button_reset)


        self.loadCipherTextButton = ttk.Button(self.frame, text = 'Load Ciphertext',command = self.button_LoadCipherText)
        self.loadSecretKeyButton = ttk.Button(self.frame, text = 'Load Secret Key', command = self.button_LoadSecretKey)
        self.decButton = ttk.Button(self.frame, text = 'Decrypt',command = self.button_Decrypt)

        self.infoButton = tk.Button(self.frame,text = "?",state='disabled')
        ToolTip(self.infoButton,msg = "Na dešifrovanie správy Mini-Kyber vyžaduje ako vstup zašifrovanú správu ako dvojicu (u,v) a secret key sk == s.\n"
                + "Ako prvá časť dešifrovania sa vypočíta zašumený výsledok m_n = v - s^T * u = e^T * r + e_2 + m + s^T * e_1\n"
                + "Na tento výsledok sa následne použije dekódovacia funckia a teda dostaneme m = decode(m_n).\n"
                + "Dekódovacia funckia funguje tak, že všetky bity porovná či sú bližšie ku q/2 alebo ku N, resp 0.\n"
                +"Bity následne zaokrúhli na hodnoty buď q/2 ak sú bližšie ku q/2, alebo na 0 v ostatných prípadoch.\n"
                +"Výsledkom bude správa m s pozdvihnutými koeficientami.\n"
                +"Nakoniec použije funkciu copmress, ktorá nám vráti správu do jej bitovej hodnoty, z ktorej získame výslednú dešifrovanú správu.")

        self.StepsDecodeDecryptedButton = ttk.Button(self.frame,text = "Decode steps",state='disabled',command = self.button_decryptSteps)

        self.loadCipherTextButton.place(x = 0,y = 30)
        self.loadSecretKeyButton.place(x = 0, y = 150)
        self.decButton.place(x = 0, y = 270)
        self.infoButton.place(x = 350, y = 0)
        self.label1.place(x = 10, y = 400)
        self.label2.place(x=600,y = 0)
        self.resetButton.place(x = 1000,y= 600)
        self.StepsDecodeDecryptedButton.place(x = 250, y = 150)

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


    def button_LoadSecretKey(self):
        with open("keyGenSecretData.pickle", "rb") as s_in:

            # Deserialize the object from the file
            s = pickle.load(s_in)
        self.s = s['s']
        self.messageButton = tk.Button(self.frame,text = "s",state='disabled',background='lightgreen')
        ToolTip(self.messageButton,msg=str(s['s_T']))
        self.messageButton.place(x = 330,y = 465,width=48, height=175)
        self.messageButton['font'] = self.myFont

    def button_Decrypt(self):
        self.decrypted = decrypt(self.u,self.v,self.s)
        self.messageButton = tk.Button(self.frame,text = "m",state='disabled',background='lightgrey')
        ToolTip(self.messageButton,msg=self.decrypted['msg'])
        self.messageButton.place(x = 437,y = 526,width=48, height=48)
        self.messageButton['font'] = self.myFont
        self.StepsDecodeDecryptedButton['state'] = 'enabled'

    def button_reset(self):
        print('a button was pressed')

    def button_decryptSteps(self):
        with open("result.pickle", "rb") as res_in:

            # Deserialize the object from the file
            res = pickle.load(res_in)
        print(res)
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

mk = MiniKyber()
