import tkinter as tk  
from PIL import Image, ImageTk  
from tkinter.filedialog import askdirectory
from tkinter import messagebox
import os 

# # create empty lists for photo id's to be stored to
# empty = []
# not_empty = []

# counter = 0
# src = './images/'
# list_images = []

# for d in os.listdir(src):
#     if d[0] != ".":
#         list_images.append(d)
# print(list_images)




# root = tk.Tk()


# root.title("display image")  
# def open_image(img):

#     def leftKey(event):
#         print("left key pressed")

#     def rightKey(event):
#         print("right key pressed")
 
#     im=Image.open(src+img)  
#     photo=ImageTk.PhotoImage(im)  

#     cv = tk.Canvas()  
#     cv.pack(side='top', fill='both', expand='yes')  
#     cv.create_image(50, 50, image=photo, anchor='nw')  
#     root.geometry("500x500")

#     if event == leftKey(event):
#         root.bind('<Left>', leftKey)

#     if event == rightKey(event):
#         root.bind('<Right>', rightKey)

    
# for image in list_images:
#     open_image(image)

#     root.mainloop()

# class ImageRelabel(tk.Frame):
#     def __init__(self, parent, *args, **kwargs):
#         tk.Frame.__init__(self, parent, *args, **kwargs)

#         self.root = parent
#         self.root.wm_title('Image Relabel')
#         src = './images/'

#         self.list_images = []

#         for d in os.listdir(src):
#             if d[0] != '.':
#                 self.list_images.append(d)

#         self.frame = tk.Frame(self.root, width=500, height=500, bd=2)

#         self.cv = tk.Canvas(self.frame, height=500, width=500)

#         self.counter = 0
#         self.max_count = len(self.list_images)-1
#         self.next_image()

#         def next_image(self):
#             if self.counter > self.max_count:
#                 print("No more images")
#             else:
#                 im = Image.open("{}{}".format(src, self.list_images[counter]))
#                 if event == keyLeft
        
#         def next_step(self):
#             self.im = Image.open("{}")


class ImageClassifyer(tk.Frame):


    def __init__(self, parent, *args, **kwargs):

        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.root = parent
        self.root.wm_title("Classify Image")   
        src = "./images/"

        self.image_names = []
        self.list_images = []
        # for d in os.listdir(src):
        #     if d[0] != '.':
        #         self.list_images.append(d)
        for folder in os.listdir(src):
            if folder[0] != '.':
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
        self.next_image()

    def leftKey(self, event):
        print("left")
        self.next_image()
    def rightKey(self, evetnt):
        print('right')
        self.next_image()

    def next_image(self):

        if self.counter > self.max_count:
            messagebox.showinfo("Congratz", "No More Images!")
            print("No more images")
            print(self.list_images)
            print(self.image_names)
            exit()
        else:
            im = Image.open("{}{}".format("./images/", self.list_images[self.counter][0]))
            if (490-im.size[0])<(390-im.size[1]):
                width = 490
                height = width*im.size[1]/im.size[0]
                self.next_step(height, width)
            else:
                height = 390
                width = height*im.size[0]/im.size[1]
                self.next_step(height, width)

    def next_step(self, height, width):
        self.im = Image.open("{}{}".format("./images/", self.list_images[self.counter][0]))
        self.im.thumbnail((width, height), Image.ANTIALIAS)
        self.root.photo = ImageTk.PhotoImage(self.im)
        self.photo = ImageTk.PhotoImage(self.im)

        if self.counter == 0:
            self.cv1.create_image(0, 0, anchor = 'nw', image = self.photo)

        else:
            self.im.thumbnail((width, height), Image.ANTIALIAS)
            self.cv1.delete("all")
            self.cv1.create_image(0, 0, anchor = 'nw', image = self.photo)
        self.counter += 1


if __name__ == "__main__":
    root = tk.Tk() 
    MyApp = ImageClassifyer(root)
    tk.mainloop()