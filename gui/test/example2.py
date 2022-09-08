import customtkinter
import tkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("1000x600")
        self.title("small example app")
        self.minsize(600, 400)

        # create 2x2 grid system
        #self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
        
        self.label_1 = customtkinter.CTkLabel(master=self,
                                              text="BSC Token Sniper",
                                              text_font=("Roboto Medium", -48))  # font name and size in px
        self.label_1.grid(row=0, column=0, columnspan=3, pady=10, padx=10)
        
        self.bscAddress = customtkinter.CTkEntry(master=self)
        self.bscAddress.grid(row=1, column=0, padx=20, pady=5, stick="ew")
        self.bscAddress.insert(0,"BSC Address")
        
        self.privateKey = customtkinter.CTkEntry(master=self)
        self.privateKey.grid(row=2, column=0, padx=20, pady=5, stick="ew")
        self.privateKey.insert(0,"BSC Wallet Private Key")
        
        self.bscNode = customtkinter.CTkEntry(master=self)
        self.bscNode.grid(row=3, column=0, padx=20, pady=5, stick="ew")
        self.bscNode.insert(0,"https://bsc-dataseed.binance.org/")
        
        self.pancakeRouterAddress = customtkinter.CTkEntry(master=self)
        self.pancakeRouterAddress.grid(row=4, column=0, padx=20, pady=5, stick="ew")
        self.pancakeRouterAddress.insert(0,"0x10ED43C718714eb63d5aA57B78B54704E256024E")
        
        self.bnbAmount = customtkinter.CTkEntry(master=self)
        self.bnbAmount.grid(row=1, column=1, padx=20, pady=5, stick="ew")
        self.bnbAmount.insert(0,"0.05")
        
        self.takeProfit = customtkinter.CTkEntry(master=self)
        self.takeProfit.grid(row=2, column=1, padx=20, pady=5, stick="ew")
        self.takeProfit.insert(0,"1.5")
        
        self.gasAmt = customtkinter.CTkEntry(master=self)
        self.gasAmt.grid(row=3, column=1, padx=20, pady=5, stick="ew")
        self.gasAmt.insert(0,"300000")

        self.combobox = customtkinter.CTkComboBox(master=self, values=["Sample text 1", "Text 2"])
        self.combobox.grid(row=5, column=0, padx=20, pady=20, sticky="ew")
        self.button = customtkinter.CTkButton(master=self, command=self.button_callback, text="Start Bot")
        self.button.grid(row=5, column=1, padx=20, pady=20, sticky="ew")
        
        self.button = customtkinter.CTkButton(master=self, command=self.button_callback, text="Stop Bot")
        self.button.grid(row=5, column=2, padx=20, pady=20, sticky="ew")

    def button_callback(self):
        self.textbox.insert("insert", self.combobox.get() + "\n")


if __name__ == "__main__":
    app = App()
    app.mainloop()