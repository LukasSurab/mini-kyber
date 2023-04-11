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

        self.infoButton = tk.Button(self.frame,text = "?",state='disabled')
        ToolTip(self.infoButton,msg = "KeyGen pozostáva z generovania kľúčov s a pk.\nVšetky koeficienty polynómov sú mod q = 137, q - prvočíslo.\nPre q musí platiť (q - 1) = 2^n * p.\nPolynómy sú z okruhu f = x^8 + 1.\n1)Secret Key s je generovaný ako vektor malých polynómov.\nV našom modeli tvoria s DVA polynómy.\n2)Public Key pk sa skladá z dvoch častí.\n a) Matice náhodných polnómov A.\n b) t = A*s + e, kde e je náhodný malý šum.")

        
        #pic
        self.image1 = Image.open("keyggg.PNG")
        self.test = ImageTk.PhotoImage(self.image1)
        self.label1 = ttk.Label(self.frame,image=self.test)

        
        self.image2 = Image.open("keygenerator.PNG")
        self.test1 = ImageTk.PhotoImage(self.image2)
        self.label2 = ttk.Label(self.frame,image=self.test1)


        self.seedLabelA = ttk.Label(self.frame, text = 'seed for matrix A')
        self.enrtryASeed = ttk.Entry(self.frame)
        self.PKgenerateAButton = ttk.Button(self.frame,text = "Generate matrix A", command = self.button_generateMatrixA)
        self.matrixALabel = ttk.Label(self.frame,text = "matrix A: ")
        ToolTip(self.PKgenerateAButton, msg = 'vygeneruje 2x2 maticu polynomov')


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
        if self.enrtryKeyGenSeed.get() != '':
            seed = int (self.enrtryKeyGenSeed.get())
        else:
            seed = None
        print(seed)
        if seed != None:
            self.enrtryKeyGenSeed.configure(state = 'disabled')
        print('a button was pressed')


    def button_generateMatrixA(self,seed = None):
        if self.enrtryASeed.get() != '':
            seed = int (self.enrtryASeed.get())
        else:
            seed = None
        print(seed)
        resultButton = ttk.Button(self.frame,text = "Show generated Matrix A on hover",state='disabled')
        resultButton.place(x = 0,y = 90)
        ToolTip(resultButton, msg = "matrix A: " + "[100*x^7 + 42*x^6 + 63*x^5 + 180*x^4 + 67*x^3 + 181*x^2 + 75*x + 12\n  34*x^7 + 97*x^6 + 156*x^5 + 55*x^4 + 199*x^3 + 154*x^2 + 49*x + 122]\n[22*x^7 + 208*x^6 + 105*x^5 + 35*x^4 + 16*x^3 + 44*x^2 + 16*x + 14\n 195*x^7 + 231*x^6 + 87*x^5 + 197*x^4 + 174*x^3 + 27*x^2 + 26*x + 216]")
        self.matrixALabel['text'] = "matrix A was generated"
        if seed != None:
            self.enrtryASeed.configure(state = 'disabled')
        print('a button was pressed')

    def button_generateError(self,seed = None):
        if self.enrtryErrorSeed.get() != '':
            seed = int (self.enrtryErrorSeed.get())
        else:
            seed = None
        print(seed)
        if seed != None:
            self.enrtryErrorSeed.configure(state = 'disabled')
        print('a button was pressed')    


