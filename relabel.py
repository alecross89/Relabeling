import tkinter as tk  
from PIL import Image, ImageTk  
from tkinter.filedialog import askdirectory
import os 

# create empty lists for photo id's to be stored to
empty = []
not_empty = []

# def save_button_click(event):
#     if event = left_arrow:
#         not_empty.append(img_name)
#     elif event = right_arrow:
#         empty.append(img_name)

def leftKey(event):
    print ("Left key pressed")

def rightKey(event):
    print ("Right key pressed")

root = tk.Tk()

# frame = Frame(root, width=100, height=100)
# main.bind('<Left>', leftKey)
# main.bind('<Right>', rightKey)
# frame.pack()
# main.mainloop()

root.title("display image")  
im=Image.open("./images/test.jpg")  
photo=ImageTk.PhotoImage(im)  
cv = tk.Canvas()  
cv.pack(side='top', fill='both', expand='yes')  
cv.create_image(50, 50, image=photo, anchor='nw')  
root.geometry("500x500")

root.bind('<Left>', leftKey)
root.bind('<Right>', rightKey)
root.mainloop()


# # Function to load the next image into the Label
# def next_img():
#     img_label.img = tk.PhotoImage(file=next(imgs))
#     img_label.config(image=img_label.img)

# root = tk.Tk()

# # Choose multiple images
# img_dir = askdirectory(parent=root, initialdir="D:/Temp/", title='Choose folder')
# os.chdir(img_dir)
# imgs = iter(os.listdir(img_dir))

# img_label = tk.Label(root)
# img_label.pack()
# img_label.bind("<Button-1>",save_coords)

# btn = tk.Button(root, text='Next image', command=next_img)
# btn.pack()

# next_img() # load first image

# root.mainloop()

# print (coords)


# root = tk.Tk()  
# root.title("display image")  
# im=Image.open("test.jpg")  
# photo=ImageTk.PhotoImage(im)  
# cv = tk.Canvas()  
# cv.pack(side='top', fill='both', expand='yes')  
# cv.create_image(50, 50, image=photo, anchor='nw')  
# root.geometry("500x500")
# root.mainloop()

# # Create empty list for coordinate arrays to be appended to
# coords = []

# # Function to be called when mouse is clicked
# def save_coords(event):
#     click_loc = [event.x, event.y]
#     print ("you clicked on {}".format(click_loc))
#     coords.append(click_loc)

# # Function to load the next image into the Label
# def next_img():
#     img_label.img = tk.PhotoImage(file=next(imgs))
#     img_label.config(image=img_label.img)

# root = tk.Tk()

# # Choose multiple images
# img_dir = askdirectory(parent=root, initialdir="D:/Temp/", title='Choose folder')
# os.chdir(img_dir)
# imgs = iter(os.listdir(img_dir))

# img_label = tk.Label(root)
# img_label.pack()
# img_label.bind("<Button-1>",save_coords)

# btn = tk.Button(root, text='Next image', command=next_img)
# btn.pack()

# next_img() # load first image

# root.mainloop()

# print (coords)

# # shareimprove this answer
