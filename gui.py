import tkinter as tk
from tkinter import ttk
from tktooltip import ToolTip
from PIL import Image, ImageTk

class MiniKyber:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('1100x700')
        self.window.title("Mini Kyber")
        self.window.minsize(1050,700)
        self.notebook = ttk.Notebook(self.window,width=1050, height=700)
        
        self.tab1 = KeyGenerationTab(self.notebook)
        self.tab2 = EncryptionTab(self.notebook)
        self.tab3 = DecryptionTab(self.notebook)
        
        self.notebook.add(self.tab1.frame, text='KeyGen')
        self.notebook.add(self.tab2.frame, text='Encryption')
        self.notebook.add(self.tab3.frame, text='Decryption')
        
        self.notebook.pack(expand=1, fill='both')

        self.window.mainloop()

class KeyGenerationTab:
    def __init__(self, notebook):
        self.frame = ttk.Frame(notebook)

        self.infoButton = tk.Button(self.frame,text = "?")
        ToolTip(self.infoButton,msg = "KeyGen pozostáva z generovania kľúčov s a pk.\nVšetky koeficienty polynómov sú mod q = 137, q - prvočíslo.\nPre q musí platiť (q - 1) = 2^n * p.\nPolynómy sú z okruhu f = x^8 + 1.\n1)Secret Key s je generovaný ako vektor malých polynómov.\nV našom modeli tvoria s DVA polynómy.\n2)Public Key pk sa skladá z dvoch častí.\n a) Matice náhodných polnómov A.\n b) t = A*s + e, kde e je náhodný malý šum.")

        
        #pic
        self.image1 = Image.open("keygen.PNG")
        self.test = ImageTk.PhotoImage(self.image1)
        self.label1 = ttk.Label(self.frame,image=self.test)

        self.image2 = Image.open("kg.PNG")
        self.test1 = ImageTk.PhotoImage(self.image2)
        self.label2 = ttk.Label(self.frame,image=self.test1)


        self.seedLabelA = ttk.Label(self.frame, text = 'seed for matrix A')
        self.enrtryASeed = ttk.Entry(self.frame)
        self.PKgenerateAButton = ttk.Button(self.frame,text = "Generate matrix A", command = self.button_generateMatrixA)
        self.matrixALabel = ttk.Label(self.frame,text = "matrix A: ")
        self.seedLabelError = ttk.Label(self.frame, text = 'seed for error e')
        self.enrtryErrorSeed = ttk.Entry(self.frame)
        self.PKgeneateEButton = ttk.Button(self.frame,text = "Generate error e",command = self.button_generateError)
        self.errorELabel = ttk.Label(self.frame,text = "error e: ")
        self.seedKeyGen = ttk.Label(self.frame, text = 'seed for SK and PK')
        self.enrtryKeyGenSeed = ttk.Entry(self.frame)
        self.KeyGenButton = ttk.Button(self.frame,text = "Generate Keys",command = self.button_generateKeys)
        self.SKLabel = ttk.Label(self.frame,text = "secretKey: ")
        self.PKALabel = ttk.Label(self.frame,text = "publicKey A: ")
        self.PKtLabel = ttk.Label(self.frame,text = "publicKey t: ")

        self.seedLabelA.place(x = 120, y = 10)
        self.enrtryASeed.place(x = 120, y = 32)
        self.PKgenerateAButton.place(x= 0, y = 30)
        self.matrixALabel.place(x= 0, y = 60)
        self.seedLabelError.place(x = 120, y = 230)
        self.enrtryErrorSeed.place(x = 120, y = 252)
        self.PKgeneateEButton.place(x=0, y = 250)
        self.errorELabel.place(x= 0, y = 280)
        self.seedKeyGen.place(x = 120, y = 330)
        self.enrtryKeyGenSeed.place(x = 120, y = 352)
        self.KeyGenButton.place(x= 0, y = 350)
        self.SKLabel.place(x= 0, y = 380)
        self.PKALabel.place(x= 0, y = 440)
        self.PKtLabel.place(x= 0, y = 530)
        self.label1.place(x=250,y = 210)
        self.infoButton.place(x =250, y = 0)
        self.label2.place(x=630,y = 10)

    def button_generateKeys(self):
        seed = int (self.enrtryKeyGenSeed.get())
        print(seed)
        self.enrtryKeyGenSeed.configure(state = 'disabled')
        print('a button was pressed')


    def button_generateMatrixA(self,seed = None):
        seed = int (self.enrtryASeed.get())
        print(seed)
        resultButton = ttk.Button(self.frame,text = "Show generated Matrix A on hover",state='disabled')
        resultButton.place(x = 0,y = 90)
        ToolTip(resultButton, msg = "matrix A: " + "[100*x^7 + 42*x^6 + 63*x^5 + 180*x^4 + 67*x^3 + 181*x^2 + 75*x + 12  34*x^7 + 97*x^6 + 156*x^5 + 55*x^4 + 199*x^3 + 154*x^2 + 49*x + 122]\n[22*x^7 + 208*x^6 + 105*x^5 + 35*x^4 + 16*x^3 + 44*x^2 + 16*x + 14 195*x^7 + 231*x^6 + 87*x^5 + 197*x^4 + 174*x^3 + 27*x^2 + 26*x + 216]")
        self.matrixALabel['text'] = "matrix A was generated"
        self.enrtryASeed.configure(state = 'disabled')
        print('a button was pressed')

    def button_generateError(self,seed = None):
        seed = int (self.enrtryErrorSeed.get())
        print(seed)
        self.enrtryErrorSeed.configure(state = 'disabled')
        print('a button was pressed')    


