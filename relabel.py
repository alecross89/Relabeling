import tkinter as tk  
from PIL import Image, ImageTk  
from tkinter.filedialog import askdirectory
from tkinter import messagebox
import os 
import shutil

class ImageClassifyer(tk.Frame):


    def __init__(self, parent, *args, **kwargs):

        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.root = parent
        src = "./test_folder/"
        self.empty_path = './empty'
        self.not_empty_path = './not_empty'

        if not os.path.exists(self.empty_path):
            os.mkdir(self.empty_path)
    
        if not os.path.exists(self.not_empty_path):
            os.mkdir(self.not_empty_path)
        
        self.image_names = []
        self.list_images = []
        self.image_folder = []
        self.empty = []
        self.not_empty = []

        for folder in os.listdir(src):
            if folder[0] != '.':
                self.image_folder.append(src+folder+'/')
                self.image_names.append(folder)

                self.list_images.append(os.listdir(src+folder))

        
        self.frame1 = tk.Frame(self.root, width=500, height=400, bd=2)
        self.frame1.grid(row=1, column=0)

        self.cv1 = tk.Canvas(self.frame1, height=390, width=490, background="white", bd=1, relief=tk.RAISED)
        self.cv1.grid(row=1,column=0)

        self.root.bind('<Left>', self.leftKey)
        self.root.bind('<Right>', self.rightKey)

        self.counter = 0
        self.max_count = len(self.list_images)-1
        self.display_image(500, 500)
        
    def display_image(self, width, height):
        try:   
            self.root.wm_title(self.image_names[self.counter]) 
            self.im = Image.open("{}".format(self.image_folder[self.counter] + self.list_images[self.counter][0]))
            self.im.thumbnail((width, height), Image.ANTIALIAS)
            self.root.photo = ImageTk.PhotoImage(self.im)
            self.photo = ImageTk.PhotoImage(self.im)
            if self.counter == 0:
                self.cv1.create_image(0, 0, anchor = 'nw', image = self.photo)
            else:
                self.im.thumbnail((width, height), Image.ANTIALIAS)
                self.cv1.delete("all")
                self.cv1.create_image(0, 0, anchor = 'nw', image = self.photo)
            print("current {}".format(self.image_folder[self.counter]))
        except OSError as e:
            print(e)

    def leftKey(self, event):

        if self.counter < self.max_count:

            shutil.move(self.image_folder[self.counter], self.empty_path)

            self.counter += 1
            self.display_image(500,500)

        elif self.counter == self.max_count:

            self.display_image(500,500)

            shutil.move(self.image_folder[self.counter], self.empty_path)
            
            messagebox.showinfo("Congratz", "No More Images!")
            exit()

    def rightKey(self, event):

        if self.counter < self.max_count:

            shutil.move(self.image_folder[self.counter], self.not_empty_path)
            
            self.counter += 1
            self.display_image(500,500)

        elif self.counter == self.max_count:
            
            self.display_image(500,500)
            
            shutil.move(self.image_folder[self.counter], self.not_empty_path)
            
            messagebox.showinfo("Congratz", "No More Images!")
            exit()


if __name__ == "__main__":
    root = tk.Tk() 
    MyApp = ImageClassifyer(root)
    tk.mainloop()