class EncryptionTab:
    def __init__(self, notebook):
        self.sada = False
        self.frame = ttk.Frame(notebook)

        self.infoButton = tk.Button(self.frame,text = "?",command = self.button_infoButtonChangePics)
        ToolTip(self.infoButton,msg = "Na zašifrovanie správy Mini-Kyber vyžaduje ako vstup public key pk, randimzer vector r a samotnú správu m, ktorú chceme zašifrovať.\n"
                + "Voliteľným parametrom je seed, podľa ktorý používa PRF.\n"
                + "Samotná funkcia encrypt vygeneruje dva náhodné šumy e_1 (vektor), e_2 (polynóm).\n"
                + "Následne transponuje maticu A a vypočíta u = A^T * r + e_1.\n"
                + "Ďalej zmení správu na jej bitovú reprezentáciu a \"pozdvihne\" koeficienty.\n"
                +"Nakoniec transponuje t a vypočíta v = t^T * r + e2 + m.\n"
                + "Výstupom šifrovania je zašifrovaná správa ako dvojica (u,v).")

        
        self.image2 = Image.open("encryptionFlow.PNG")
        self.test1 = ImageTk.PhotoImage(self.image2)
        self.label2 = ttk.Label(self.frame,image=self.test1)

        self.image1 = Image.open("encccS.PNG")
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

        self.seedLabelRandomizer.place(x = 150,y = 10)
        self.encSeedRandomizerEntry.place(x = 150, y = 32)
        self.encGenerateRButton.place(x = 0, y = 30)
        self.seedLabelRandomizerResult.place(x = 0,y = 60)
        self.loadPKButton.place(x = 0, y = 150)
        self.seedEncLabel.place(x = 150,y = 200)
        self.seedEncEntry.place(x = 150, y = 222)
        self.messageLabel.place(x = 150,y = 250)
        self.messageToEncEntry.place(x = 150, y = 272)
        self.encButton.place(x = 0, y = 250)
        self.infoButton.place(x =300, y = 0)
        self.label2.place(x=400,y = 0)
        self.label1.place(x = 10, y = 345)

    def button_infoButtonChangePics(self):
        print('a button was pressed')
        if self.sada is True:
            self.test1 = ImageTk.PhotoImage(file='encccS.png')
            self.label1.place(x = 10, y = 345)
            self.label1['image'] = self.test1
            #self.label1.image = self.test1

            self.test2 = ImageTk.PhotoImage(file='encryptionFlow.PNG')
            self.label2.place(x=400,y = 0)
            self.label2['image'] = self.test2
            #self.label2.image = self.test2

            self.sada = False
        else:
            self.test1 = ImageTk.PhotoImage(file='uuuuu.PNG')
            self.label1.place(x=10,y = 400)
            self.label1['image'] = self.test1
            #self.label1.image = self.test1

            self.test2 = ImageTk.PhotoImage(file='vvvvv1.PNG')
            self.label2.place(x=450,y = -50)
            self.label2['image'] = self.test2
            #self.label2.image = self.test2

            self.sada = True


    def button_LoadPublicKey(self):
        print('a button was pressed')

    def button_generateRandomizer(self,seed = None):
        if self.encSeedRandomizerEntry.get() != '':
            seed = int (self.encSeedRandomizerEntry.get())
        else:
            seed = None
        print(seed)
        #matrixALabel['text'] = "matrix A: " + str(156)
        if seed != None:
            self.encSeedRandomizerEntry.configure(state = 'disabled')
        print('a button was pressed')

    def button_Encrypt(self,seed = None):
        if self.seedEncEntry.get() != '':
            seed = int (self.seedEncEntry.get())
        else:
            seed = None
        message = str(self.messageToEncEntry.get())
        print(seed)
        print(message)
        if seed != None:
            self.seedEncEntry.configure(state = 'disabled')
        if(str(self.messageToEncEntry.get()) != ""):
            self.messageToEncEntry.configure(state = 'disabled')
        print('a button was pressed')

class DecryptionTab:
    def __init__(self, notebook):
        self.frame = ttk.Frame(notebook)

        self.image1 = Image.open("decc.PNG")
        self.test = ImageTk.PhotoImage(self.image1)
        self.label1 = ttk.Label(self.frame,image=self.test)

        self.image2 = Image.open("decryptionFlow.PNG")
        self.test1 = ImageTk.PhotoImage(self.image2)
        self.label2 = ttk.Label(self.frame,image=self.test1)

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


        self.loadCipherTextButton.place(x = 0,y = 30)
        self.loadSecretKeyButton.place(x = 0, y = 150)
        self.decButton.place(x = 0, y = 270)
        self.infoButton.place(x = 300, y = 0)
        self.label1.place(x = 10, y = 400)
        self.label2.place(x=600,y = 0)


    def button_LoadCipherText(self):
        print('a button was pressed')

    def button_LoadSecretKey(self):
        print('a button was pressed')

    def button_Decrypt(self):
        print('a button was pressed')

mk = MiniKyber()