class EncryptionTab:
    def __init__(self, notebook):
        self.frame = ttk.Frame(notebook)
        self.text1 = tk.Text(master = self.frame,width= 60,height=30)
        self.text1.configure(state='disabled')
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

        self.seedLabelRandomizer.place(x = 150,y = 10)
        self.encSeedRandomizerEntry.place(x = 150, y = 32)
        self.encGenerateRButton.place(x = 0, y = 30)
        self.seedLabelRandomizerResult.place(x = 0,y = 60)
        self.loadPKButton.place(x = 0, y = 110)
        self.seedEncLabel.place(x = 150,y = 120)
        self.seedEncEntry.place(x = 150, y = 142)
        self.messageLabel.place(x = 150,y = 170)
        self.messageToEncEntry.place(x = 150, y = 192)
        self.encButton.place(x = 0, y = 160)
        self.text1.place(x = 290, y = 30)

    def button_LoadPublicKey(self):
        print('a button was pressed')

    def button_generateRandomizer(self,seed = None):
        seed = int (self.encSeedRandomizerEntry.get())
        print(seed)
        #matrixALabel['text'] = "matrix A: " + str(156)
        self.encSeedRandomizerEntry.configure(state = 'disabled')
        print('a button was pressed')

    def button_Encrypt(self,seed = None):
        seed = int (self.seedEncEntry.get())
        message = str(self.messageToEncEntry.get())
        print(seed)
        print(message)
        self.seedEncEntry.configure(state = 'disabled')
        if(str(self.messageToEncEntry.get()) != ""):
            self.messageToEncEntry.configure(state = 'disabled')
        print('a button was pressed')

class DecryptionTab:
    def __init__(self, notebook):
        self.frame = ttk.Frame(notebook)

        self.text2 = tk.Text(master = self.frame,width= 60,height=30)
        self.text2.configure(state='disabled')
        self.loadCipherTextButton = ttk.Button(self.frame, text = 'Load Ciphertext',command = self.button_LoadCipherText)
        self.loadSecretKeyButton = ttk.Button(self.frame, text = 'Load Secret Key', command = self.button_LoadSecretKey)
        self.decButton = ttk.Button(self.frame, text = 'Decrypt',command = self.button_Decrypt)


        self.loadCipherTextButton.place(x = 0,y = 30)
        self.loadSecretKeyButton.place(x = 0, y = 100)
        self.decButton.place(x = 0, y = 170)
        self.text2.place(x = 290, y = 30)

    def button_LoadCipherText(self,):
        print('a button was pressed')

    def button_LoadSecretKey(self,seed = None):
        print('a button was pressed')

    def button_Decrypt(self,seed = None):
        print('a button was pressed')

mk = MiniKyber()