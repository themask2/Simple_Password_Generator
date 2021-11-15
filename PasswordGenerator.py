from tkinter import *;
from tkinter import ttk;
from random import *

class Application:
    def __init__(self, master=None):
        # Creating a container
        self.widget1 = Frame(master);
        self.widget1.pack(side=TOP);
        #Creating a widget
        self.msg = Label(self.widget1, text="Click to generate a password");
        self.msg["font"] = ("Arial", "12", "normal", "bold");
        self.msg.pack();
        #Creating another widget -> A Button
        self.generate = Button(self.widget1);
        self.generate["text"] = "Generate";
        self.generate["font"] = ("Arial", "12");
        self.generate["width"] = 10;
        self.generate.bind("<Button-1>", self.generatePassword);
        self.generate.pack();

    def generatePassword(self, event):
        pswd = [];
        
        for x in range(3):
            pswd.append(choice('abcdefghijklmnopqrstuvwxyz'));
        
        for x in range(2):
            pswd.append(choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'));
        
        for x in range(2):
            pswd.append(choice('0123456789'));

        pswd.append(choice('!?#@$&_'));

        shuffle(pswd);
        pswd = "".join(pswd);
        self.msg["text"] = pswd;



root = Tk();

#This changes the Title of the main Window
root.title("Password Generator");

#This predefine the size of the mais Window
root.geometry("400x60");

Application(root);
root.mainloop();
